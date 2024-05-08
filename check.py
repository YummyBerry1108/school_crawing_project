import requests, time, json
from bs4 import BeautifulSoup as BS
from announcement import Announcement
anns_link = "https://www.ttsh.tp.edu.tw/category/news/news_01/"
while True:
    old_hash_values = set()
    hash_to_ann = {}
    with open("hash-values.json", "r") as f:
        old_hash_values = set(json.load(f))
    new_hash_values : set = set()
    r = requests.get(anns_link)
    soup = BS(r.text,"html.parser")
    announcements_tags = soup.find_all("a", class_ = "news_title", limit=20)
    hash_temp = []
    for ann_tag in announcements_tags:
        ann = Announcement(ann_tag["href"])
        hash_to_ann[ann.hash_value] = ann
        new_hash_values.add(ann.hash_value)

    new_set = new_hash_values - old_hash_values
    new_ann = []
    for hash_value in new_set:
        new_ann.append(hash_to_ann[hash_value])

    new_ann = sorted(new_ann, key=lambda ann : ann.date_to_day())
    for ann in new_ann:
        print(ann.date)
    with open("hash-values.json", "w") as f:
        json.dump(list(new_hash_values), f)
    time.sleep(5)
    