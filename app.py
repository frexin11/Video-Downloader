# ─────────────────────────────────────────
# Video Downloader Web App
# Style: Glassmorphism + Gradient (Apple)
# ─────────────────────────────────────────

import streamlit as st
import yt_dlp
import os
import tempfile

# ── 1. Page Config ────────────────────────
st.set_page_config(
    page_title="Video Downloader",
    page_icon="🎬",
    layout="centered"
)

# ── 2. Glass UI CSS ───────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Animated Gradient Background ── */
.stApp {
    background: linear-gradient(
        135deg,
        #0f0c29,
        #302b63,
        #24243e,
        #0f3460,
        #16213e
    );
    background-size: 400% 400%;
    animation: gradientShift 8s ease infinite;
    font-family: 'Inter', sans-serif;
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Hide Streamlit Default UI ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

/* ── Main Container Glass Card ── */
.main .block-container {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 40px !important;
    margin-top: 20px;
    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

/* ── Title ── */
.app-title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(
        135deg,
        #ffffff,
        #a78bfa,
        #60a5fa,
        #34d399
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
    letter-spacing: -1px;
}

/* ── Subtitle ── */
.app-subtitle {
    text-align: center;
    color: rgba(255, 255, 255, 0.5);
    font-size: 15px;
    font-weight: 300;
    margin-bottom: 32px;
    letter-spacing: 0.3px;
}

/* ── Glass Card Component ── */
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    padding: 24px;
    margin: 16px 0;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.glass-card:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

/* ── Text Input ── */
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: white !important;
    font-size: 15px !important;
    padding: 14px 18px !important;
    backdrop-filter: blur(8px) !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: rgba(167, 139, 250, 0.6) !important;
    background: rgba(255, 255, 255, 0.12) !important;
    box-shadow: 0 0 0 3px rgba(167, 139, 250, 0.15) !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(255, 255, 255, 0.3) !important;
}

/* ── Labels ── */
.stTextInput label,
.stRadio label,
p, span, div {
    color: rgba(255, 255, 255, 0.85) !important;
}

/* ── Primary Button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #4f46e5,
        #0ea5e9
    ) !important;
    background-size: 200% 200% !important;
    animation: buttonGlow 3s ease infinite !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 100% !important;
    letter-spacing: 0.3px !important;
    box-shadow:
        0 4px 15px rgba(124, 58, 237, 0.4),
        0 0 30px rgba(79, 70, 229, 0.2) !important;
    transition: all 0.3s ease !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow:
        0 8px 25px rgba(124, 58, 237, 0.5),
        0 0 40px rgba(79, 70, 229, 0.3) !important;
}

@keyframes buttonGlow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Secondary Button ── */
.stButton > button {
    background: rgba(255, 255, 255, 0.08) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    width: 100% !important;
    backdrop-filter: blur(8px) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: rgba(255, 255, 255, 0.15) !important;
    border-color: rgba(255, 255, 255, 0.3) !important;
    transform: translateY(-1px) !important;
}

/* ── Radio Buttons ── */
.stRadio > div {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    padding: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.stRadio > div > label {
    color: rgba(255, 255, 255, 0.85) !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

.stRadio > div > label:hover {
    background: rgba(255, 255, 255, 0.08) !important;
}

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 14px !important;
    padding: 16px !important;
    backdrop-filter: blur(8px) !important;
}

[data-testid="metric-container"] label {
    color: rgba(255, 255, 255, 0.5) !important;
    font-size: 12px !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: white !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

/* ── Divider ── */
hr {
    border-color: rgba(255, 255, 255, 0.08) !important;
    margin: 24px 0 !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    color: white !important;
}

/* ── Success / Error / Info boxes ── */
.stSuccess {
    background: rgba(52, 211, 153, 0.15) !important;
    border: 1px solid rgba(52, 211, 153, 0.3) !important;
    border-radius: 12px !important;
    color: #34d399 !important;
}

.stError {
    background: rgba(239, 68, 68, 0.15) !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    border-radius: 12px !important;
}

.stInfo {
    background: rgba(96, 165, 250, 0.15) !important;
    border: 1px solid rgba(96, 165, 250, 0.3) !important;
    border-radius: 12px !important;
}

/* ── Download Button ── */
.stDownloadButton > button {
    background: linear-gradient(
        135deg,
        #34d399,
        #059669
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 14px !important;
    width: 100% !important;
    box-shadow: 0 4px 15px rgba(52, 211, 153, 0.3) !important;
    transition: all 0.3s ease !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(52, 211, 153, 0.4) !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #a78bfa !important;
}

/* ── Image ── */
.stImage {
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(15, 12, 41, 0.8) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* ── Tags row ── */
.tag {
    display: inline-block;
    background: rgba(167, 139, 250, 0.15);
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 13px;
    color: #a78bfa;
    margin: 4px;
}

/* ── Footer ── */
.footer-text {
    text-align: center;
    color: rgba(255, 255, 255, 0.25);
    font-size: 12px;
    margin-top: 32px;
}
</style>
""", unsafe_allow_html=True)

# ── 3. Header ─────────────────────────────
st.markdown('<p class="app-title">🎬 Video Downloader</p>',
            unsafe_allow_html=True)
st.markdown(
    '<p class="app-subtitle">'
    'Download from YouTube, Instagram, Twitter & 1000+ sites'
    '</p>',
    unsafe_allow_html=True
)

# ── 4. Supported Sites Tags ───────────────
st.markdown("""
<div style="text-align:center; margin-bottom:24px">
    <span class="tag">▶ YouTube</span>
    <span class="tag">📸 Instagram</span>
    <span class="tag">🐦 Twitter</span>
    <span class="tag">📘 Facebook</span>
    <span class="tag">🎵 TikTok</span>
    <span class="tag">🎬 Vimeo</span>
    <span class="tag">+ 1000 more</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── 5. URL Input ──────────────────────────
url = st.text_input(
    "🔗 Video URL",
    placeholder="Paste your video link here...",
    help="Works with YouTube, Instagram, Twitter and 1000+ sites"
)

# ── 6. Format Selection ───────────────────
st.markdown("### ⚙️ Format")
format_option = st.radio(
    "Choose quality:",
    [
        "🎬 MP4 - Best Quality",
        "🎬 MP4 - 1080p",
        "🎬 MP4 - 720p",
        "🎬 MP4 - 480p",
        "🎵 MP3 - Audio Only",
    ],
    horizontal=False,
    label_visibility="collapsed"
)

st.divider()

# ── 7. Helper Functions ───────────────────
def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            'title':      info.get('title', 'Unknown'),
            'duration':   info.get('duration', 0),
            'uploader':   info.get('uploader', 'Unknown'),
            'thumbnail':  info.get('thumbnail', ''),
            'view_count': info.get('view_count', 0),
        }

def format_duration(seconds):
    if not seconds:
        return "Unknown"
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins}:{secs:02d}"

def download_video(url, format_choice, output_path):
    format_map = {
        "🎬 MP4 - Best Quality": {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'ext': 'mp4'
        },
        "🎬 MP4 - 1080p": {
            'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]',
            'ext': 'mp4'
        },
        "🎬 MP4 - 720p": {
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]',
            'ext': 'mp4'
        },
        "🎬 MP4 - 480p": {
            'format': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]',
            'ext': 'mp4'
        },
        "🎵 MP3 - Audio Only": {
            'format': 'bestaudio/best',
            'ext': 'mp3'
        },
    }

    chosen = format_map[format_choice]
    ydl_opts = {
        'format': chosen['format'],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',
    }

    if chosen['ext'] == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info     = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if chosen['ext'] == 'mp3':
            filename = filename.rsplit('.', 1)[0] + '.mp3'
        return filename, info.get('title', 'video')

# ── 8. Fetch Info Button ──────────────────
if url:
    if st.button("🔍 Fetch Video Info"):
        with st.spinner("Fetching video info..."):
            try:
                info = get_video_info(url)
                st.session_state['video_info'] = info
                st.session_state['url'] = url
            except Exception as e:
                st.error(f"❌ Could not fetch: {str(e)}")

# ── 9. Show Video Info ────────────────────
if 'video_info' in st.session_state:
    info = st.session_state['video_info']

    st.divider()

    # Thumbnail
    if info['thumbnail']:
        st.image(
            info['thumbnail'],
            use_container_width=True
        )

    # Stats row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⏱️ Duration",
                  format_duration(info['duration']))
    with col2:
        st.metric("👤 Uploader",
                  info['uploader'][:15])
    with col3:
        views = info['view_count']
        st.metric("👁️ Views",
                  f"{views:,}" if views else "N/A")

    # Title
    st.markdown(f"""
    <div class="glass-card">
        <p style="color:rgba(255,255,255,0.5);
                  font-size:12px;
                  margin-bottom:4px">
            📌 TITLE
        </p>
        <p style="color:white;
                  font-size:16px;
                  font-weight:600;
                  margin:0">
            {info['title']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ── 10. Download Button ───────────────
    if st.button("⬇️ Download Now", type="primary"):
        with st.spinner("⏳ Downloading..."):
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    filepath, title = download_video(
                        st.session_state['url'],
                        format_option,
                        tmp
                    )
                    with open(filepath, 'rb') as f:
                        file_bytes = f.read()

                    ext      = filepath.split('.')[-1]
                    filename = f"{title[:50]}.{ext}"

                    st.success("✅ Ready to save!")

                    st.download_button(
                        label=f"💾 Save {ext.upper()} File",
                        data=file_bytes,
                        file_name=filename,
                        mime=f"video/{ext}"
                              if ext != 'mp3'
                              else "audio/mp3"
                    )

            except Exception as e:
                st.error(f"❌ Failed: {str(e)}")

# ── 11. Empty State ───────────────────────
else:
    st.markdown("""
    <div class="glass-card" style="text-align:center; padding:40px">
        <p style="font-size:48px; margin:0">🎬</p>
        <p style="color:white;
                  font-size:20px;
                  font-weight:600;
                  margin:12px 0 8px">
            Ready to Download
        </p>
        <p style="color:rgba(255,255,255,0.4);
                  font-size:14px;
                  margin:0">
            Paste any video URL above and click Fetch
        </p>
    </div>
    """, unsafe_allow_html=True)

    # How to use steps
    st.markdown("### 📖 How to Use")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="glass-card" style="text-align:center">
            <p style="font-size:32px">🔗</p>
            <p style="color:white; font-weight:600">Paste URL</p>
            <p style="color:rgba(255,255,255,0.4);
                      font-size:13px">
                Copy any video link
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align:center">
            <p style="font-size:32px">⚙️</p>
            <p style="color:white; font-weight:600">Pick Format</p>
            <p style="color:rgba(255,255,255,0.4);
                      font-size:13px">
                MP4 or MP3 quality
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass-card" style="text-align:center">
            <p style="font-size:32px">💾</p>
            <p style="color:white; font-weight:600">Download</p>
            <p style="color:rgba(255,255,255,0.4);
                      font-size:13px">
                Save to your device
            </p>
        </div>
        """, unsafe_allow_html=True)

# ── 12. Footer ────────────────────────────
st.markdown("""
<p class="footer-text">
    Built with yt-dlp + Streamlit • For educational purposes only
</p>
""", unsafe_allow_html=True)