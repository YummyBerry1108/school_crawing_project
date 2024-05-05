import requests, time, json
from bs4 import BeautifulSoup as BS
from announcement import Announcement
anns_link = "https://www.ttsh.tp.edu.tw/category/news/news_01/"
while True:
    old_hash_values = {}
    with open("hash-values.json", "r") as f:
        old_hash_values = set(json.load(f))
    new_hash_values : set = set()
    r = requests.get(anns_link)
    soup = BS(r.text,"html.parser")
    announcements_tags = soup.find_all("a", class_ = "news_title", limit=5)
    hash_temp = []
    for ann_tag in announcements_tags:
        ann = Announcement(ann_tag["href"])
        new_hash_values.add(ann.hash_value)

    print(old_hash_values)
    print(new_hash_values)
    time.sleep(5)
    