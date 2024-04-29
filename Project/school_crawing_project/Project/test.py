import requests
from bs4 import BeautifulSoup as BS
from announcement import Announcement
r = requests.get("https://www.ttsh.tp.edu.tw/category/news/news_01/")
soup = BS(r.text,"html.parser")
announcements = soup.find_all("a", class_ = "news_title", limit=5)
for ann_link in announcements:
    # print(ann_link["href"])
    ann = Announcement(ann_link["href"])
    # print(ann.content)
    print(ann.title)
    print()
    for content in ann.content:
        print(content, end = '')
    print("\n\n")

