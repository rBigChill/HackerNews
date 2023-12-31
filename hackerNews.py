import subprocess
import sys

try:
    import requests
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
finally:
    import requests

class Article:
    def __init__(self):
        self.title = ''
        self.url = ''

class HackerNews:
    def __init__(self):
        self.API_BASE = "https://hacker-news.firebaseio.com/v0"
        self.TOP_STORIES = f"{self.API_BASE}/topstories.json"
        self.ARTICLES = f"{self.API_BASE}/item/"
        self.frontPage = [] 

    def _makeRequest(self):
        r = requests.get(self.TOP_STORIES)
        self.submission_ids = r.json()

    def _getArticles(self):
        self._makeRequest()

        for submission_id in self.submission_ids[:10]:
            r = requests.get(f"{self.ARTICLES}{submission_id}.json")
            response_dict = r.json()

            r = Article()

            try:
                r.title = response_dict["title"]
                r.url = response_dict["url"]
                self.frontPage.append(r)
            except KeyError:
                continue

    def GetNews(self):
        self._getArticles()
        
        count = 1
        print()
        for i in self.frontPage:
            article = f"{count}) {i.title}\n\t{i.url:0}\n"
            print(article)
            count += 1
        print()

if __name__ == "__main__":
    HN = HackerNews()
    HN.GetNews()
