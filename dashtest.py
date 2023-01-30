from mpegdash.parser import MPEGDASHParser

mpd_path = './manifest.mpd'
mpd = MPEGDASHParser.parse(mpd_path)
print('Done')