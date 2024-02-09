import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(response.text, "lxml")

print(soup.select('img')[0])

print(soup.select('.mw-file-description'))