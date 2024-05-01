import requests, time
from bs4 import BeautifulSoup as BS
from announcement import Announcement
ann_link = "https://www.ttsh.tp.edu.tw/category/news/news_01/"
while True:
    r = requests.get(ann_link)
    soup = BS(r.text,"html.parser")
    announcements_tag = soup.find_all("a", class_ = "news_title", limit=20)
    