# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}


for n in range(0,10):
        #오늘의유머 주소 
        url ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(url)
        req = urllib.request.Request(url, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        # <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=477648&amp;s_no=477648&amp;page=1" target="_top">약국 타짜</a><span class="list_memo_count_span"> [20]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>
	
        for item in list:
            try:
                title = item.find('a')
                title = item.text.strip()
                # print(title)
                if re.search('한국', title):
                    print(title)
            except:
                pass


