import requests
import bs4

## send a get request to website we want to scrap
request = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(request.text, 'lxml')

print(soup.select('.vector-toc-text'))
first_item = soup.select('.vector-toc-text')[0]
for item in soup.select('.vector-toc-text'):
    print(item.getText())
