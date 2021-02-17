def make_album(singer, album, number = ''):
    album_integretion = {'singer_name':singer, 'album_name':album}
    if number:
        album_integretion['number'] = number
    return album_integretion
while True:
    print("\nPlease input singer and album:")
    print("(enter 'q' at any time to quit)")

    singer_name = input("The singer is: ")
    if singer_name == 'q':
        break

    album_name = input("The album is: ")
    if album_name == 'q':
        break
    album_info = make_album(singer_name, album_name)
    print("\n" + singer_name.title() + " has writtened the " + album_name + ".")