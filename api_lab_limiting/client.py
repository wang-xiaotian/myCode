import requests

URL = 'http://0.0.0.0:2224/fast'
for i in range(201):
    response = requests.get(URL)
    print(f'#{i} fast request: {response.text}')
