# 🚀 部署指南 / Deployment Guide

本指南将帮助你将 yt-dlp Web UI 部署到新的 GitHub 仓库。

---

## 📋 步骤 1：在 GitHub 创建新仓库

1. 访问 [GitHub](https://github.com)
2. 点击右上角的 "+" → "New repository"
3. 填写信息：
   - **Repository name**: `yt-dlp-webui` （或你喜欢的名字）
   - **Description**: `A beautiful web UI for yt-dlp - Download videos and audio from 1000+ websites`
   - **Public/Private**: 选择 Public（公开）或 Private（私有）
   - **⚠️ 不要勾选**：
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license
   （因为我们已经准备好这些文件了）
4. 点击 "Create repository"

---

## 📋 步骤 2：准备项目文件

在你的 Mac 上，创建一个新的项目目录：

```bash
# 1. 创建新目录
mkdir ~/yt-dlp-webui
cd ~/yt-dlp-webui

# 2. 初始化 Git
git init

# 3. 从旧项目复制文件
cp -r ~/Desktop/dev/yt-dlp/yt-dlp/web-ui/* .

# 或者如果你还在 yt-dlp 目录内
# cd ~/Desktop/dev/yt-dlp/yt-dlp/web-ui
# cp -r ./* ~/yt-dlp-webui/
```

---

## 📋 步骤 3：清理和优化

```bash
cd ~/yt-dlp-webui

# 删除旧的 README，使用新的
rm README.md QUICKSTART.md
mv README_NEW.md README.md

# 查看项目结构
ls -la
```

应该看到以下文件：
```
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── docker-compose.yml
├── requirements.txt
├── start.sh
├── stop.sh
└── templates/
    └── index.html
```

---

## 📋 步骤 4：推送到 GitHub

```bash
# 1. 添加所有文件
git add .

# 2. 创建第一次提交
git commit -m "Initial commit: yt-dlp Web UI

- Beautiful web interface for yt-dlp
- Support video and audio downloads
- Support 1000+ websites
- Docker ready
- Real-time progress tracking
- File management"

# 3. 添加远程仓库（替换为你的 GitHub 用户名和仓库名）
git remote add origin https://github.com/你的用户名/yt-dlp-webui.git

# 4. 推送到 GitHub
git branch -M main
git push -u origin main
```

---

## 📋 步骤 5：验证部署

访问你的 GitHub 仓库页面，应该能看到：

- ✅ README 显示正常，有完整的文档
- ✅ 代码结构清晰
- ✅ LICENSE 文件存在

---

## 📋 步骤 6：测试部署

### 在本地测试

```bash
cd ~/yt-dlp-webui

# 使用 Docker
docker-compose up -d

# 或本地运行
python app.py
```

访问：http://localhost:8080

### 在 NAS 上部署

1. 从 GitHub 克隆项目到 NAS：
   ```bash
   cd /你的NAS路径
   git clone https://github.com/你的用户名/yt-dlp-webui.git
   cd yt-dlp-webui
   ```

2. 修改 docker-compose.yml：
   ```yaml
   volumes:
     - /volume1/downloads:/downloads  # 改为你的 NAS 路径
   ```

3. 启动服务：
   ```bash
   docker-compose up -d
   ```

4. 访问：http://NAS地址:8080

---

## 🎯 可选步骤

### 添加项目截图

1. 运行应用，截图界面
2. 在 GitHub 仓库创建 `screenshots` 目录
3. 上传截图
4. 在 README.md 中添加：
   ```markdown
   ### 📸 界面预览

   ![主界面](screenshots/main.png)
   ![下载中](screenshots/downloading.png)
   ```

### 添加 GitHub Topics

在 GitHub 仓库页面：
1. 点击右侧的 "About" 旁边的设置图标
2. 添加 Topics（标签）：
   - `yt-dlp`
   - `video-downloader`
   - `youtube-dl`
   - `web-ui`
   - `flask`
   - `docker`
   - `nas`

### 启用 GitHub Actions（可选）

创建 `.github/workflows/docker-build.yml` 自动构建 Docker 镜像。

---

## 🎉 完成！

现在你有了一个独立的、干净的 GitHub 项目！

**项目链接**：`https://github.com/你的用户名/yt-dlp-webui`

你可以：
- 分享给其他人使用
- 接收 Issues 和 Pull Requests
- 持续改进功能

---

## 📝 后续维护

### 更新代码

```bash
cd ~/yt-dlp-webui

# 修改代码...

git add .
git commit -m "描述你的修改"
git push
```

### 更新 NAS 上的部署

```bash
cd /你的NAS路径/yt-dlp-webui

# 拉取最新代码
git pull

# 重新构建并启动
docker-compose down
docker-compose up -d --build
```

---

## ❓ 常见问题

**Q: 如何改变仓库名？**
- 在 GitHub 仓库 Settings → General → Repository name

**Q: 如何设为私有仓库？**
- 在 GitHub 仓库 Settings → Danger Zone → Change visibility

**Q: 推送时需要密码？**
- 使用 GitHub Personal Access Token 代替密码
- Settings → Developer settings → Personal access tokens

**Q: 如何让别人贡献代码？**
- Public 仓库：任何人都可以提 Pull Request
- Private 仓库：需要邀请协作者

---

需要帮助？查看 [GitHub 文档](https://docs.github.com) 或提交 Issue。
