from catt.api import CattDevice, discover
import pychromecast
import streamlink

cc = pychromecast.get_chromecasts()
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Mesch Cast"])
cast = chromecasts[0]
cast.wait()
mc = cast.media_controller
mc.play_media('https://pl.crunchyroll.com/evs3/0ccd0f2bb8232df70a3dfc3221d5782e/assets/9c1eidhyearcq8k_,1890561.mp4,1890555.mp4,1890549.mp4,.urlset/master.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly9wbC5jcnVuY2h5cm9sbC5jb20vZXZzMy8wY2NkMGYyYmI4MjMyZGY3MGEzZGZjMzIyMWQ1NzgyZS9hc3NldHMvOWMxZWlkaHllYXJjcThrXywxODkwNTYxLm1wNCwxODkwNTU1Lm1wNCwxODkwNTQ5Lm1wNCwudXJsc2V0L21hc3Rlci5tM3U4IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjc1NDM2ODA1fX19XX0_&Signature=JDJYRP2uDuI6drbv8F5pCFRg1QbDdufSiMEXweeKx31AWcLNiiQ0wmDwqhNwwPWEHTTM4i4y3z~IjY8IE4fez30cCdmwDFUpQpGOamnrjF1KOAfqw83etnr-m~V-PQhddeWfJJTbrsj5dYACpMzx0QvqvjeuzI2nnchjYftz5ubSxf~bkwyd-yhZL55ByHnvJRjyWfCb0js39ZgkS-DKkINcaxinBZ51FTOigcDS9GmRegC73k0VLV9cJgQjTBFzPjOd0ii~5WC2teRyC-N3DHLmrXH1REujOPqtAkRVVI~tD6i31ASZWf-mBU9i7XX4k7YpeECoGu2BporGYLGXMg__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA', 'application/x-mpegurl')
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