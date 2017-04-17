# -*- coding: utf-8 -*- 
import requests 
from bs4 import BeautifulSoup 
import re

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")


soup.find_all("a")
soup.find_all(["a", "b"])

soup.find_all('p', 'course')

soup.find_all(id='link')

soup.find_all(id=re.compile('link'))

soup.find_all('a', recursive=False)

soup.find_all(string="Basic Python")
soup.find_all(string=re.compile("Python"))