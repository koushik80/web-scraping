from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# *** Table ***

tbody = doc.tbody
#print(tbody)

trs = tbody.contents
#print(trs)
#print(trs[0].next_sibling)
#print(trs[1].previous_sibling)
print(trs[0].next_siblings)