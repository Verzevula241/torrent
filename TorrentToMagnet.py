import base64
import hashlib
import sys

import bencodepy
from torrentool.api import Torrent

def make_magnet_from_file(file) :
    metadata = bencodepy.decode_from_file(file)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    return 'magnet:?'\
             + 'xt=urn:btih:' + b32hash\
             + '&dn=' + metadata[b'info'][b'name'].decode()\
             + '&tr=' + metadata[b'announce'].decode()\
             + '&xl=' + str(metadata[b'info'])


print(make_magnet_from_file('Рик и Морти Rick and Morty Сезон 4 Серии 5 из 10 (Пит Мишелс, Уэсли Арчер, Брайан Ньютон) [2019, США, Мультфильм, приключе [rutracker-5804994].torrent'))