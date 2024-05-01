import requests, json, hashlib
from bs4 import BeautifulSoup as BS
from announcement import Announcement
r = requests.get("https://www.ttsh.tp.edu.tw/category/news/news_01/")
soup = BS(r.text,"html.parser")
announcements = soup.find_all("a", class_ = "news_title", limit=5)
hash_values = []
for ann_link in announcements:
    # print(ann_link["href"])
    ann = Announcement(ann_link["href"])
    hash_values.append(ann.hash_value)
    # print(ann.content)
    print("公告名稱: " + ann.title)
    print()
    for content in ann.content:
        print(content, end = '')
    print()
    print(f"檔案連結: {len(ann.attachment)}")
    for attachment in ann.attachment:
        print(f"附件名稱: {attachment[0]}\n附件連結: {attachment[1]}")
    print("\n\n")
with open("hash-values.json", "w") as f:
    json.dump(hash_values, f)