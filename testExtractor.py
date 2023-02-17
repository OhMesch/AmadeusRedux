import subprocess

from Extractors import CrunchyRollExtractor
from subprocess import Popen, PIPE, STDOUT

cre = CrunchyRollExtractor('https://www.crunchyroll.com/watch/GK9U313E5/dream')
video_url = cre.videoSource()
subtitle_url = cre.subtitleSource()

# print(video_url)
# print(subtitle_url)

# mpv 'https://pl.crunchyroll.com/evs3/0ccd0f2bb8232df70a3dfc3221d5782e/assets/9c1eidhyearcq8k_,1890561.mp4,1890555.mp4,1890549.mp4,.urlset/master.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly9wbC5jcnVuY2h5cm9sbC5jb20vZXZzMy8wY2NkMGYyYmI4MjMyZGY3MGEzZGZjMzIyMWQ1NzgyZS9hc3NldHMvOWMxZWlkaHllYXJjcThrXywxODkwNTYxLm1wNCwxODkwNTU1Lm1wNCwxODkwNTQ5Lm1wNCwudXJsc2V0L21hc3Rlci5tM3U4IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjc1NDM2ODA1fX19XX0_&Signature=JDJYRP2uDuI6drbv8F5pCFRg1QbDdufSiMEXweeKx31AWcLNiiQ0wmDwqhNwwPWEHTTM4i4y3z~IjY8IE4fez30cCdmwDFUpQpGOamnrjF1KOAfqw83etnr-m~V-PQhddeWfJJTbrsj5dYACpMzx0QvqvjeuzI2nnchjYftz5ubSxf~bkwyd-yhZL55ByHnvJRjyWfCb0js39ZgkS-DKkINcaxinBZ51FTOigcDS9GmRegC73k0VLV9cJgQjTBFzPjOd0ii~5WC2teRyC-N3DHLmrXH1REujOPqtAkRVVI~tD6i31ASZWf-mBU9i7XX4k7YpeECoGu2BporGYLGXMg__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA' --sub-file='https://v.vrv.co/evs3/0ccd0f2bb8232df70a3dfc3221d5782e/assets/9c1eidhyearcq8k_224902.txt?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly92LnZydi5jby9ldnMzLzBjY2QwZjJiYjgyMzJkZjcwYTNkZmMzMjIxZDU3ODJlL2Fzc2V0cy85YzFlaWRoeWVhcmNxOGtfMjI0OTAyLnR4dCIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY3NTQzNjgwNX19fV19&Signature=PPbLNXpkTET7~AOS4oGh1kj6PSQv4OWKMa959qkXXCBD-24YV9E7nxFPXnJzyUtvOzMF81~xCatM20sH4hfLPzaOHKZp48B7MnUUT9G~8WUCYVqT73qtNWJv7Zy5BbpEF6QODI0n7zYTUEv8KEEWdf0coXP3ukS2KOc0JraxdveN2HI2Mt5jy64HQ4Zw1XJREuKZS~Dzdh2GZN0PbBX2Jqh5c1Mg6vf~NYsdeoBhVUPejzMoBTrnV5Y45DF5t~-RPFcT0SoMdeVy3S1KR9AdYUo~aF2Zy2qJuDxNw3ZYxd0p-23MaQrCL9JEZrApuDmFnGnpMu~kNbd-SY6H2ALSyQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA' --o=- --of=hls | castnow --address 192.168.86.27 - --tomp4
 # --o=- --of=hls | castnow --address 192.168.86.27 - --tomp4
# mpv = subprocess.run(['/usr/bin/mpv', video_url, '--sub-file', subtitle_url], stdout=subprocess.PIPE)
mpv = subprocess.run(['/usr/bin/mpv', video_url, '--sub-file', subtitle_url, '--o', '-', '-of', 'hls'], stdout=subprocess.PIPE)
castnow = subprocess.run(['castnow', '--address', '192.168.86.27', '-', '--tomp4'], stdin=subprocess.PIPE)
print("complete")