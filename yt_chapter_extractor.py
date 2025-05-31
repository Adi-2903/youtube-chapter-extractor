import subprocess
import json

def get_chapters_ytdlp(url):
    try:
        # Run yt-dlp to fetch metadata in JSON
        result = subprocess.run(
            ['yt-dlp', '--dump-json', url],
            capture_output=True, text=True
        )

        data = json.loads(result.stdout)

        if "chapters" not in data or not data["chapters"]:
            print("No chapters found in this video.")
            return

        print(f"\nChapters for: {data['title']}\n")
        for chapter in data["chapters"]:
            start_time = chapter["start_time"]
            title = chapter["title"]
            # Convert seconds to HH:MM:SS
            hh = int(start_time // 3600)
            mm = int((start_time % 3600) // 60)
            ss = int(start_time % 60)
            print(f"{hh:02}:{mm:02}:{ss:02} - {title}")

    except Exception as e:
        print(f"Error: {e}")

# Use the video URL here
video_url = "https://www.youtube.com/watch?v=4HyTlbHUKSw"
get_chapters_ytdlp(video_url)
