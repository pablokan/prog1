import xml.etree.ElementTree as ET
from collections import Counter
import requests
resp = requests.get("https://pybit.es/feeds/all.rss.xml")
tree = ET.fromstring(resp.content)
categories = (e.text for e in tree.findall("./channel/item/category"))
cc = Counter(categories).most_common(5)
print(cc)

