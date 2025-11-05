# yt-dlp Web UI

一个美观、易用的 yt-dlp Web 界面，支持通过浏览器下载视频和音频。

## ✨ 功能特性

- 🎥 **视频下载** - 支持多种视频质量选择（720p、1080p、4K等）
- 🎵 **音频下载** - 支持提取音频并转换为MP3、AAC、FLAC等格式
- 📊 **实时进度** - 实时显示下载进度和状态
- 📁 **文件管理** - 查看、下载和删除已下载的文件
- 🎨 **美观界面** - 现代化的响应式设计，支持移动端
- 🐳 **Docker支持** - 一键部署，轻松运行在NAS上
- 🌍 **多网站支持** - 支持 YouTube、Bilibili 等 1000+ 个网站

## 📋 前提条件

- Docker 和 Docker Compose（用于容器化部署）
- 或者 Python 3.10+（用于本地运行）

## 🚀 快速开始

### 方法一：使用 Docker Compose（推荐）

1. **克隆或下载项目文件**

2. **编辑 `docker-compose.yml` 设置下载目录**

   打开 `docker-compose.yml`，找到 `volumes` 部分：

   ```yaml
   volumes:
     # 将 ./downloads 改为你 NAS 上的实际路径
     # 例如：/volume1/downloads/yt-dlp:/downloads
     - ./downloads:/downloads
   ```

3. **构建并启动容器**

   ```bash
   cd web-ui
   docker-compose up -d
   ```

4. **访问 Web 界面**

   打开浏览器，访问：`http://你的NAS地址:8080`

### 方法二：使用 Docker 命令

```bash
# 构建镜像
docker build -t yt-dlp-webui .

# 运行容器
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v /你的下载路径:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  yt-dlp-webui
```

### 方法三：本地运行（开发模式）

```bash
# 安装依赖
pip install -r requirements.txt
pip install yt-dlp

# 安装 ffmpeg（必需）
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: 从 https://ffmpeg.org/download.html 下载

# 运行应用
python app.py
```

访问：`http://localhost:8080`

## 📖 使用说明

### 下载视频

1. 在"视频/音频链接"输入框中粘贴视频URL
2. 选择"视频"模式
3. 选择视频质量（可选）
4. 勾选需要的选项（嵌入缩略图、元数据、字幕等）
5. 点击"开始下载"

### 下载音频

1. 在"视频/音频链接"输入框中粘贴视频URL
2. 选择"音频"模式
3. 选择音频格式（MP3、AAC、FLAC等）
4. 设置音频质量（0-10，0为最佳）
5. 点击"开始下载"

### 管理文件

- **查看文件**：在"已下载文件"区域查看所有已下载的文件
- **下载到本地**：点击文件旁边的"📥 下载"按钮，文件会下载到你的浏览器本地
- **删除文件**：点击"🗑️ 删除"按钮删除服务器上的文件
- **刷新列表**：点击"🔄 刷新列表"按钮更新文件列表

## ⚙️ 配置选项

### 环境变量

在 `docker-compose.yml` 中可以设置以下环境变量：

```yaml
environment:
  - DOWNLOAD_DIR=/downloads  # 下载目录
  - TZ=Asia/Shanghai         # 时区设置
```

### 音频格式说明

- **MP3** - 最常用，兼容性好
- **AAC** - 相同比特率下质量优于MP3
- **M4A** - Apple设备友好
- **Opus** - 高效的现代编码格式
- **FLAC** - 无损格式，文件较大
- **WAV** - 未压缩无损，文件最大

### 视频质量说明

- **最佳质量** - 下载最高质量的视频
- **最佳视频+音频** - 分别下载最佳视频和音频并合并
- **720p / 1080p / 4K** - 指定分辨率
- **最低质量** - 下载最小的文件（节省空间）

## 🔧 高级配置

### 在 NAS 上设置共享文件夹

1. 在 Synology NAS 上创建共享文件夹（如 `yt-dlp-downloads`）
2. 修改 `docker-compose.yml`：

   ```yaml
   volumes:
     - /volume1/yt-dlp-downloads:/downloads
   ```

3. 通过 SMB/NFS 在你的电脑上访问该共享文件夹

### 自定义端口

如果8080端口被占用，可以修改 `docker-compose.yml`：

```yaml
ports:
  - "9090:8080"  # 将主机端口改为其他端口
```

或者通过环境变量设置：

```yaml
environment:
  - PORT=9090  # 容器内使用的端口
```

### 持久化配置

如果需要保存 yt-dlp 配置文件：

```yaml
volumes:
  - ./downloads:/downloads
  - ./config:/root/.config/yt-dlp  # 添加配置目录映射
```

## 🐛 故障排除

### 下载失败

1. **检查 URL** - 确保URL有效且网站被 yt-dlp 支持
2. **查看日志**：
   ```bash
   docker logs yt-dlp-webui
   ```
3. **更新 yt-dlp**：
   ```bash
   docker-compose down
   docker-compose build --no-cache
   docker-compose up -d
   ```

### 无法访问 Web 界面

1. **检查容器状态**：
   ```bash
   docker ps
   ```
2. **检查防火墙**：确保 5000 端口开放
3. **检查 NAS 网络设置**

### 音频转换失败

- 确保 ffmpeg 已安装（Docker 镜像中已包含）
- 检查是否有足够的磁盘空间

## 📝 支持的网站

yt-dlp 支持 1000+ 个网站，包括但不限于：

- YouTube
- Bilibili
- Twitter
- Facebook
- Instagram
- TikTok
- Vimeo
- Twitch
- 等等...

完整列表：https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## 🔄 更新

### 更新 Docker 镜像

```bash
cd web-ui
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### 更新 yt-dlp

在容器内更新：

```bash
docker exec -it yt-dlp-webui pip install --upgrade yt-dlp
docker restart yt-dlp-webui
```

或者重新构建镜像（推荐）。

## 📂 项目结构

```
web-ui/
├── app.py                 # Flask 应用主程序
├── templates/
│   └── index.html        # Web 界面 HTML
├── Dockerfile            # Docker 镜像配置
├── docker-compose.yml    # Docker Compose 配置
├── requirements.txt      # Python 依赖
└── README.md            # 项目说明文档
```

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可证

本项目基于 Unlicense 许可证开源。

yt-dlp 本身也是开源项目：https://github.com/yt-dlp/yt-dlp

## ⚠️ 免责声明

本工具仅供学习和个人使用。请遵守相关网站的服务条款和版权法律。下载受版权保护的内容可能是非法的。使用本工具的风险由用户自行承担。

## 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [Flask](https://flask.palletsprojects.com/) - Web 框架
- [FFmpeg](https://ffmpeg.org/) - 多媒体处理工具
