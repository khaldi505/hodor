#!/usr/bin/python3
import requests

print("hello world!\n")
url = "http://158.69.76.135/level0.php"
id = int(input("enter your id:\n"))
yes_no = input("wanna see the request status y/n ?")
for req in range(1024):

    requests.post(url, data={
        'id': id,
        'holdthedoor': "Submit"
    })
    if yes_no == 'y':
        print("request number {} has been sent to {}".format(req, url))
    elif yes_no == 'n':
        pass
    else:
        print("please enter y or n")
print("done!")
