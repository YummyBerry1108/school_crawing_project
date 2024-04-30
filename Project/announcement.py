import requests
from bs4 import BeautifulSoup as BS 

class Announcement():
    def __init__(self, link : str) -> None:
        r : requests.Response = requests.get(link)
        soup : BS = BS(r.text, "html.parser")
        news = soup.find("table", class_ = "single_news")
        # print(news)
        self.title : str = news.find("tr", class_ = "news_title").td.string
        self.date : str = news.find("tr", class_ = "news_date").td.string
        self.unit : str = news.find("tr", class_ = "news_unit").td.string
        self.type : str = news.find("tr", class_ = "news_cat").td.a.string
        self.content : list[str] = []
        contents = news.find("tr", class_ = "news_content").td.div
        for content in contents.strings:
            self.content.append(content.string)
        self.attachment : list[str] = []