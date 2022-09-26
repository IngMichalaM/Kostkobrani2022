from bs4 import BeautifulSoup

class HomePageParser:

    def __init__(self, page_content, url):
        self.soup_content = BeautifulSoup(page_content, 'html.parser')
        self.url = url

    @property
    def left_column(self):
        left_column_content = self.soup_content.select('div#column_left li a')

        return [LeftColumnItemsParser(e, self.url) for e in left_column_content]
        # e - beautifulsoup tag


class LeftColumnItemsParser:

    def __init__(self, parent, url):
        """ Parent is the whole <a> tag containing the link and its text. """

        self.parent = parent
        self.url = url

    def __repr__(self):
        return f'<Item: {self.item_text_text} - {self.item_link}>'


    @property
    def item_text_text(self):
        # '\n\n\nX\n\n\n\nNovinky\n          \n\n\n\nAKCE a SLEVY\n
        return self.parent.text.strip()

    # @property
    # def item_text_string(self):
    #     return self.parent.string

    @property
    def item_title(self):

        return self.parent.get('title')

    @property
    def item_link(self):
        link = self.parent.get('href')

        if 'https' not in link:
            link = link.strip('/>')
            link = self.url + link

        return link



if __name__ == '__main__':
    from imago_homepage import ImagoHomepage
    from selenium import webdriver
    import requests

    # driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1300,1000')
    # chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://www.imago.cz/'
    homepage = ImagoHomepage(driver, url)
    # homepage.go()

    page_content = requests.get(url).content
    left_column_items = HomePageParser(page_content, url)

    for item in left_column_items.left_column:
        print(item)

