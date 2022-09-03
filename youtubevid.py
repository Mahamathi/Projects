#youtube video downloader
from pytube import YouTube
link=str(input("Enter the Video Link:"))
yt=YouTube(link)
stream=yt.streams.get_highest_resolution()
stream.download()
print("VIDEO DOWNLOADED SUCCESSFULLY")