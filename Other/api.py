# Python Crash Course
# api.py
# Created by Mauro J. Pappaterra on 25 of September 2020.
import requests
import sys

url = "www.url.com/api/something"
username = "username"
token = "password"

# alternative with credentials
try:
    req = requests.get(url, auth=(username, token))
    data = req.json() # parse response into JSON
except:
    print("Unexpected error: ", sys.exc_info()[0]) # error handling here

# alternative without credentials
try:
    req = requests.get(url)
    data = req.json() # parse response into JSON
except:
    print("Unexpected error: ", sys.exc_info()[0]) # error handling here