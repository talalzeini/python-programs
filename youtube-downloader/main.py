from pytube import YouTube
# Install pytube using the following commands
# pip install pytube
# or
# python3 -m pip install pytube

print("\n\nYoutube Video Donwloader")
link = input("\nPlease enter the URL of the video: ")
yt = YouTube(link)
videos = yt.streams

dn_video = videos[1]
dn_video.download()

print("\nDownloaded Succesfully\n")
