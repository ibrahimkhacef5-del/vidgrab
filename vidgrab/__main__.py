import sys
from .core import download, color

BANNER = r"""
  ██╗   ██╗██╗██████╗  ██████╗ ██████╗  █████╗ ██████╗
  ██║   ██║██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
  ██║   ██║██║██║  ██║██║  ███╗██████╔╝███████║██████╔╝
  ╚██╗ ██╔╝██║██║  ██║██║   ██║██╔══██╗██╔══██║██╔══██╗
   ╚████╔╝ ██║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
    ╚═══╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
"""

def help_text():
    print(color(BANNER, "cyan"))
    print(color("  VidGrab - تحميل الفيديوهات من كل المواقع\n", "yellow"))
    print("الأوامر:")
    print("  vidgrab <url>              ← تحميل بأفضل جودة")
    print("  vidgrab 720 <url>          ← تحميل بجودة 720p")
    print("  vidgrab 1080 <url>         ← تحميل بجودة 1080p")
    print("  vidgrab audio <url>        ← تحميل الصوت فقط (MP3)\n")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        help_text()
        sys.exit(0)

    cmd = sys.argv[1]

    # الأوامر
    if cmd == "audio" and len(sys.argv) >= 3:
        url = sys.argv[2]
        print(color(f"\n⬇️ جاري تحميل الصوت من: {url}", "cyan"))
        download(url, "bestaudio/best")
    
    elif cmd in ("360", "480", "720", "1080") and len(sys.argv) >= 3:
        quality = cmd
        url = sys.argv[2]
        print(color(f"\n⬇️ جاري تحميل الفيديو بجودة {quality}p من: {url}", "cyan"))
        download(url, f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]")
    
    else:
        # رابط مباشر
        url = cmd
        print(color(f"\n⬇️ جاري تحميل: {url}", "cyan"))
        download(url)

if __name__ == "__main__":
    main()
