import phonenumbers
from phonenumbers import timezone
from termcolor import colored
import os
from phonenumbers import geocoder
import time
from phonenumbers import carrier
from tqdm import tqdm

os.system('clear')
os.system('figlet phone number')
print(colored('================================','cyan'))
# Parsing String to Phone number
a=str(input(colored('enter number: ','green')))
for i in tqdm(range(100)):
    time.sleep(0.01)

print(colored('''=======================
[      TIME ZONE      ]
======================= ''','green'))
phoneNumber = phonenumbers.parse(a)
# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)
time.sleep(1)

# It print the timezone of a phonenumber
print(colored(timeZone,'yellow'))
print(colored('''=======================
[      NETWORK        ]
======================= ''','green'))
ro_number = phonenumbers.parse(a, "RO")
time.sleep(1)

print(colored(carrier.name_for_number(ro_number, "en"),'yellow'))
print(colored('''=======================
[      GEOLOCATION    ]
======================= ''','green'))
ch_number = phonenumbers.parse(a, "CH")
time.sleep(1)
print(colored(geocoder.description_for_number(ch_number, "de"),'yellow'))
