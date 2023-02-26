from catt.api import CattDevice, discover
import pychromecast
import streamlink
import logging
import time

from Extractors import CrunchyRollExtractor

# cre = CrunchyRollExtractor.CrunchyRollExtractor('https://www.crunchyroll.com/watch/GK9U313E5/dream')
# video_url = cre.videoSource()
# print(video_url)
# exit()
# subtitle_url = cre.subtitleSource()
video_url = "https://pl.crunchyroll.com/evs3/ec3d3d217582ac276450d89e342476c7/assets/417f3f055a8db35e7d50cdde8135d56b_,4785803.mp4,4785804.mp4,4785802.mp4,4785800.mp4,4785801.mp4,.urlset/master.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly9wbC5jcnVuY2h5cm9sbC5jb20vZXZzMy9lYzNkM2QyMTc1ODJhYzI3NjQ1MGQ4OWUzNDI0NzZjNy9hc3NldHMvNDE3ZjNmMDU1YThkYjM1ZTdkNTBjZGRlODEzNWQ1NmJfLDQ3ODU4MDMubXA0LDQ3ODU4MDQubXA0LDQ3ODU4MDIubXA0LDQ3ODU4MDAubXA0LDQ3ODU4MDEubXA0LC51cmxzZXQvbWFzdGVyLm0zdTgiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NzcxMDc0MzR9fX1dfQ__&Signature=nzR4mQZBnULAm5cAnJ8wokmZRwQIYTrVTGFMNu-pwoeqz5sfovyD6FFYMYKMTSjMlVJVTZ9HOCG9b~bU1J5RCZofSZMQLho9m8HOOjSaYzbtFVHh8z2rDh8uEZ4sF4fkAP2KfN7qMCnSjbLRaXpi9zGnrZaecyV6n8M1RVpqRUnPY0gvJ6rpXwphiM5mr9cYs6SWWhCyBVjY6LhVZxQ-3bfygtpoBDOl3MxWK~po91saVDlBpxUY2n~IzKYGt0-9Cpf~8xkyVLdd104K7G~EImZO-6zauj31EDvFr2DRcC24J-wxNZoyJ122FK4DyDyC6TsRBy4DE7hwaDl88YdpIg__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA"
# video_url = "https://pl.crunchyroll.com/evs3/ec3d3d217582ac276450d89e342476c7/assets/417f3f055a8db35e7d50cdde8135d56b_,4785803.mp4,4785804.mp4,4785802.mp4,4785800.mp4,4785801.mp4,.urlset/master.m3u8"
subtitle_url = "https://v.vrv.co/evs3/ec3d3d217582ac276450d89e342476c7/assets/417f3f055a8db35e7d50cdde8135d56b_316481.txt?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly92LnZydi5jby9ldnMzL2VjM2QzZDIxNzU4MmFjMjc2NDUwZDg5ZTM0MjQ3NmM3L2Fzc2V0cy80MTdmM2YwNTVhOGRiMzVlN2Q1MGNkZGU4MTM1ZDU2Yl8zMTY0ODEudHh0IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjc3MTAzMjU0fX19XX0_&Signature=kfYdFd2cc6Y1scD59ftHV25GWdlkAukT64CIlmnloZEEKEDUuwq9d5AxzSuqJEdhq9iXvUI5G6340PzCQ6XYGYFMUF-INB8pkl5zTl3dHDn-oO3Lzgf6EaywWHxpqENKaY8DNggThhYRdNkXvqhPEVDo~fJMKRrqOqdCLfHcjVhcwwf-YuoEEGFqZR0PT5SK51T-9hQrlGnnwhLdg-2Jmg-QHqUPN0PJUJUg8DaDGnPDSpKpOGoLsCZ80ii2TUJH25siefkp9zpDVR5B-wqUwnc4z6L8zQEx2ka2-iSof1KljOodY7BTtJOckx~ehjCUxpM5yLlcADOOTDcDIT~7lQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA"


def callback(*args):
    print("\033[94mI AM HERE'\033[0m'")
    print(*args)

from pychromecast.controllers.receiver import CastStatusListener
class MyCastStatusListener(CastStatusListener):
    """Cast status listener"""

    def __init__(self, name, cast):
        self.name = name
        self.cast = cast

    def new_cast_status(self, status):
        print("[", time.ctime(), " - ", self.name, "] status chromecast change:")
        print(status)

from pychromecast.controllers.media import MediaStatusListener
class MyMediaStatusListener(MediaStatusListener):
    """Status media listener"""

    def __init__(self, name, cast):
        self.name = name
        self.cast = cast

    def new_media_status(self, status):
        print("[", time.ctime(), " - ", self.name, "] status media change:")
        print(status)

    def load_media_failed(self, item, error_code):
        print(
            "\033[91m[",
            time.ctime(),
            " - ",
            self.name,
            "] load media filed for item: ",
            item,
            " with code: ",
            error_code,
            "\033[0m",
        )

# logging.basicConfig(level=logging.DEBUG)
print("starting chromecast section\n")
cc = pychromecast.get_chromecasts()
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
print("Discovery Complete\n")
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Mesch Cast"])
cast = chromecasts[0]
cast.wait()
listenerCast = MyCastStatusListener(cast.name, cast)
cast.register_status_listener(listenerCast)
print("Cast connected\n")
mc = cast.media_controller
MyMediaStatusListener = MyMediaStatusListener(cast.name, cast)
mc.register_status_listener(MyMediaStatusListener)
mc.play_media(video_url, 'application/x-mpegurl', subtitles=subtitle_url, callback_function=callback)
mc.block_until_active()
print("cast active\n")
print(mc.status)
print('done\n')

# print("starting catt section")
# # devices = discover()
# print("done discovering")
# cast = CattDevice(name="Mesch Cast")
# cast.play_url(video_url, subtitle_url=subtitle_url, resolve=False)
# # https://developers.google.com/cast/docs/web_receiver/error_codes
# print('done with catt')


# a = "https://monkey-d-luffy.site/v1/files?resolution=default&id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbmltZV9pZCI6Ik1Ua3pORGN3IiwidGltZXN0YW1wIjoxNjc0OTUwMjI2NDUzLCJpcCI6IjczLjE0My4xNzMuNzYiLCJpYXQiOjE2NzQ5NTAyMjZ9.8lpYibsRRbdbKjQwqdpcwEp-bNBB69dBtjHvcnlXQxU"
# cast = CattDevice(name="Mesch Cast")
# cast.play_url(a, resolve=True, block=True)


# from yt_dlp import YoutubeDL
# ydl_opts = {"username": "xeno43", "password": "bubbles"}
# URLS = ['https://www.crunchyroll.com/watch/GK9U313E5/dream']
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download(URLS)