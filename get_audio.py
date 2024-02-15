import os
from pytube import YouTube

def Download(link):
    ytVideo = YouTube(link)
    ytVideo = ytVideo.streams.get_by_itag(140)
    try:
        downloadedVideo=ytVideo.download()
        baseName, ext = os.path.splitext(downloadedVideo) 
        audioConverted = baseName + '.mp3'
        os.rename(downloadedVideo, audioConverted) 
    except:
        return False, ""
    return True, baseName 