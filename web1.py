#웹글로링 예제
from bs4 import BeautifulSoup

page = open('Chap09_test.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())
# print(soup.find_all('p'))
# print(soup.find('p'))
# print(soup.find_all('p', class_='inner-text'))
# print(soup.find_all('p', attrs={'class':'inner-text'}))

for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n','')
    print(title)


