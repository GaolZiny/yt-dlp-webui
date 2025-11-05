#!/bin/bash

# yt-dlp Web UI 启动脚本

echo "🚀 启动 yt-dlp Web UI..."
echo ""

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ 错误: Docker 未安装"
    echo "请先安装 Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

# 检查 Docker Compose 是否安装
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ 错误: Docker Compose 未安装"
    echo "请先安装 Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# 创建下载目录
if [ ! -d "./downloads" ]; then
    echo "📁 创建下载目录..."
    mkdir -p ./downloads
fi

# 停止旧容器（如果存在）
echo "🛑 停止旧容器（如果存在）..."
docker-compose down 2>/dev/null || true

# 构建并启动容器
echo "🔨 构建 Docker 镜像..."
if docker compose version &> /dev/null; then
    docker compose build
else
    docker-compose build
fi

echo "▶️  启动容器..."
if docker compose version &> /dev/null; then
    docker compose up -d
else
    docker-compose up -d
fi

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 3

# 检查容器状态
if docker ps | grep -q yt-dlp-webui; then
    echo ""
    echo "✅ yt-dlp Web UI 已成功启动！"
    echo ""
    echo "📱 访问地址："
    echo "   http://localhost:5000"
    echo ""
    echo "📂 下载目录："
    echo "   $(pwd)/downloads"
    echo ""
    echo "📋 管理命令："
    echo "   查看日志: docker-compose logs -f"
    echo "   停止服务: docker-compose down"
    echo "   重启服务: docker-compose restart"
    echo ""
else
    echo ""
    echo "❌ 启动失败，请查看日志："
    echo "   docker-compose logs"
    echo ""
    exit 1
fi
