from requests import get
import json
url = 'https://restcountries.com/v3.1/all'
res = get(url)
content = json.loads(res.content)
print('country_name \t\t\t capital')
print('*'*40)
for country in content:
    country_name = country.get('name').get('official')
    capital = country.get('capital')
    print(f'{country_name} \t\t\t {capital}')
