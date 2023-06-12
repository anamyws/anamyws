import requests

op = '37.238.121.17'

ip = requests.get(f'http://ip-api.com/json/{op}').json()

a =  country = ip['country']

print('دوله : '+country)

regionName = ip['regionName']

print(' محافضه : '+regionName)

#سورس استخراج موقع الضحيه من ip

telegram : @anamyws
