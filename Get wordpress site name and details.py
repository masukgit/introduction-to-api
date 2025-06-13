def increment(salary, increase = .10):
    total = salary + salary * increase
    return total
print(increment(1000, increase= .25))
print(increment(2000))

from requests import get
import json

url = 'https://math.berkeley.edu/wp/wp-json'
res = get(url)
if res.status_code == 200:
    content = json.loads(res.content)
    name = content.get('name')
    description = content.get('description')
    timezone_string = content.get('timezone_string')
    print(name, description, timezone_string, sep='\n')

else:
    print('Fail')

from requests import get
import json
url = 'https://blog.mozilla.org/theden/wp-json'
res = get(url)
if res.status_code == 200:
    content = json.loads(res.content)
    name = content.get('name')
    description = content.get('description')
    home = content.get('home')
    gmt_offset = content.get('gmt_offset')
    print(name, description, home, gmt_offset, sep='\n')
else:
    print('Feltus')
    