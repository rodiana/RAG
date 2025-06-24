import os
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url_or_id: str) -> str:
    """
    Extracts the video ID from a full YouTube URL or returns the ID if already passed.
    """
    print("Extracting video ID from URL...")
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url_or_id)
    if match:
        print(f"Video ID extracted successfully!")
        return match.group(1)
    elif len(url_or_id) == 11:
        print(f"URL is actually the video ID. Using it!")
        return url_or_id
    else:
        raise ValueError("Invalid YouTube URL or video ID")

def fetch_transcript(video_id: str) -> str:
    """
    Fetches transcript for the given YouTube video ID or URL.
    """
    print("Fetching transcript from video...")
    # video_id = extract_video_id(video_id_or_url)
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise RuntimeError("No transcript found for this video.")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: {e}")
    
    full_text = " ".join([entry["text"] for entry in transcript_list])
    print("Transcript successfully fetched...")
    return full_text

def save_transcript(video_id: str, text: str, output_dir="data/transcripts"):
    """
    Saves the transcript to a .txt file under the given directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{video_id}.txt")
    print(f"Saving transcript to {path}...")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    f.close()
