# Docker 部署指南 / Docker Deployment Guide

## 中文

### GitHub Container Registry 自动构建

本项目已配置 GitHub Actions 自动构建和推送 Docker 镜像到 GitHub Container Registry (GHCR)。

#### 工作流程

1. **自动触发**：当代码推送到 `main` 分支或创建版本标签时自动构建
2. **多架构支持**：自动构建 X86/AMD64 和 ARM64 架构镜像
3. **标签策略**：
   - `latest` - 最新的 main 分支版本
   - `v1.2.3` - 语义化版本号（需要创建 git tag）
   - `sha-xxxxx` - 基于 git commit SHA

#### 首次设置

**无需额外配置！** GitHub Actions 会自动使用 `GITHUB_TOKEN` 推送镜像到 GHCR。

#### 发布新版本

**方法1：推送到 main 分支**（自动更新 `latest` 标签）
```bash
git push origin main
```

**方法2：创建版本标签**（创建特定版本）
```bash
# 创建标签
git tag v1.0.0
git push origin v1.0.0

# 镜像将发布为：
# - ghcr.io/gaolziny/yt-dlp-webui:latest
# - ghcr.io/gaolziny/yt-dlp-webui:1.0.0
# - ghcr.io/gaolziny/yt-dlp-webui:1.0
# - ghcr.io/gaolziny/yt-dlp-webui:1
```

#### 在 NAS 上使用

**Synology NAS：**

1. 打开 Container Manager
2. 在"注册表"中添加：
   - 注册表 URL: `https://ghcr.io`
   - 搜索：`gaolziny/yt-dlp-webui`
3. 下载 `latest` 标签
4. 创建容器，配置：
   ```yaml
   端口映射: 8080:8080
   卷: /volume1/downloads/yt-dlp:/downloads
   环境变量: TZ=Asia/Shanghai
   自动重启: 是
   ```

**QNAP NAS：**

1. 打开 Container Station
2. 创建容器，镜像设置为：`ghcr.io/gaolziny/yt-dlp-webui:latest`
3. 端口映射：`8080:8080`
4. 共享文件夹：将下载目录挂载到 `/downloads`

**命令行方式：**

```bash
docker pull ghcr.io/gaolziny/yt-dlp-webui:latest

docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v /your/nas/path:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  ghcr.io/gaolziny/yt-dlp-webui:latest
```

#### 更新镜像

**方法1：Docker 管理界面**
- 当有新版本时，界面会显示更新提示
- 点击"更新"按钮即可

**方法2：命令行**
```bash
# 拉取最新镜像
docker pull ghcr.io/gaolziny/yt-dlp-webui:latest

# 停止并删除旧容器
docker stop yt-dlp-webui
docker rm yt-dlp-webui

# 使用新镜像创建容器
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v /your/nas/path:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  ghcr.io/gaolziny/yt-dlp-webui:latest
```

#### 查看可用版本

访问：https://github.com/GaolZiny/yt-dlp-webui/pkgs/container/yt-dlp-webui

或使用命令：
```bash
# 需要安装 GitHub CLI
gh api /user/packages/container/yt-dlp-webui/versions
```

---

## English

### GitHub Container Registry Auto-Build

This project is configured with GitHub Actions to automatically build and push Docker images to GitHub Container Registry (GHCR).

#### Workflow

1. **Auto-trigger**: Builds automatically when code is pushed to `main` branch or version tags are created
2. **Multi-architecture**: Automatically builds for X86/AMD64 and ARM64 architectures
3. **Tagging strategy**:
   - `latest` - Latest main branch version
   - `v1.2.3` - Semantic version numbers (requires git tag)
   - `sha-xxxxx` - Based on git commit SHA

#### Initial Setup

**No additional configuration needed!** GitHub Actions automatically uses `GITHUB_TOKEN` to push images to GHCR.

#### Releasing New Versions

**Method 1: Push to main branch** (auto-update `latest` tag)
```bash
git push origin main
```

**Method 2: Create version tag** (create specific version)
```bash
# Create tag
git tag v1.0.0
git push origin v1.0.0

# Images will be published as:
# - ghcr.io/gaolziny/yt-dlp-webui:latest
# - ghcr.io/gaolziny/yt-dlp-webui:1.0.0
# - ghcr.io/gaolziny/yt-dlp-webui:1.0
# - ghcr.io/gaolziny/yt-dlp-webui:1
```

#### Using on NAS

**Synology NAS:**

1. Open Container Manager
2. Add registry:
   - Registry URL: `https://ghcr.io`
   - Search: `gaolziny/yt-dlp-webui`
3. Download `latest` tag
4. Create container with settings:
   ```yaml
   Port mapping: 8080:8080
   Volume: /volume1/downloads/yt-dlp:/downloads
   Environment: TZ=Asia/Shanghai
   Auto-restart: Yes
   ```

**QNAP NAS:**

1. Open Container Station
2. Create container with image: `ghcr.io/gaolziny/yt-dlp-webui:latest`
3. Port mapping: `8080:8080`
4. Shared folder: Mount download directory to `/downloads`

**Command Line:**

```bash
docker pull ghcr.io/gaolziny/yt-dlp-webui:latest

docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v /your/nas/path:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  ghcr.io/gaolziny/yt-dlp-webui:latest
```

#### Updating the Image

**Method 1: Docker Management UI**
- Update notification will appear when new version is available
- Click "Update" button

**Method 2: Command Line**
```bash
# Pull latest image
docker pull ghcr.io/gaolziny/yt-dlp-webui:latest

# Stop and remove old container
docker stop yt-dlp-webui
docker rm yt-dlp-webui

# Create container with new image
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v /your/nas/path:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  ghcr.io/gaolziny/yt-dlp-webui:latest
```

#### View Available Versions

Visit: https://github.com/GaolZiny/yt-dlp-webui/pkgs/container/yt-dlp-webui

Or use command:
```bash
# Requires GitHub CLI
gh api /user/packages/container/yt-dlp-webui/versions
```

---

## 故障排除 / Troubleshooting

### 无法拉取镜像 / Cannot Pull Image

**问题 / Issue**: `Error response from daemon: manifest unknown`

**解决方案 / Solution**:
1. 确保镜像已成功构建（检查 GitHub Actions）
2. 确认镜像名称正确：`ghcr.io/gaolziny/yt-dlp-webui:latest`
3. 检查网络连接到 ghcr.io

### 架构不匹配 / Architecture Mismatch

**问题 / Issue**: `exec format error`

**解决方案 / Solution**:
- 镜像支持 `linux/amd64` 和 `linux/arm64`
- Docker 会自动选择正确的架构
- 如果问题持续，请在 Issues 中报告您的 NAS 型号和架构

### 权限问题 / Permission Issues

**问题 / Issue**: 下载的文件无法访问

**解决方案 / Solution**:
```bash
# 在宿主机上设置正确的权限
sudo chown -R 1000:1000 /your/download/path
```
