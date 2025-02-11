class Album:
    def __init__(self, artist, album, snumber, year, download):
        self.artist = artist
        self.album = album
        self.snumber = snumber
        self.year = year
        self.download = download


def read():

    with open("Data.txt", "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    temp_table = lines
    return temp_table


def write(file_content):
    albums = []

    for i in range(0, len(file_content)+1, 6):
        artist = file_content[i].strip()
        album = file_content[i+1].strip()
        numbers = file_content[i+2].strip()
        year = file_content[i+3].strip()
        download = file_content[i+4].strip()
        albums.append(Album(artist, album, numbers, year, download))
    for i in range(len(file_content)//6):
        print(
            f'{albums[i].artist} \n {albums[i].album} \n {albums[i].snumber} \n {albums[i].year} \n {albums[i].download} \n')
        
    for i in range(len(file_content)-1):
        for j in range((len(file_content))-i-1):
            if albums[j].download > albums[j+1].download:
                albums[j], albums[j+1] = albums[j+1], albums[j]

    for i in range((len(file_content)+1)//6):
        print(
            f'{albums[i].artist} \n {albums[i].album} \n {albums[i].snumber} \n {albums[i].year} \n {albums[i].download} \n')


write(read())
