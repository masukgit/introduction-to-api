import requests
print(requests.__doc__)

response = requests.get('https://www.python.org')
print(response.status_code)

print(b'programming or an experienced' in response.content)
print(response.content)