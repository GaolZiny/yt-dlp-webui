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

# Execute the main application
exec python app.py
