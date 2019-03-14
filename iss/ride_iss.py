#!usr/bin/env python3

import urllib.request
import json

majortom = "http://api.open-notify.org/astros.json"

grndcntrl = urllib.request.urlopen(majortom)

helmet = grndcntrl.read()

helmetson = json.loads(helmet.decode('utf-8'))

print("\n\n Converted data")
people = helmetson['people']
print(people)