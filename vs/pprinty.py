import json
import pprint
from urllib.request import urlopen

#url = 'https://pypi.org/pypi/flask/json'
url = 'https://www.clarin.com'

with urlopen(url) as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)

