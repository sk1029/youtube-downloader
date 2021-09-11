from pytube import YouTube

URL = input("enter URL of the youtube video: ")
My_video = YouTube(URL)

print("video title")
print(My_video.title)

print("thumbnail")
print(My_video.thumbnail_url)

print("downloading")

My_video = My_video.streams.get_highest_resolution()
My_video.d
