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
#print(trs[0].next_siblings)
#print(list(trs[0].parent))
#print(trs[0].parent)
#print(trs[0].parent.name)
#print(list(trs[0].descendants))
#print(list(trs[0].children))
#print(list(trs[0].contents))



# **** Getting Crypto Prices ****

prices = {}

#for tr in trs:
    #for td in tr.contents[2:4]:
        #print(td)
        #print()

#for tr in trs[:10]:
    #name, price = tr.contents[2:4]
    #print(name.p)
    #print(name.p.string)
    #print()

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    #print(price.a.string)

    prices[fixed_name] = fixed_price
print(prices)
