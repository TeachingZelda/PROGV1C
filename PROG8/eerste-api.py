import requests

with open('api.key') as key_file:
    api_key = key_file.read()

uri = f'https://api.openweathermap.org/data/2.5/weather?q=Utrecht,nl&APPID={api_key}'
response = requests.get(uri)
print('Weather forecast:', response.json())

# print('Weather forecast:', response.json()['weather'][0]['description'])
