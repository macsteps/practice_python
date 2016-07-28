#!/usr/bin/env python
# goal: Use the BeautifulSoup and requests Python packages to print
# out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
headings = soup.find_all("h2", {"class": "story-heading"})

for heading in headings:
    if heading.find_all("a"):
        print heading.a.text.strip()
    else:
        # some headings are not in an a tag (e.g. video)
        print heading.text
