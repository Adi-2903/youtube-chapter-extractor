# YouTube Chapter Extractor

This Python script allows you to extract chapter information from any YouTube video that contains chapters, using the `yt-dlp` tool. It prints the chapter titles and their start times in a human-readable format.

## Features
- Fetches chapters from YouTube videos (if available)
- Displays chapter start times in HH:MM:SS format
- Simple and easy to use

## Requirements
- Python 3.6 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (YouTube video downloader)

## Installation
1. **Clone this repository or download the script.**
2. **Install yt-dlp:**
   ```bash
   pip install yt-dlp
   ```
   Or, for system-wide installation:
   ```bash
   pip install -U yt-dlp
   ```

## Usage
1. Edit the `video_url` variable in `yt_chapter_extractor.py.py` to the YouTube video you want to extract chapters from.
2. Run the script:
   ```bash
   python "yt_chapter_extractor.py.py"
   ```

## Example Output
```
Chapters for: Example Video Title

00:00:00 - Introduction
00:01:23 - First Topic
00:05:47 - Second Topic
...
```
If the video has no chapters, you'll see:
```
No chapters found in this video.
```

## License
This project is open source. You may use it as you wish. 