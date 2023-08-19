from pytube import YouTube
import os

def download_video(youtube_url, choice, output_path):
    try:
        yt = YouTube(youtube_url)
        print("Video Title:", yt.title)

        if choice == '1':
            video_stream = yt.streams.filter(only_audio=True).first()
        elif choice == '2':
            video_stream = yt.streams.get_highest_resolution()
        else:
            print("Invalid choice.")
            return

        video_stream.download(output_path=output_path)
        print("Download finished.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    link = input("Enter the video link: ")
    choice = input("Enter '1' for audio or '2' for video: ")
    
    output_folder = input("Enter the output folder (leave blank for current directory): ")
    if not output_folder:
        output_folder = os.getcwd()
    
    download_video(link, choice, output_path=output_folder)
    input("Press any key to exit...")
