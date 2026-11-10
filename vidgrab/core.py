
import os
import yt_dlp
from pathlib import Path

OUT_DIR = Path("/sdcard/VidGrab")

COLORS = {
    "red": "\033[1;31m", "green": "\033[1;32m",
    "yellow": "\033[1;33m", "cyan": "\033[1;36m", "reset": "\033[0m",
}

def color(t, c):
    return f"{COLORS.get(c, '')}{t}{COLORS['reset']}"

def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "?").strip()
        speed = d.get("_speed_str", "?").strip()
        print(f"\r  ⬇ {percent} | سرعة: {speed}  ", end="", flush=True)
    elif d["status"] == "finished":
        print(color("\n  ✓ اكتمل التحميل", "green"))

def download(url, quality="best"):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        "outtmpl": str(OUT_DIR / "%(title)s.%(ext)s"),
        "format": quality,
        "progress_hooks": [progress_hook],
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(color(f"\n✅ تم التحميل: {info['title']}", "green"))
            return True
    except Exception as e:
        print(color(f"\n❌ فشل التحميل: {e}", "red"))
        return False
