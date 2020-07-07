import asyncio
import time

import transmissionrpc

c = transmissionrpc.Client(address='kovardici.keenetic.link', port=8090, user='admin', password='Anna2074')
# c = transmissionrpc.Client(address='192.168.1.1', port=8090, user='admin', password='Anna2074')
torrent = c.get_torrents(None, None, 60)

status = ''
for tor in torrent:
    torry = tor._fields.get('name').value
    print(torry)
    status = status + str(tor._get_name_string() + '  ' + tor.status + '   ' + str(round(tor.progress)) + ' %' + '\n')



