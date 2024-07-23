import requests
from bs4 import BeautifulSoup

# body > section.highlights-portal
url = 'https://example.me'

def realizar_raspagem():
    acess = requests.get(url)
    html = acess.content
    html_parsed = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    my_news = html_parsed.select_one('body') # Redefina o campo da raspagem

    if my_news is not None:
        return my_news
