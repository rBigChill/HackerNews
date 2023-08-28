import subprocess

try:
    import requests
except:
    subprocess.check_call([sys.execuable, "-m", "pip", "istall", "requests"])
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

        i = 0
        for submission_id in self.submission_ids[:10]:
            r = requests.get(f"{self.ARTICLES}{submission_id}.json")
            response_dict = r.json()

            r = Article()

            try:
                r.title = response_dict["title"]
                r.url = response_dict["url"]
                self.frontPage.append(r)
                i += 1
            except KeyError:
                i += 1

    def GetNews(self):
        self._getArticles()

        print()
        for i in self.frontPage:
            article = f"{i.title}\n\t{i.url}\n"
            print(article)
        print()

if __name__ == "__main__":
    HN = HackerNews()
    HN.GetNews()
