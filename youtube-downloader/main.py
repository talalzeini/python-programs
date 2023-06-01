# pip install pytube
from pytube import YouTube

print("\n\nYoutube Video Donwloader")
link = input("\nPlease enter the URL of the video: ")

yt = YouTube(link)
videos = yt.streams

dn_video = videos[1]
dn_video.download()

print("\nDownloaded Succesfully\n")