# -*- coding: utf-8 -*- 
import requests 
from bs4 import BeautifulSoup 

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

soup.title

soup.a # 第一个a标签
soup.name 
soup.a.parent.name
soup.a.parent.parent.name  
soup.a.attrs
soup.a.attrs['class']
type(soup.a)
type(soup.a.attrs)
soup.string  # 标签内非属性的字符串内容,不包括子标签

# 以注释的类型来判断 标签内非属性的字符串内容 是否是注释

# 标签树的下行遍历
soup.body.contents
for el in soup.p.children:
    # print(el)
    pass
for el in soup.p.descendants:
    # print(el)
    pass

# 标签树的上行遍历
soup.body.parent
for parent in soup.a.parents:
    # if parent is None:
    #     print(parent)
    # else:
    #     print(parent.name)
    pass

# 标签树的平行遍历   在同一个父标签下
soup.p.next_sibling
soup.p.previous_sibling
for el in soup.p.next_siblings:
    pass
for el in soup.p.previous_sibling:
    pass

# 让html代码更加友好的显示
print(soup.prettify())    
print(soup.a.prettify())




for link in soup.find_all('a'):
    print(link.get("href"))


