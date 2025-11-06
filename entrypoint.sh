#!/bin/bash
set -e

echo "=================================================="
echo "🚀 Starting yt-dlp Web UI"
echo "=================================================="

# Update yt-dlp to the latest version
echo "📦 Checking for yt-dlp updates..."
pip install --upgrade --no-cache-dir yt-dlp > /dev/null 2>&1

# Get yt-dlp version
YT_DLP_VERSION=$(yt-dlp --version)
echo "✅ yt-dlp version: $YT_DLP_VERSION"

# Get ffmpeg version
FFMPEG_VERSION=$(ffmpeg -version 2>&1 | head -n 1 | cut -d ' ' -f 3)
echo "✅ ffmpeg version: $FFMPEG_VERSION"

echo "=================================================="
echo "🌐 Starting web server on port 8080..."
echo "=================================================="

# Get port from environment or use default
PORT=${PORT:-8080}

# Execute the main application with gunicorn
# - app:app means module 'app' and Flask instance 'app'
# - --bind 0.0.0.0:$PORT listens on all interfaces
# - --workers 4 uses 4 worker processes for better performance
# - --timeout 300 allows long-running downloads (5 minutes)
# - --graceful-timeout 30 gives workers time to finish on shutdown
# - --access-logfile - logs requests to stdout
exec gunicorn app:app \
    --bind 0.0.0.0:$PORT \
    --workers 4 \
    --timeout 300 \
    --graceful-timeout 30 \
    --access-logfile - \
    --error-logfile -
