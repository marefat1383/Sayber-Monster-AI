import os
import shutil

def ensure_tmp_dir():
    os.makedirs("tmp_uploads", exist_ok=True)

def handle_upload(uploaded_file) -> str:
    ensure_tmp_dir()
    file_path = os.path.join("tmp_uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def extract_audio_if_video(file_path: str) -> str:
    """
    If the file is an mp4, extract the audio to a wav file.
    Otherwise, assume it's audio and return it (or convert to wav if necessary).
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.mp4':
        try:
            from moviepy.editor import VideoFileClip
        except ImportError:
            raise RuntimeError("The 'moviepy' package failed to install (likely due to disk space). Video extraction is unavailable. Please upload .wav or .mp3 files instead.")
            
        wav_path = file_path.replace('.mp4', '.wav')
        # Extract audio using moviepy
        try:
            video = VideoFileClip(file_path)
            audio = video.audio
            audio.write_audiofile(wav_path, logger=None)
            audio.close()
            video.close()
            return wav_path
        except Exception as e:
            # Fallback if ffmpeg is missing
            raise RuntimeError(f"Error extracting audio: {e}")
            
    return file_path

def clear_tmp_dir():
    if os.path.exists("tmp_uploads"):
        shutil.rmtree("tmp_uploads")
    ensure_tmp_dir()
