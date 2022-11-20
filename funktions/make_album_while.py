
def make_akbum(album, autor, title=None):
    album_ = {'album': album, 'autor': autor}
    if title:
        album_['song'] = title
    return album_


while True:
    print('\nPlease tell your autor and album ')
    print("Please enter 'q' at any time to quit")

    a_album = input('Альбом ')
    if a_album == 'q':
        break

    a_autor = input('Виконавець ')
    if a_autor == 'q':
        break
    title_num = input('Скільки пісень ')
    if title_num == 'q':
        break


    formated_album = make_akbum(a_album, a_autor, title_num)
    print(formated_album)
