from yt_dlp import YoutubeDL
import creds

class CrunchyRollExtractor:
    def __init__(self, url):
        ydl_opts = {"username": creds.CRUNCHY_USER,
                    "password": creds.CRUNCHY_PASS,
                    "simulate": 1,
                    "cachedir": False,
                    "cookiesfrombrowser": ("firefox",)}

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url)

        self.video_sources = info["formats"]
        self.subtitle_sources = info["subtitles"]

    def videoSource(self):
        return self.video_sources[-1]["manifest_url"]

    def subtitleSource(self, lang="en-US"):
        if lang not in self.subtitle_sources:
            print(f"Cannot find subtitles for language: {lang}.")
        return self.subtitle_sources[lang][0]['url']