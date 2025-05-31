# YouTube Chapter Extractor

This Python script allows you to extract chapter information from any YouTube video that contains chapters, using the `yt-dlp` tool. It prints the chapter titles and their start times in a human-readable format, and can optionally copy the chapters to your clipboard (with or without timestamps).

## Features
- Fetches chapters from YouTube videos (if available)
- Displays chapter start times in HH:MM:SS format
- Interactive mode: prompts for a URL if none is given
- Option to copy chapters to clipboard (with or without timestamps)
- Colored, user-friendly terminal output
- Validates YouTube URLs and checks for yt-dlp installation

## Requirements
- Python 3.6 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (YouTube video downloader)
- (Optional) [pyperclip](https://pypi.org/project/pyperclip/) for clipboard support

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
3. *(Optional, for clipboard support)*
   ```bash
   pip install pyperclip
   ```

## Usage
### 1. Command-Line Mode
Run the script with a YouTube URL:
```bash
python yt_chapter_extractor.py <YouTube-URL>
```

#### Copy chapters to clipboard (with timestamps):
```bash
python yt_chapter_extractor.py <YouTube-URL> --copy
```

#### Copy only chapter titles to clipboard:
```bash
python yt_chapter_extractor.py <YouTube-URL> --copy-titles
```

### 2. Interactive Mode
If you run the script without arguments (e.g., by double-clicking or just `python yt_chapter_extractor.py`), it will prompt you to enter a YouTube URL. After displaying the chapters, you will be asked if you want to copy the chapters to your clipboard:

```
YouTube Chapter Extractor
Enter YouTube video URL: <paste your URL here>

Chapters for: Example Video Title

00:00:00 - Introduction
00:01:23 - First Topic
00:05:47 - Second Topic
...

Copy chapters to clipboard?
  1. With timestamps
  2. Without timestamps
  3. No (or press Enter)
Choose an option [1/2/3]:
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
