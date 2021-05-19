import requests

URL = 'http://0.0.0.0:2224/fast'
<<<<<<< HEAD
response = requests.get(URL)
print(response.text)
=======
for i in range(201):
    response = requests.get(URL)
    print(f'#{i} fast request: {response.text}')
>>>>>>> d419e641e2e37dd80a76d2fe924a785794a9d0d3
