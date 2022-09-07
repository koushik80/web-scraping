from bs4 import BeautifulSoup
import re



with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#result = doc.find("option")
#print (result)

#tag = doc.find("option")
#tag['selected'] = 'false'
#tag['color'] = 'blue'
#print(tag.attrs)
#print(tag)

#tags = doc.find_all(["p", "div", "li"])
#print(tags)

#tags = doc.find_all(["option"], text="Undergraduate", value = "undergraduate")
#print(tags)

tags = doc.find_all(class_="btn-item")
print(tags)