#!/bin/bash

# yt-dlp Web UI 停止脚本

echo "🛑 停止 yt-dlp Web UI..."
echo ""

# 停止容器
if docker compose version &> /dev/null; then
    docker compose down
else
    docker-compose down
fi

echo ""
echo "✅ yt-dlp Web UI 已停止"
echo ""
