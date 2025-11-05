# yt-dlp Web UI

<div align="center">

![yt-dlp Web UI](https://img.shields.io/badge/yt--dlp-Web%20UI-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

一个美观、易用的 **yt-dlp** Web 界面，支持通过浏览器下载 1000+ 个网站的视频和音频。

[English](#english) | [中文](#中文) | [日本語](#日本語)

</div>

---

## 中文

### ✨ 功能特性

- 🎥 **视频下载** - 支持多种视频质量（720p、1080p、4K、最佳质量）
- 🎵 **音频下载** - 支持 MP3、AAC、M4A、Opus、FLAC、WAV 等格式
- 📊 **实时进度** - 实时显示下载进度和状态
- 📁 **文件管理** - 查看、下载和删除已下载的文件
- 🎨 **美观界面** - 现代化的响应式设计，支持移动端
- 🐳 **Docker 支持** - 一键部署，轻松运行在 NAS 上
- 🌍 **多网站支持** - 支持 YouTube、Bilibili、Twitter、Instagram、TikTok 等 1000+ 个网站

### 📸 界面预览

- 简洁的渐变色界面
- 支持音频/视频模式切换
- 实时下载进度显示
- 文件列表管理

### 🚀 快速开始

#### 使用 Docker Compose（推荐）

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/yt-dlp-webui.git
cd yt-dlp-webui

# 2. 启动服务
docker-compose up -d

# 3. 访问 Web 界面
# 打开浏览器访问：http://localhost:8080
```

#### 使用 Docker

```bash
# 构建镜像
docker build -t yt-dlp-webui .

# 运行容器
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v $(pwd)/downloads:/downloads \
  -e TZ=Asia/Shanghai \
  --restart unless-stopped \
  yt-dlp-webui
```

#### 本地运行

```bash
# 1. 安装依赖
pip install -r requirements.txt
pip install yt-dlp

# 2. 安装 ffmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: https://ffmpeg.org/download.html

# 3. 运行应用
python app.py

# 4. 访问：http://localhost:8080
```

### 📖 使用说明

#### 下载视频

1. 在"视频/音频链接"输入框中粘贴视频 URL
2. 选择"视频"模式
3. 选择视频质量（720p、1080p、4K 等）
4. 点击"开始下载"

#### 下载音频

1. 在"视频/音频链接"输入框中粘贴视频 URL
2. 选择"音频"模式
3. 选择音频格式（推荐 MP3）
4. 设置音频质量（0-10，0 为最佳）
5. 点击"开始下载"

#### 管理文件

- **查看文件**：在"已下载文件"区域查看所有文件
- **下载到本地**：点击"📥 下载"按钮
- **删除文件**：点击"🗑️ 删除"按钮

### ⚙️ 配置

#### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `DOWNLOAD_DIR` | 下载目录 | `/downloads` (Docker) 或 `./downloads` (本地) |
| `PORT` | Web 服务端口 | `8080` |
| `TZ` | 时区 | `UTC` |

#### docker-compose.yml

```yaml
services:
  yt-dlp-webui:
    build: .
    container_name: yt-dlp-webui
    ports:
      - "8080:8080"
    volumes:
      # 修改为你的下载目录
      - ./downloads:/downloads
    environment:
      - DOWNLOAD_DIR=/downloads
      - TZ=Asia/Shanghai
    restart: unless-stopped
```

### 🔧 高级功能

#### 音频格式说明

- **MP3** - 最常用，兼容性好
- **AAC** - 相同比特率下质量优于 MP3
- **M4A** - Apple 设备友好
- **Opus** - 高效的现代编码格式
- **FLAC** - 无损格式，文件较大
- **WAV** - 未压缩无损，文件最大

#### 视频质量说明

- **最佳质量** - 下载最高质量的视频
- **720p / 1080p / 4K** - 指定分辨率（如果源没有会自动降级）
- **最低质量** - 下载最小的文件（节省空间）

#### 在 NAS 上部署

1. 将项目复制到 NAS
2. 修改 `docker-compose.yml` 中的下载目录：
   ```yaml
   volumes:
     - /volume1/downloads/yt-dlp:/downloads  # Synology
   ```
3. 运行 `docker-compose up -d`
4. 访问 `http://NAS地址:8080`

### 📝 支持的网站

yt-dlp 支持 1000+ 个网站，包括但不限于：

- **视频平台**：YouTube, Bilibili, Vimeo, Dailymotion
- **社交媒体**：Twitter, Facebook, Instagram, TikTok
- **直播平台**：Twitch, YouTube Live
- **其他**：更多网站请查看 [支持列表](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

### 🐛 故障排除

#### 下载失败

1. 检查 URL 是否有效
2. 检查网站是否被 yt-dlp 支持
3. 查看日志：`docker-compose logs -f`
4. 更新 yt-dlp：重新构建镜像

#### 无法访问界面

1. 检查容器状态：`docker ps`
2. 检查端口是否开放
3. 检查防火墙设置

#### macOS 端口冲突

如果 8080 端口被占用，修改 `docker-compose.yml`：

```yaml
ports:
  - "9090:8080"  # 改为其他端口
```

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。

### 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [Flask](https://flask.palletsprojects.com/) - Web 框架
- [FFmpeg](https://ffmpeg.org/) - 多媒体处理工具

### ⚠️ 免责声明

本工具仅供学习和个人使用。请遵守相关网站的服务条款和版权法律。

---

## English

### ✨ Features

- 🎥 **Video Downloads** - Support multiple quality options (720p, 1080p, 4K, best quality)
- 🎵 **Audio Extraction** - Extract and convert to MP3, AAC, M4A, Opus, FLAC, WAV
- 📊 **Real-time Progress** - Live download progress tracking
- 📁 **File Management** - View, download, and delete files
- 🎨 **Beautiful UI** - Modern responsive design, mobile-friendly
- 🐳 **Docker Support** - Easy deployment on NAS or servers
- 🌍 **1000+ Sites** - YouTube, Bilibili, Twitter, Instagram, TikTok, and more

### 🚀 Quick Start

#### Using Docker Compose (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/yt-dlp-webui.git
cd yt-dlp-webui

# 2. Start the service
docker-compose up -d

# 3. Access the web interface
# Open browser: http://localhost:8080
```

#### Using Docker

```bash
# Build the image
docker build -t yt-dlp-webui .

# Run the container
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v $(pwd)/downloads:/downloads \
  --restart unless-stopped \
  yt-dlp-webui
```

#### Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt
pip install yt-dlp

# 2. Install ffmpeg
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: https://ffmpeg.org/download.html

# 3. Run the application
python app.py

# 4. Visit: http://localhost:8080
```

### 📖 Usage

#### Download Video

1. Paste video URL in the input field
2. Select "Video" mode
3. Choose video quality
4. Click "Start Download"

#### Download Audio

1. Paste video URL in the input field
2. Select "Audio" mode
3. Choose audio format (MP3 recommended)
4. Set audio quality (0-10, 0 is best)
5. Click "Start Download"

#### Manage Files

- **View Files**: Check all downloaded files
- **Download to Local**: Click "📥 Download" button
- **Delete Files**: Click "🗑️ Delete" button

### ⚙️ Configuration

#### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DOWNLOAD_DIR` | Download directory | `/downloads` (Docker) or `./downloads` (local) |
| `PORT` | Web service port | `8080` |
| `TZ` | Timezone | `UTC` |

### 📝 Supported Sites

yt-dlp supports 1000+ websites including:

- **Video Platforms**: YouTube, Bilibili, Vimeo, Dailymotion
- **Social Media**: Twitter, Facebook, Instagram, TikTok
- **Live Streaming**: Twitch, YouTube Live
- **More**: See [full list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

### 🤝 Contributing

Issues and Pull Requests are welcome!

### 📄 License

This project is licensed under the [MIT License](LICENSE).

### 🙏 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Powerful video downloader
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [FFmpeg](https://ffmpeg.org/) - Multimedia processing

### ⚠️ Disclaimer

This tool is for educational and personal use only. Please comply with the terms of service and copyright laws of relevant websites.

---

## 日本語

### ✨ 機能

- 🎥 **動画ダウンロード** - 複数の品質オプションに対応（720p、1080p、4K、最高品質）
- 🎵 **音声抽出** - MP3、AAC、M4A、Opus、FLAC、WAV形式に変換
- 📊 **リアルタイム進捗** - ダウンロード進捗をリアルタイムで表示
- 📁 **ファイル管理** - ファイルの表示、ダウンロード、削除
- 🎨 **美しいUI** - モダンなレスポンシブデザイン、モバイル対応
- 🐳 **Docker対応** - NASやサーバーへの簡単なデプロイ
- 🌍 **1000以上のサイト対応** - YouTube、Bilibili、Twitter、Instagram、TikTokなど

### 📸 インターフェース

- シンプルなグラデーションデザイン
- 音声/動画モード切替
- リアルタイムダウンロード進捗表示
- ファイルリスト管理
- プレイリストサポート - URLを入力して動画を選択し、一括ダウンロード

### 🚀 クイックスタート

#### Docker Composeを使用（推奨）

```bash
# 1. リポジトリをクローン
git clone https://github.com/あなたのユーザー名/yt-dlp-webui.git
cd yt-dlp-webui

# 2. サービスを起動
docker-compose up -d

# 3. Webインターフェースにアクセス
# ブラウザで開く：http://localhost:8080
```

#### Dockerを使用

```bash
# イメージをビルド
docker build -t yt-dlp-webui .

# コンテナを実行
docker run -d \
  --name yt-dlp-webui \
  -p 8080:8080 \
  -v $(pwd)/downloads:/downloads \
  --restart unless-stopped \
  yt-dlp-webui
```

#### ローカル開発

```bash
# 1. 依存関係をインストール
pip install -r requirements.txt
pip install yt-dlp

# 2. ffmpegをインストール
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: https://ffmpeg.org/download.html

# 3. アプリケーションを実行
python app.py

# 4. アクセス：http://localhost:8080
```

### 📖 使い方

#### 動画をダウンロード

1. 入力フィールドに動画URLを貼り付け
2. 「動画」モードを選択
3. 動画品質を選択
4. 「ダウンロード開始」をクリック

#### 音声をダウンロード

1. 入力フィールドに動画URLを貼り付け
2. 「音声」モードを選択
3. 音声形式を選択（MP3推奨）
4. 音声品質を設定（0-10、0が最高）
5. 「ダウンロード開始」をクリック

#### プレイリストをダウンロード

1. プレイリストのURLを入力
2. 「🔍 プレイリストを確認」をクリック
3. ダウンロードする動画を選択（「すべて選択」/「すべて解除」も使用可能）
4. 動画または音声モードを選択
5. 「ダウンロード開始」をクリック

#### ファイルを管理

- **ファイルを表示**：ダウンロード済みファイルをすべて確認
- **ローカルにダウンロード**：「📥 ダウンロード」ボタンをクリック
- **ファイルを削除**：「🗑️ 削除」ボタンをクリック

### ⚙️ 設定

#### 環境変数

| 変数 | 説明 | デフォルト値 |
|------|------|------------|
| `DOWNLOAD_DIR` | ダウンロードディレクトリ | `/downloads`（Docker）または`./downloads`（ローカル） |
| `PORT` | Webサービスポート | `8080` |
| `TZ` | タイムゾーン | `UTC` |

#### docker-compose.yml

```yaml
services:
  yt-dlp-webui:
    build: .
    container_name: yt-dlp-webui
    ports:
      - "8080:8080"
    volumes:
      # ダウンロードディレクトリを変更
      - ./downloads:/downloads
    environment:
      - DOWNLOAD_DIR=/downloads
      - TZ=Asia/Tokyo
    restart: unless-stopped
```

### 🔧 高度な機能

#### 音声形式の説明

- **MP3** - 最も一般的で、互換性が高い
- **AAC** - 同じビットレートでMP3より高品質
- **M4A** - Appleデバイスに最適
- **Opus** - 効率的な最新エンコード形式
- **FLAC** - 無損失形式、ファイルサイズが大きい
- **WAV** - 非圧縮無損失、最大のファイルサイズ

#### 動画品質の説明

- **最高品質** - 最高品質の動画をダウンロード
- **720p / 1080p / 4K** - 指定した解像度（ソースにない場合は自動的に低下）
- **最低品質** - 最小のファイルをダウンロード（容量節約）

#### NASへのデプロイ

1. プロジェクトをNASにコピー
2. `docker-compose.yml`のダウンロードディレクトリを変更：
   ```yaml
   volumes:
     - /volume1/downloads/yt-dlp:/downloads  # Synology
   ```
3. `docker-compose up -d`を実行
4. `http://NASのアドレス:8080`にアクセス

### 📝 対応サイト

yt-dlpは1000以上のウェブサイトに対応しています：

- **動画プラットフォーム**：YouTube、Bilibili、Vimeo、Dailymotion
- **ソーシャルメディア**：Twitter、Facebook、Instagram、TikTok
- **ライブ配信**：Twitch、YouTube Live
- **その他**：[完全なリスト](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)を参照

### 🐛 トラブルシューティング

#### ダウンロード失敗

1. URLが有効か確認
2. yt-dlpがサイトに対応しているか確認
3. ログを確認：`docker-compose logs -f`
4. yt-dlpを更新：イメージを再ビルド

#### インターフェースにアクセスできない

1. コンテナの状態を確認：`docker ps`
2. ポートが開いているか確認
3. ファイアウォール設定を確認

#### macOSでポート競合

8080ポートが使用中の場合、`docker-compose.yml`を変更：

```yaml
ports:
  - "9090:8080"  # 別のポートに変更
```

### 🤝 コントリビューション

IssueとPull Requestを歓迎します！

### 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下でオープンソース化されています。

### 🙏 クレジット

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 強力な動画ダウンローダー
- [Flask](https://flask.palletsprojects.com/) - Webフレームワーク
- [FFmpeg](https://ffmpeg.org/) - マルチメディア処理ツール

### ⚠️ 免責事項

このツールは教育および個人使用のみを目的としています。関連ウェブサイトの利用規約と著作権法を遵守してください。
