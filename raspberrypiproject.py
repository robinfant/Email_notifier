sudo apt-get update
sudo apt-get upgrade

sudo apt-get install sense-hat
sudo reboot

sudo nano ~/sensehat_test.py

from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Hello World")

sudo python ~/sensehat_test.py

sudo reboot

sudo apt-get remove python-pip
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo apt-get install python-pip

sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo pip install imapclient

sudo mkdir ~/emailnotifier
cd ~/emailnotifier

curl -L https://go.pimylifeup.com/v3pcgz/sensehatfileimages | sudo tar xvz

sudo nano emailnotifier.py

#!/usr/bin/python
from sense_hat import SenseHat
from imapclient import IMAPClient
import time
import sys

HOSTNAME = 'TigerteamHCHS@gmail.com'
USERNAME = 'TigerteamHCHS'
PASSWORD = 'raspberrypiproject'
MAILBOX = 'Inbox'
NEWMAIL_OFFSET = 0 
MAIL_CHECK_FREQ = 20

sense = SenseHat()
sense.load_image("hello.png")

try:
      server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
      server.login(USERNAME, PASSWORD)
except:
      connected = False
      sense.load_image("error.png")
else:
      connected = True
      sense.load_image("done.png")
      select_info = server.select_folder(MAILBOX)

try:
      while connected:
            folder_status = server.folder_status(MAILBOX, 'UNSEEN')
            newmails = int(folder_status['UNSEEN'])
            if newmails > NEWMAIL_OFFSET:
                  newmails -= NEWMAIL_OFFSET
                  sense.show_message(str(newmails))
                  if newmails == 1:
                        sense.load_image("mail.png")
                  elif newmails > 1 and newmails < 15 : 
                        sense.load_image("mailFew.png") 
                  elif newmails > 14:
                        sense.load_image("mailLot.png")
            else:
                  sense.load_image("nomail.png")
            time.sleep(MAIL_CHECK_FREQ)
except KeyboardInterrupt:
      pass
sense.clear()

sudo python emailnotifier.py
