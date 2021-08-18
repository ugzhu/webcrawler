from bs4 import BeautifulSoup
import requests
from baidu_getNextUrl import getNextUrl


def configureBaiduSheet(sheet):
    sheet.write(0, 0, "标题")
    sheet.write(0, 1, "摘要")
    sheet.write(0, 2, "链接")
    sheet.col(0).width = 256 * 100
    sheet.col(1).width = 256 * 100
    sheet.col(2).width = 256 * 100


def searchBaidu(sheet, keyword, number_of_pages):
    # first page
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    keyword = keyword
    baidu_url = 'https://www.baidu.com/s?wd='
    url = baidu_url+keyword
    result = requests.get(url, headers={'User-Agent': user_agent})
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    if soup.find('title').text == "百度安全验证":
        print("尝试爬取次数过多，请稍后重试")
        return
    cards = soup.find_all('div', class_='result c-container new-pmd')
    i = 1

    for card in cards:
        title = card.find('a', target='_blank').text
        sheet.write(i, 0, title)
        url = card.find('a', target='_blank', href=True)['href']
        sheet.write(i, 2, url)
        abstract = card.find('div', class_='c-abstract').text
        sheet.write(i, 1, abstract)
        i = i + 1
    # second page
    if number_of_pages > 1:
        page2 = soup.find('a', class_='n', href=True)['href']
        url = 'https://www.baidu.com'+page2
        result = requests.get(url, headers={'User-Agent': user_agent})
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        cards = soup.find_all('div', class_='result c-container new-pmd')
        for card in cards:
            title = card.find('a', target='_blank').text
            sheet.write(i, 0, title)
            url = card.find('a', target='_blank', href=True)['href']
            sheet.write(i, 2, url)
            abstract = card.find('div', class_='c-abstract').text
            sheet.write(i, 1, abstract)
            i = i + 1
        # more pages, starting at 3
        for count in range(3, number_of_pages + 1):
            next_url = getNextUrl(result)
            if next_url == -1:
                print('尝试搜索更少的页面数量，或过一会儿再搜索')
                break
            url = 'https://www.baidu.com'+next_url
            result = requests.get(url, headers={'User-Agent': user_agent})
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            cards = soup.find_all('div', class_='result c-container new-pmd')
            for card in cards:
                title = card.find('a', target='_blank').text
                sheet.write(i, 0, title)
                url = card.find('a', target='_blank', href=True)['href']
                sheet.write(i, 2, url)
                abstract = card.find('div', class_='c-abstract').text
                sheet.write(i, 1, abstract)
                i = i + 1
    print("百度SEO搜索完成")

