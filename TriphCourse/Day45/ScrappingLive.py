import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
web_page = response.text
# print(web_page)

soup = BeautifulSoup(web_page, "html.parser")
print(soup.title.string)

tit = soup.find(name='span', class_="score")
print(tit.getText())

tits = soup.findAll(name='span', class_="score")
final = []
for ti in tits:
    inter = ti.getText().split()[0]
    final.append(inter)


print(max(final))

print('Hello')

numbers = ['1','2','3','4','5']
append = []
for no in numbers:
    append.append(no)

print(max(append))



