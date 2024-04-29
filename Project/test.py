import requests
from bs4 import BeautifulSoup as BS
from announcement import Announcement
r = requests.get("https://www.ttsh.tp.edu.tw/category/news/news_01/")
soup = BS(r.text,"html.parser")
announcements = soup.find_all("a", class_ = "news_title")
ann = Announcement("https://www.ttsh.tp.edu.tw/news/%e5%88%86%e7%a7%91%e6%b8%ac%e9%a9%97%e8%a1%9d%e5%88%ba%e3%80%90%e9%ab%98%e4%b8%894-29%e4%b8%805-31%e4%ba%94%e9%96%8b%e6%94%be%e6%95%99%e5%ae%a4%e5%a4%9c%e8%87%aa%e7%bf%92%e3%80%91/")
print(ann.content)
for content in ann.content:
    print(content, end = '')
# for ann in announcements:
#     strings = []
#     for string in ann.strings:
#         strings.append(string)
#         # print(repr(string))
#     print(strings[-1])
#     print()
