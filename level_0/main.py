#!/usr/bin/python3
# cheat vote is fun
import requests
with requests.Session() as x:
    url = "http://158.69.76.135/level0.php"
    x.get(url)
print("please wait ..")
for req in range(1024):
    requests.post(url, data={
        'id': 1129,
        'holdthedoor': "Submit"
    })
print("done")
