# pip install instaloader
import instaloader

i = instaloader.Instaloader()
username = input("Please enter a username: ")
i.download_profile(username, profile_pic_only=True)