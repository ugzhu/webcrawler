from bs4 import BeautifulSoup
import requests
import xlwt


def Searchbaiduads(sheet, keyword):
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    keyword = keyword
    baidu_url = 'https://www.baidu.com/s?wd='
    url = baidu_url+keyword
    result = requests.get(url, headers={'User-Agent': user_agent})
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('div', {'data-cmatchid': '225'})

    count = 0
    i = 1
    style_head = xlwt.easyxf('alignment: wrap True')
    for card in cards:
        count = count + 1
        content = card.find_all('a', target='_blank', href=True)
        if count == 0 or count == 1 or count == 2 or count == 3 or count == 4 or count == 5 or count == 6 or count == 7:
            s_count = 0
            for c in content:
                s_count = s_count + 1
                if s_count == 1:
                    url = c['href']
                    sheet.write(i, 1, url, style_head)
                if s_count == 0 or s_count == 1 or s_count == 3 or s_count == 4 or s_count == 5 or s_count == 6:
                    text = c.text
                    sheet.write(i, 0, text, style_head)
                    i = i + 1
        i = i + 5
    print("百度SEM搜索完成")
    return keyword
