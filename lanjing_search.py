from bs4 import BeautifulSoup
import requests


def Searchlanjing(sheet):
    url = 'https://bk.tencent.com/info/#news'
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    all_news = soup.find_all('li', class_='clearfix', limit=40)
    i = 1

    for news in all_news:
        title = news.find('div', class_='content fr').h3.text.replace(' ', '')
        sheet.write(i, 2, title)
        date = news.find('div', class_='time fl').h3.text
        sheet.write(i, 1, date)
        year = news.find('div', class_='time fl').p.text
        sheet.write(i, 0, year)
        url = news.find('a', target='_blank', href=True)['href']
        sheet.write(i, 3, url)
        i = i + 1
    print("蓝鲸搜索完成")
