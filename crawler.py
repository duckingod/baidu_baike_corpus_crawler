
class BaiduBaikePageGetter:
    def __init__(self):
        self.n = 0
        self.viewed = set()
        self.viewed.add(-1)
        self.id_rng = (0, 19343260)

    def url(self, n):
        return 'http://baike.baidu.com/view/' + str(n) + '.htm' 
    def is_error_page(self, soup):
        return soup.find('div', attrs={'class': 'errorBox'})!=None
    def is_ok_page(self, soup):
        returnsoup.find('div', attrs={'class': 'main-content'})!=None
    def get(self, page_id=-1):
        from urllib2 import urlopen, Request
        from bs4 import BeautifulSoup
        from random import randint
        from time import sleep
        while True:
            while page_id in self.viewed:
                page_id = randint(self.id_rng[0], self.id_rng[1])
            self.viewed.add(page_id)
            print("getting.. " + str(page_id))
            sleep(1)
            data = urlopen(self.url(page_id))
            soup = BeautifulSoup(data, "html.parser")
            if self.is_ok_page(soup):
                return (page_id, soup)
            else:
                print 'failed'

class CorpusExtractor:
    def __init__(self):
        pass
    def get_corpus(self, soup):
        res = []
        cont = soup.find('div', attrs={'class': 'main-content'}) 
        paras = cont.find_all('div', attrs={'class': 'para'}) 
        for p in paras:
            res.append(p.text)
        return " ".join(res)
            
def get_n_corpus(n):
    res = []
    page_getter = BaiduBaikePageGetter()
    extractor = CorpusExtractor()
    for _ in range(n):
        print "get doc.."
        page = page_getter.get()
        res.append((page[0], extractor.get_corpus(page[1])))
        del page
    return res

if __name__=="__main__":
    pass


