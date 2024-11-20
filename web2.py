from bs4 import BeautifulSoup
import urllib.request as req
import re

f = open('clien.txt', 'wt', encoding='utf-8')

for i in range(0, 10):
    url = 'https://www.clien.net/service/board/sold?&od=T31&category=0&po=' + str(i)
    print(url)
    f.write(url + '\n')

    response = req.urlopen(url)
    # 문자열을 받아서
    page = response.read().decode('utf-8')
    # 검색이 용이한 객체 생성
    soup = BeautifulSoup(page, 'html.parser')
    list = soup.find_all('a', attrs={'class':'list_subject'})

    for item in list:
        try:
            title = item.find('span', attrs={'class':'subject_fixed'})
            title = title.text.strip()
            # print(title)
            if re.search('아이폰', title):
                f.write(title + '\n')
                print(title)
        except:
            pass
f.close()

# <a class="list_subject" href="/service/board/sold/18843936?od=T31&po=0&category=0&groupCd=" data-role="cut-string">	 
# 		<span class="category fixed" title="판매">판매</span>
# 		<span class="subject_fixed" data-role="list-title-text" title="맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.">
# 			맥북에어15 M3 칩셋 8코어 CPU, 10코어 GPU, 16GB RAM, 256GB 판매합니다.
# 						</span>
# 					</a>