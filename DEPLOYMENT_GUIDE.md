# 🚀 部署指南 / Deployment Guide / デプロイガイド

[English](#english) | [中文](#中文) | [日本語](#日本語)

---

## 中文

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

---

## English

This guide will help you deploy yt-dlp Web UI to a new GitHub repository.

---

### 📋 Step 1: Create New Repository on GitHub

1. Visit [GitHub](https://github.com)
2. Click "+" in top right → "New repository"
3. Fill in information:
   - **Repository name**: `yt-dlp-webui` (or your preferred name)
   - **Description**: `A beautiful web UI for yt-dlp - Download videos and audio from 1000+ websites`
   - **Public/Private**: Choose Public or Private
   - **⚠️ Do NOT check**:
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license
   (Because we already have these files)
4. Click "Create repository"

---

### 📋 Step 2: Prepare Project Files

On your Mac, create a new project directory:

```bash
# 1. Create new directory
mkdir ~/yt-dlp-webui
cd ~/yt-dlp-webui

# 2. Initialize Git
git init

# 3. Copy files from old project
cp -r ~/Desktop/dev/yt-dlp/yt-dlp/web-ui/* .

# Or if you're still in yt-dlp directory
# cd ~/Desktop/dev/yt-dlp/yt-dlp/web-ui
# cp -r ./* ~/yt-dlp-webui/
```

---

### 📋 Step 3: Clean Up and Optimize

```bash
cd ~/yt-dlp-webui

# Delete old README, use new one
rm README.md QUICKSTART.md
mv README_NEW.md README.md

# View project structure
ls -la
```

You should see these files:
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

### 📋 Step 4: Push to GitHub

```bash
# 1. Add all files
git add .

# 2. Create first commit
git commit -m "Initial commit: yt-dlp Web UI

- Beautiful web interface for yt-dlp
- Support video and audio downloads
- Support 1000+ websites
- Docker ready
- Real-time progress tracking
- File management"

# 3. Add remote repository (replace with your username and repo name)
git remote add origin https://github.com/yourusername/yt-dlp-webui.git

# 4. Push to GitHub
git branch -M main
git push -u origin main
```

---

### 📋 Step 5: Verify Deployment

Visit your GitHub repository page, you should see:

- ✅ README displays properly with complete documentation
- ✅ Code structure is clear
- ✅ LICENSE file exists

---

### 📋 Step 6: Test Deployment

#### Test Locally

```bash
cd ~/yt-dlp-webui

# Using Docker
docker-compose up -d

# Or run locally
python app.py
```

Visit: http://localhost:8080

#### Deploy on NAS

1. Clone project from GitHub to NAS:
   ```bash
   cd /your/nas/path
   git clone https://github.com/yourusername/yt-dlp-webui.git
   cd yt-dlp-webui
   ```

2. Modify docker-compose.yml:
   ```yaml
   volumes:
     - /volume1/downloads:/downloads  # Change to your NAS path
   ```

3. Start service:
   ```bash
   docker-compose up -d
   ```

4. Visit: http://NAS-IP:8080

---

### 🎯 Optional Steps

#### Add Screenshots

1. Run the app and take screenshots
2. Create `screenshots` directory in GitHub repo
3. Upload screenshots
4. Add to README.md:
   ```markdown
   ### 📸 Interface Preview

   ![Main Interface](screenshots/main.png)
   ![Downloading](screenshots/downloading.png)
   ```

#### Add GitHub Topics

On GitHub repository page:
1. Click settings icon next to "About"
2. Add Topics (tags):
   - `yt-dlp`
   - `video-downloader`
   - `youtube-dl`
   - `web-ui`
   - `flask`
   - `docker`
   - `nas`

#### Enable GitHub Actions (Optional)

Create `.github/workflows/docker-build.yml` for automatic Docker image building.

---

### 🎉 Done!

Now you have a clean, independent GitHub project!

**Project Link**: `https://github.com/yourusername/yt-dlp-webui`

You can:
- Share with others
- Receive Issues and Pull Requests
- Continue improving features

---

### 📝 Ongoing Maintenance

#### Update Code

```bash
cd ~/yt-dlp-webui

# Make changes...

git add .
git commit -m "Describe your changes"
git push
```

#### Update Deployment on NAS

```bash
cd /your/nas/path/yt-dlp-webui

# Pull latest code
git pull

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

---

### ❓ FAQ

**Q: How to change repository name?**
- Go to GitHub repository Settings → General → Repository name

**Q: How to make repository private?**
- Go to GitHub repository Settings → Danger Zone → Change visibility

**Q: Need password when pushing?**
- Use GitHub Personal Access Token instead of password
- Settings → Developer settings → Personal access tokens

**Q: How to let others contribute?**
- Public repo: Anyone can submit Pull Requests
- Private repo: Need to invite collaborators

---

Need help? Check [GitHub Docs](https://docs.github.com) or submit an Issue.

---

## 日本語

このガイドは、yt-dlp Web UIを新しいGitHubリポジトリにデプロイする方法を説明します。

---

### 📋 ステップ1：GitHubで新しいリポジトリを作成

1. [GitHub](https://github.com)にアクセス
2. 右上の「+」→「New repository」をクリック
3. 情報を入力：
   - **Repository name**: `yt-dlp-webui` （またはお好みの名前）
   - **Description**: `A beautiful web UI for yt-dlp - Download videos and audio from 1000+ websites`
   - **Public/Private**: PublicまたはPrivateを選択
   - **⚠️ チェックしないでください**：
     - ❌ Add a README file
     - ❌ Add .gitignore
     - ❌ Choose a license
   （これらのファイルは既に用意されているため）
4. 「Create repository」をクリック

---

### 📋 ステップ2：プロジェクトファイルを準備

Macで新しいプロジェクトディレクトリを作成：

```bash
# 1. 新しいディレクトリを作成
mkdir ~/yt-dlp-webui
cd ~/yt-dlp-webui

# 2. Gitを初期化
git init

# 3. 旧プロジェクトからファイルをコピー
cp -r ~/Desktop/dev/yt-dlp/yt-dlp/web-ui/* .

# または、yt-dlpディレクトリ内にいる場合
# cd ~/Desktop/dev/yt-dlp/yt-dlp/web-ui
# cp -r ./* ~/yt-dlp-webui/
```

---

### 📋 ステップ3：クリーンアップと最適化

```bash
cd ~/yt-dlp-webui

# 古いREADMEを削除し、新しいものを使用
rm README.md QUICKSTART.md
mv README_NEW.md README.md

# プロジェクト構造を確認
ls -la
```

以下のファイルが表示されるはずです：
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

### 📋 ステップ4：GitHubにプッシュ

```bash
# 1. すべてのファイルを追加
git add .

# 2. 最初のコミットを作成
git commit -m "Initial commit: yt-dlp Web UI

- Beautiful web interface for yt-dlp
- Support video and audio downloads
- Support 1000+ websites
- Docker ready
- Real-time progress tracking
- File management"

# 3. リモートリポジトリを追加（ユーザー名とリポジトリ名を置き換えてください）
git remote add origin https://github.com/yourusername/yt-dlp-webui.git

# 4. GitHubにプッシュ
git branch -M main
git push -u origin main
```

---

### 📋 ステップ5：デプロイを確認

GitHubリポジトリページにアクセスし、以下を確認：

- ✅ READMEが正しく表示され、完全なドキュメントがある
- ✅ コード構造が明確
- ✅ LICENSEファイルが存在する

---

### 📋 ステップ6：デプロイをテスト

#### ローカルでテスト

```bash
cd ~/yt-dlp-webui

# Dockerを使用
docker-compose up -d

# またはローカルで実行
python app.py
```

アクセス：http://localhost:8080

#### NASにデプロイ

1. GitHubからNASにプロジェクトをクローン：
   ```bash
   cd /your/nas/path
   git clone https://github.com/yourusername/yt-dlp-webui.git
   cd yt-dlp-webui
   ```

2. docker-compose.ymlを変更：
   ```yaml
   volumes:
     - /volume1/downloads:/downloads  # NASのパスに変更
   ```

3. サービスを起動：
   ```bash
   docker-compose up -d
   ```

4. アクセス：http://NASのIP:8080

---

### 🎯 オプションステップ

#### スクリーンショットを追加

1. アプリを実行してスクリーンショットを撮影
2. GitHubリポジトリに`screenshots`ディレクトリを作成
3. スクリーンショットをアップロード
4. README.mdに追加：
   ```markdown
   ### 📸 インターフェースプレビュー

   ![メイン画面](screenshots/main.png)
   ![ダウンロード中](screenshots/downloading.png)
   ```

#### GitHub Topicsを追加

GitHubリポジトリページで：
1. 「About」の横の設定アイコンをクリック
2. Topics（タグ）を追加：
   - `yt-dlp`
   - `video-downloader`
   - `youtube-dl`
   - `web-ui`
   - `flask`
   - `docker`
   - `nas`

#### GitHub Actionsを有効化（オプション）

自動Dockerイメージビルド用に`.github/workflows/docker-build.yml`を作成。

---

### 🎉 完了！

これで、クリーンで独立したGitHubプロジェクトができました！

**プロジェクトリンク**：`https://github.com/yourusername/yt-dlp-webui`

以下が可能です：
- 他の人と共有
- IssueとPull Requestを受け取る
- 機能を継続的に改善

---

### 📝 継続的なメンテナンス

#### コードを更新

```bash
cd ~/yt-dlp-webui

# 変更を加える...

git add .
git commit -m "変更内容を説明"
git push
```

#### NAS上のデプロイを更新

```bash
cd /your/nas/path/yt-dlp-webui

# 最新のコードを取得
git pull

# 再ビルドして再起動
docker-compose down
docker-compose up -d --build
```

---

### ❓ よくある質問

**Q: リポジトリ名を変更するには？**
- GitHubリポジトリのSettings → General → Repository name

**Q: リポジトリを非公開にするには？**
- GitHubリポジトリのSettings → Danger Zone → Change visibility

**Q: プッシュ時にパスワードが必要？**
- パスワードの代わりにGitHub Personal Access Tokenを使用
- Settings → Developer settings → Personal access tokens

**Q: 他の人にコードを貢献してもらうには？**
- Publicリポジトリ：誰でもPull Requestを提出可能
- Privateリポジトリ：コラボレーターを招待する必要があります

---

ヘルプが必要ですか？[GitHubドキュメント](https://docs.github.com)を確認するか、Issueを提出してください。
