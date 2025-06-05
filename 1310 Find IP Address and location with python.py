from requests import get
import json

ip_api = 'https://api.ipify.org/?format=json'
res = get(ip_api)
if res.status_code == 200:
    content = json.loads(res.content)
    ip = content.get('ip')
    print(content)
else:
    print('Connection Error')


ip_details = f'http://ip-api.com/json/{ip}'
res = get(ip_details)
if res.status_code == 200:
    print(res.content)