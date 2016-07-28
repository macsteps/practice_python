#!/usr/bin/env python
# goal: print text of article

import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
article_text = soup.find_all("section", {"class": "content-section"})

for article in article_text:
    contents = article.find_all("p")
    for content in contents:
        print content.text.strip()
