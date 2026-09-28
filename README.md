# 🎬 Video Downloader

A simple and clean web application to download videos from
YouTube, Instagram, Twitter and 1000+ websites.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.64-red)
![yt-dlp](https://img.shields.io/badge/yt--dlp-2026-green)

---

## ✨ Features

- 🌐 Download from 1000+ websites
- 🎬 Multiple video quality options (480p, 720p, 1080p, Best)
- 🎵 Audio only download (MP3)
- 📋 Video info preview before downloading
- 🖼️ Thumbnail preview
- 🎨 Clean dark themed UI

---

## 🌐 Supported Sites

| Platform | Status |
|----------|--------|
| YouTube | ✅ |
| Instagram | ✅ |
| Twitter/X | ✅ |
| Facebook | ✅ |
| TikTok | ✅ |
| Vimeo | ✅ |
| Reddit | ✅ |
| Twitch | ✅ |
| 1000+ more | ✅ |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| yt-dlp | Video downloading engine |
| Streamlit | Web interface |
| ffmpeg | Video conversion |

---

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/frexin11/video-downloader
cd video-downloader

### 2. Create environment
conda create -n video_downloader python=3.11
conda activate video_downloader

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install ffmpeg
brew install ffmpeg

### 5. Run the app
streamlit run app.py

---

## 📁 Project Structure

video_downloader/
├── app.py              # Main Streamlit web app
├── requirements.txt    # Python dependencies
├── run.sh             # Quick run script
└── README.md          # Project documentation

---

## 📖 How to Use

1. **Paste URL** — Copy any video link and paste it
2. **Fetch Info** — Click to see video details and thumbnail
3. **Choose Format** — Select quality or audio only
4. **Download** — Click download and save to device

---

## ⚙️ Download Formats

| Format | Quality | Best For |
|--------|---------|----------|
| MP4 Best | Highest available | Best quality |
| MP4 1080p | Full HD | Normal use |
| MP4 720p | HD | Smaller size |
| MP4 480p | SD | Smallest size |
| MP3 | Audio only | Music/Podcasts |

---

## ⚠️ Disclaimer

This tool is built for **educational purposes only**.
Please respect copyright laws and terms of service
of each platform when downloading content.

---

## 🎓 About

- Python web application
- Integration of open source tools
- Clean UI/UX design with Streamlit

**Built by:** Frexin
**Year:** 2026
