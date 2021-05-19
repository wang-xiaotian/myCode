import requests

URL = 'http://0.0.0.0:2224/fast'
response = requests.get(URL)
print(response.text)
