import requests
import json


url = 'https://restcountries.com/v3.1/all'
res = requests.get(url)
content = json.loads(res.content)

i = 0
while i <= 9:
    single_country = content[i]
    country_name = single_country.get('name').get('common')
    country_currencies = single_country.get('currencies')
    country_capital = single_country.get('capital')[0]
    country_region = single_country.get('region')
    country_language = single_country.get('languages')
    text = f'The country {country_name} is a great in the world. The currency of this country is {country_currencies}. The capital is {country_capital}. It is in {country_region} region. It\'s language is {country_language}.'
    print(text)
    i += 1
