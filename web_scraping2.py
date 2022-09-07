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

#tags = doc.find_all(class_="btn-item")
#print(tags)



#  **********   Regex:  **********

#tags = doc.find_all(text =re.compile("\$.*"))
#for tag in tags:
    #print(tag.strip())

tags = doc.find_all("input", type = "text")
for tag in tags:
    tag['placeholder'] = "I'm loving it!"

with open("changed.html", 'w') as file:
    file.write(str(doc))




