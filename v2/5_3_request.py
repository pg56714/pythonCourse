# 安專套件、串接匯率 api

import requests
r = requests.get('https://api.exchangerate-api.com/v4/latest/TWD')
# print(r.json())

data = r.json()['rates']
print(data)
print(data['USD'])
print(800*(1/data['USD']))
