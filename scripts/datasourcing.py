import requests
arrestdata_api = 'https://data.cityofnewyork.us/resource/uip8-fykc.json'
response = requests.get(arrestdata_api)
data = response.json()
print(data)
