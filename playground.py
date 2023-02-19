from catt.api import CattDevice, discover
import pychromecast
import streamlink

from Extractors import CrunchyRollExtractor

cre = CrunchyRollExtractor('https://www.crunchyroll.com/watch/GK9U313E5/dream')
video_url = cre.videoSource()
subtitle_url = cre.subtitleSource()

cc = pychromecast.get_chromecasts()
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Mesch Cast"])
cast = chromecasts[0]
cast.wait()
mc = cast.media_controller
mc.play_media(video_url, 'application/x-mpegurl')
mc.block_until_active()
print(mc.status)
print('done')

# devices = discover()
# cast = CattDevice(name="Mesch Cast")
# cast.play_url("https://www.crunchyroll.com/watch/GK9U313E5/dream", resolve=True)
# print('h')


# a = "https://monkey-d-luffy.site/v1/files?resolution=default&id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbmltZV9pZCI6Ik1Ua3pORGN3IiwidGltZXN0YW1wIjoxNjc0OTUwMjI2NDUzLCJpcCI6IjczLjE0My4xNzMuNzYiLCJpYXQiOjE2NzQ5NTAyMjZ9.8lpYibsRRbdbKjQwqdpcwEp-bNBB69dBtjHvcnlXQxU"
# cast = CattDevice(name="Mesch Cast")
# cast.play_url(a, resolve=True, block=True)


# from yt_dlp import YoutubeDL
# ydl_opts = {"username": "xeno43", "password": "bubbles"}
# URLS = ['https://www.crunchyroll.com/watch/GK9U313E5/dream']
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download(URLS)