import subprocess
import json
import sys
import shutil
import re

try:
    from pyperclip import copy as copy_to_clipboard
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False

# ANSI color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_help():
    print(f"{Colors.BOLD}YouTube Chapter Extractor{Colors.ENDC}")
    print("Usage: python yt_chapter_extractor.py <YouTube-URL> [--copy]")
    print("\nOptions:")
    print("  --copy     Copy the chapter list to clipboard (with timestamps, requires pyperclip)")
    print("  -h, --help Show this help message and exit\n")

def check_ytdlp():
    if not shutil.which('yt-dlp'):
        print(f"{Colors.FAIL}Error: yt-dlp is not installed or not in PATH.{Colors.ENDC}")
        print("Install it from https://github.com/yt-dlp/yt-dlp or with 'pip install yt-dlp'.")
        sys.exit(1)

def is_valid_youtube_url(url):
    # Basic check for YouTube URL
    pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$"
    return re.match(pattern, url) is not None

def get_chapters_ytdlp(url, copy_clipboard=False, copy_mode='with_timestamp', interactive=False):
    try:
        # Run yt-dlp to fetch metadata in JSON
        result = subprocess.run(
            ['yt-dlp', '--dump-json', url],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"{Colors.FAIL}yt-dlp error:{Colors.ENDC} {result.stderr.strip()}")
            return
        data = json.loads(result.stdout)
        if "chapters" not in data or not data["chapters"]:
            print(f"{Colors.WARNING}No chapters found in this video.{Colors.ENDC}")
            return
        print(f"\n{Colors.HEADER}Chapters for: {Colors.BOLD}{data['title']}{Colors.ENDC}\n")
        chapter_lines = []
        chapter_titles = []
        for chapter in data["chapters"]:
            start_time = chapter["start_time"]
            title = chapter["title"]
            # Convert seconds to HH:MM:SS
            hh = int(start_time // 3600)
            mm = int((start_time % 3600) // 60)
            ss = int(start_time % 60)
            line = f"{Colors.OKGREEN}{hh:02}:{mm:02}:{ss:02}{Colors.ENDC} - {Colors.OKCYAN}{title}{Colors.ENDC}"
            print(line)
            chapter_lines.append(f"{hh:02}:{mm:02}:{ss:02} - {title}")
            chapter_titles.append(title)
        # Interactive copy prompt
        if interactive and HAS_CLIPBOARD:
            print(f"\nCopy chapters to clipboard?")
            print("  1. With timestamps")
            print("  2. Without timestamps")
            print("  3. No (or press Enter)")
            choice = input("Choose an option [1/2/3]: ").strip()
            if choice == '1':
                copy_to_clipboard("\n".join(chapter_lines))
                print(f"{Colors.OKBLUE}Chapters (with timestamps) copied to clipboard!{Colors.ENDC}")
            elif choice == '2':
                copy_to_clipboard("\n".join(chapter_titles))
                print(f"{Colors.OKBLUE}Chapters (titles only) copied to clipboard!{Colors.ENDC}")
            else:
                print("No chapters copied.")
        elif copy_clipboard:
            if HAS_CLIPBOARD:
                if copy_mode == 'with_timestamp':
                    copy_to_clipboard("\n".join(chapter_lines))
                    print(f"\n{Colors.OKBLUE}Chapters (with timestamps) copied to clipboard!{Colors.ENDC}")
                elif copy_mode == 'titles_only':
                    copy_to_clipboard("\n".join(chapter_titles))
                    print(f"\n{Colors.OKBLUE}Chapters (titles only) copied to clipboard!{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}pyperclip not installed. Cannot copy to clipboard.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error: {e}{Colors.ENDC}")

def main():
    url = None
    copy_flag = False
    copy_mode = 'with_timestamp'
    interactive = False
    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print_help()
        return
    # Check for URL argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
        copy_flag = '--copy' in sys.argv
        # Optionally allow --copy-titles for titles only
        if '--copy-titles' in sys.argv:
            copy_flag = True
            copy_mode = 'titles_only'
    else:
        # Interactive prompt if no URL provided
        print(f"{Colors.BOLD}YouTube Chapter Extractor{Colors.ENDC}")
        url = input("Enter YouTube video URL: ").strip()
        interactive = True
    if not is_valid_youtube_url(url):
        print(f"{Colors.FAIL}Error: The provided URL does not appear to be a valid YouTube link.{Colors.ENDC}")
        print("Example: https://www.youtube.com/watch?v=... or https://youtu.be/...")
        return
    check_ytdlp()
    get_chapters_ytdlp(url, copy_clipboard=copy_flag, copy_mode=copy_mode, interactive=interactive)

if __name__ == "__main__":
    main()
