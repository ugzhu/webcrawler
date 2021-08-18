from bs4 import BeautifulSoup

def getNextUrl(result):
    next_url = -1
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    pages = soup.find_all('a', class_='n', href=True)
    count = 0
    for page in pages:
        count = count + 1
        if count == 2:
            next_url = page['href']
    print(next_url)
    return next_url

