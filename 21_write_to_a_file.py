#!/usr/bin/env python
# goal: write story headings of web page to file.

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
headings = soup.find_all("h2", {"class": "story-heading"})

with open('decode_web_page.txt', 'w') as open_file:
    for heading in headings:
        if heading.find_all("a"):
            print heading.a.text.strip()
            open_file.write(heading.a.text.strip().encode("UTF-8"))
            open_file.write("\n")
        else:
            # some headings are not in an a tag (e.g. video)
            print heading.text
            open_file.write(heading.text.encode("UTF-8"))
            open_file.write("\n")
