import requests

url = "https://fake-json-api.mock.beeceptor.com/users"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("Ошибка:", response.status_code)
#Поставьте 12 прошу