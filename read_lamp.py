#!/usr/bin/python
#
# read lamp status from Beebotte

# start bridge connection 
import sys
sys.path.insert(0, '/usr/lib/python2.7/bridge')
from time import sleep
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

# start connection to beebotte
from beebotte import *
bbt = BBT('PUT_API_KEY_HERE',
          'PUT_SECRET_KEY_HERE',
          hostname = 'api.beebotte.com')

def write_status (status):
    if status:
        value.put('lamp', 'on')
    else:
        value.put('lamp', 'off')


last_status = False
write_status(False)

while True:
    status = bbt.read('PUT_CHANNEL_HERE', 'PUT_RESOURCE_HERE', 1)[0]['data']
    if status != last_status:
        write_status(status)
        last_status = status
        print(status)
    sleep(0.1)
