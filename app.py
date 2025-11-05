#!/usr/bin/env python3
"""
yt-dlp Web UI - A web interface for yt-dlp
"""

import os
import json
import subprocess
import threading
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
# Default to './downloads' for local development, '/downloads' for Docker
default_download_dir = '/downloads' if os.path.exists('/.dockerenv') else './downloads'
DOWNLOAD_DIR = Path(os.environ.get('DOWNLOAD_DIR', default_download_dir))
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Store download tasks
download_tasks = {}
task_lock = threading.Lock()


def get_download_status(task_id):
    """Get the status of a download task"""
    with task_lock:
        return download_tasks.get(task_id, {})


def update_download_status(task_id, status):
    """Update the status of a download task"""
    with task_lock:
        if task_id not in download_tasks:
            download_tasks[task_id] = {}
        download_tasks[task_id].update(status)


def run_ytdlp_download(task_id, url, options):
    """Run yt-dlp download in a separate thread"""
    try:
        # Build yt-dlp command
        cmd = ['yt-dlp']

        # Output directory
        output_template = str(DOWNLOAD_DIR / '%(title)s.%(ext)s')
        cmd.extend(['-o', output_template])

        # Download mode: audio or video
        if options.get('mode') == 'audio':
            cmd.append('-x')  # Extract audio
            audio_format = options.get('audio_format', 'mp3')
            cmd.extend(['--audio-format', audio_format])

            # Audio quality
            audio_quality = options.get('audio_quality', '5')
            cmd.extend(['--audio-quality', audio_quality])
        else:
            # Video format
            video_format = options.get('video_format', 'best')
            cmd.extend(['-f', video_format])

        # Embed thumbnail
        if options.get('embed_thumbnail'):
            cmd.append('--embed-thumbnail')

        # Embed metadata
        if options.get('embed_metadata'):
            cmd.append('--embed-metadata')

        # Subtitles
        if options.get('write_subs'):
            cmd.append('--write-subs')
            cmd.append('--sub-lang')
            cmd.append(options.get('sub_lang', 'en'))

        # Progress output
        cmd.append('--newline')
        cmd.append('--no-playlist')  # Default to single video

        # Add URL
        cmd.append(url)

        update_download_status(task_id, {
            'status': 'downloading',
            'progress': 0,
            'message': 'Starting download...',
            'command': ' '.join(cmd)
        })

        # Execute yt-dlp
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )

        # Read output
        output_lines = []
        for line in process.stdout:
            output_lines.append(line.strip())

            # Parse progress
            if '[download]' in line and '%' in line:
                try:
                    # Extract percentage
                    parts = line.split()
                    for part in parts:
                        if '%' in part:
                            percent = float(part.replace('%', ''))
                            update_download_status(task_id, {
                                'status': 'downloading',
                                'progress': percent,
                                'message': line.strip()
                            })
                            break
                except:
                    pass

        process.wait()

        if process.returncode == 0:
            update_download_status(task_id, {
                'status': 'completed',
                'progress': 100,
                'message': 'Download completed successfully!',
                'output': '\n'.join(output_lines)
            })
        else:
            update_download_status(task_id, {
                'status': 'failed',
                'progress': 0,
                'message': 'Download failed. See output for details.',
                'output': '\n'.join(output_lines)
            })

    except Exception as e:
        update_download_status(task_id, {
            'status': 'failed',
            'progress': 0,
            'message': f'Error: {str(e)}'
        })


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/download', methods=['POST'])
def download():
    """Start a new download"""
    data = request.get_json()
    url = data.get('url', '').strip()

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Generate task ID
    task_id = datetime.now().strftime('%Y%m%d_%H%M%S_%f')

    # Options
    options = {
        'mode': data.get('mode', 'video'),  # 'audio' or 'video'
        'audio_format': data.get('audio_format', 'mp3'),
        'audio_quality': data.get('audio_quality', '5'),
        'video_format': data.get('video_format', 'best'),
        'embed_thumbnail': data.get('embed_thumbnail', False),
        'embed_metadata': data.get('embed_metadata', True),
        'write_subs': data.get('write_subs', False),
        'sub_lang': data.get('sub_lang', 'en')
    }

    # Initialize task status
    update_download_status(task_id, {
        'url': url,
        'status': 'pending',
        'progress': 0,
        'message': 'Task created',
        'created_at': datetime.now().isoformat()
    })

    # Start download in a separate thread
    thread = threading.Thread(
        target=run_ytdlp_download,
        args=(task_id, url, options),
        daemon=True
    )
    thread.start()

    return jsonify({
        'task_id': task_id,
        'message': 'Download started'
    })


@app.route('/api/status/<task_id>')
def status(task_id):
    """Get the status of a download task"""
    task_status = get_download_status(task_id)

    if not task_status:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify(task_status)


@app.route('/api/files')
def list_files():
    """List all downloaded files"""
    files = []

    for file_path in DOWNLOAD_DIR.iterdir():
        if file_path.is_file():
            stat = file_path.stat()
            files.append({
                'name': file_path.name,
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
            })

    # Sort by modified time (newest first)
    files.sort(key=lambda x: x['modified'], reverse=True)

    return jsonify({'files': files})


@app.route('/api/download-file/<path:filename>')
def download_file(filename):
    """Download a file from the server to the client"""
    # Security check: prevent directory traversal attacks
    if '..' in filename or filename.startswith('/'):
        return jsonify({'error': 'Invalid filename'}), 400

    file_path = DOWNLOAD_DIR / filename

    if not file_path.exists() or not file_path.is_file():
        return jsonify({'error': 'File not found'}), 404

    # Check that the file is actually in the download directory (prevent path traversal)
    try:
        file_path.resolve().relative_to(DOWNLOAD_DIR.resolve())
    except ValueError:
        return jsonify({'error': 'Invalid file path'}), 400

    return send_file(
        file_path,
        as_attachment=True,
        download_name=filename
    )


@app.route('/api/delete-file/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    """Delete a file from the server"""
    # Security check: prevent directory traversal attacks
    if '..' in filename or filename.startswith('/'):
        return jsonify({'error': 'Invalid filename'}), 400

    file_path = DOWNLOAD_DIR / filename

    if not file_path.exists() or not file_path.is_file():
        return jsonify({'error': 'File not found'}), 404

    # Check that the file is actually in the download directory (prevent path traversal)
    try:
        file_path.resolve().relative_to(DOWNLOAD_DIR.resolve())
    except ValueError:
        return jsonify({'error': 'Invalid file path'}), 400

    try:
        file_path.unlink()
        return jsonify({'message': 'File deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Use port from environment variable or default to 8080
    # (5000 is often used by macOS AirPlay Receiver)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
