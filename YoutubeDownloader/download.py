from pytube import YouTube

def download_youtube_video(video_url, output_path):
    # Set custom user agent
    YouTube.DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    yt = YouTube(video_url)
    print("Streams: ",yt.streams())
    stream = yt.streams.filter(res="720p").first()
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Filter streams based on resolution, file extension, etc.
        print("Streams: ",yt.streams())
        stream = yt.streams.filter(res="720p").first()
        # Select the highest quality stream
        # stream = yt.streams.get_highest_resolution()
        
        # Download the video
        stream.download(output_path)
        
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred while downloading the video:", str(e))

video_url = "https://www.youtube.com/watch?v=d4L1Pte7zVc"
output_path = "/downloads/"

download_youtube_video(video_url, output_path)


