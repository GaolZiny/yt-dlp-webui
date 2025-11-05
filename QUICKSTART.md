# 快速开始指南

## 🚀 一键启动（推荐）

### 在 macOS 或 Linux 上：

```bash
cd web-ui
./start.sh
```

### 在 Windows 上：

```bash
cd web-ui
docker-compose up -d
```

然后在浏览器打开：`http://localhost:8080`

## 📦 完整步骤

### 1. 确保已安装 Docker

检查 Docker 是否已安装：
```bash
docker --version
docker-compose --version
```

如果未安装，请访问：https://docs.docker.com/get-docker/

### 2. 配置下载目录（可选）

编辑 `docker-compose.yml`，修改下载目录映射：

```yaml
volumes:
  # 将 ./downloads 改为你想要的路径
  - ./downloads:/downloads
```

### 3. 启动服务

```bash
# 方式1：使用脚本（macOS/Linux）
./start.sh

# 方式2：使用 Docker Compose
docker-compose up -d
```

### 4. 访问 Web 界面

打开浏览器访问：`http://localhost:8080`

如果在 NAS 上运行，访问：`http://NAS的IP地址:8080`

## 🎯 基本使用

### 下载视频

1. 复制视频链接（如 YouTube、Bilibili）
2. 粘贴到 Web 界面的输入框
3. 选择"视频"模式
4. 点击"开始下载"

### 下载音频（MP3）

1. 复制视频链接
2. 粘贴到 Web 界面的输入框
3. 选择"音频"模式
4. 选择格式（推荐 MP3）
5. 点击"开始下载"

### 下载文件到本地电脑

1. 在"已下载文件"列表中找到文件
2. 点击"📥 下载"按钮
3. 文件会下载到你的浏览器下载目录

## 🛠️ 常用命令

```bash
# 查看运行日志
docker-compose logs -f

# 停止服务
docker-compose down
# 或使用脚本
./stop.sh

# 重启服务
docker-compose restart

# 更新 yt-dlp
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# 查看容器状态
docker ps
```

## ❓ 常见问题

### 无法访问 Web 界面？

1. 检查容器是否运行：`docker ps`
2. 检查端口是否被占用：`lsof -i :8080`（macOS/Linux）
3. 检查防火墙设置

### 下载失败？

1. 确认 URL 是否正确
2. 检查网站是否被 yt-dlp 支持
3. 查看日志：`docker-compose logs -f`
4. 尝试更新 yt-dlp

### 如何改变端口？

编辑 `docker-compose.yml`：

```yaml
ports:
  - "9090:8080"  # 将主机端口改为其他端口
```

## 🎉 开始使用

现在你可以愉快地下载视频和音频了！支持 1000+ 个网站，包括：

- YouTube
- Bilibili
- Twitter
- Instagram
- TikTok
- 等等...

享受使用吧！🎊
