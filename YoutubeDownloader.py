
#import the youtube library
from pytube import YouTube
import time
#gets the link and create the var
link = input("Video link: ")
yt = YouTube(link)

#print views and the title from video
print("Title: ", yt.title)
print("Views: ", yt.views)


#choose the best quality
yd = yt.streams.get_highest_resolution()

#download in my donwload directory
yd.download('/Users/luigi/Downloads')
print("Finished")
time.sleep(8)