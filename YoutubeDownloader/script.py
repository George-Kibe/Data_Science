import youtube_dl

# Specify the YouTube video URL
url = "https://www.youtube.com/watch?v=d4L1Pte7zVc"

# Define the options for downloading
options = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

# Create a YouTubeDL object
ydl = youtube_dl.YoutubeDL(options)

# Download the video
ydl.download([url])
