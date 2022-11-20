
def make_album(autor, album, song=None):
    album = {'autor': autor, 'album': album}
    if song:
        album['song'] = song
    return album


title = make_album('enya', 'watermark', 13)
print(title)