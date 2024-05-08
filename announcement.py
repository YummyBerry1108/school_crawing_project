import requests, hashlib
from bs4 import BeautifulSoup as BS 
class Announcement():
    def __init__(self, link : str) -> None:
        r : requests.Response = requests.get(link)
        soup : BS = BS(r.text, "html.parser")
        self.id = 0
        self.link : str = link
        self.news = soup.find("table", class_ = "single_news")
        self.hash_value = self.__get_hash()

        self.title : str = self.news.find("tr", class_ = "news_title").td.string
        self.date : str = self.news.find("tr", class_ = "news_date").td.string
        self.unit : str = self.news.find("tr", class_ = "news_unit").td.string
        self.type : str = self.news.find("tr", class_ = "news_cat").td.a.string
        self.content : list[str] = self.__get_content()
        self.attachment : list[tuple[str, str]] = self.__get_attachment() # list pair -> (name, link)

    def __get_hash(self) -> int:
        data = hashlib.md5()
        data.update(self.link.encode('utf-8'))
        # print(type(data.digest()))
        return int.from_bytes(data.digest(), byteorder='big')
    def __get_content(self) -> str:
        contents = self.news.find("tr", class_ = "news_content").td.div
        content_temp = []
        for content in contents.strings:
            content_temp.append(content.string)
        return "".join(content_temp)
    def __get_attachment(self) -> list[str]:
        attach_tags = self.news.find_all("ul", class_ = "modal_list")
        attach_pairs = []
        for attach_tag in attach_tags:
            name = attach_tag.find("span", class_ = "modal_name").string
            link = attach_tag.find("span", class_ = "modal_download").a.get("href")
            attach_pairs.append((name, link))
        return attach_pairs
    def date_to_day(self) -> int:
        str_list = self.date.split()
        return int(str_list[0])*366 + int(str_list[2])*31 + int(str_list[4])

    