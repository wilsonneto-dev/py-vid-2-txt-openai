from moviepy.editor import *

def extract_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_mp4_file> <path_to_mp3_file>")
        return

    mp4_file_path = sys.argv[1]
    mp3_file_path = sys.argv[2]
    extract_mp3(mp4_file_path, mp3_file_path)

if __name__ == "__main__":
    main()