import requests
import bs4

## send a get request to website we want to scrap
response = requests.get("http://www.example.com")
print(type(response))
print(response.text)

## create a soup object using the bs4 module
soup = bs4.BeautifulSoup(response.text,"lxml")
print(soup)

## search for simple html elements 
print(soup.select('title'))

## this returns a list
## we can iterate through the list and extract the text we want
text_in_title_tag = soup.select('title')[0].getText()
print(text_in_title_tag)

## doing more selections
site_paragraphs = soup.select('p')
print(site_paragraphs)
parags = site_paragraphs[0].get_text()
print(parags)