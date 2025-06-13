from requests import get
import json

def request_content(url):
    """
    Get the data from requested url
    :param url: your requested url
    :return: content of the url
    """
    res = get(url)
    if res.status_code == 200:
        content = json.loads(res.content)
    else:
        content = ''
    return content

ip_api = 'https://api.ipify.org/?format=json'
ip_content = request_content(ip_api)
ip = ip_content.get('ip')
ip_details = f'http://ip-api.com/json/{ip}'
ip_details_content = request_content(ip_details)
country = ip_details_content.get('country')
location = ip_details_content.get('regionName')

print(f'your IP address is {ip}.\n\t'
      f'Your Country name is {country}.\n\t\t\t'
      f'Your location is {location}.')
