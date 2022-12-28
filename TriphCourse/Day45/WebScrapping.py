from bs4 import BeautifulSoup
import lxml

with open('web.html') as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

print(soup.title.string)
# print(soup.prettify())
print(soup.h1)
all = soup.findAll(name='title')

for al in all:
    print(al.getText())