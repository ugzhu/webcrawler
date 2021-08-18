from bs4 import BeautifulSoup
import requests


def Searchyouwei(sheet):
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    url = 'https://www.uwintech.cn/news'
    result = requests.get(url, headers={'User-Agent': user_agent})
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('div', class_='s-blog-entry s-blog-new-layout s-blog-new-layout-undefined undefined s-layout-columns s-avatar-landscape')
    i = 1

    for card in cards:
        date = card.find('span', class_='s-blog-date').text
        sheet.write(i, 0, date)
        title = card.find('div', class_='s-blog-title s-font-heading').text
        sheet.write(i, 1, title)
        url = card.find('a', target='_self', href=True)['href']
        sheet.write(i, 2, url)
        i = i + 1
    print("优维搜索完成")

