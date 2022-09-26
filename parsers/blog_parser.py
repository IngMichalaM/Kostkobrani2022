from bs4 import BeautifulSoup
from pages.base_page import BasePage

class BlogParser(BasePage):

    def __init__(self, page_content):
        super().__init__(page_content)
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    # def __repr__(self):
    #     return f'<Item: {self.item_text} - {self.item_link}>'

    # todo abstraktni trida - itmes musi byt jak tady tak v te druhe, nekde to zaefinovat, aby to vyzadovala definici teto methody
    @property
    def items(self):
        """ Return list of ItemParser objects.
            To get this list call it as: AllItemsPage.items() """
        blog_area_items = self.soup_page.select('div#blog_menu ul a.menu')  # all glog entries on that page

        return [BlogItemParser(e) for e in blog_area_items]


class BlogItemParser:

    def __init__(self, parent):
        self.parent = parent

    @property
    def item_link(self):
        return self.parent.get('href')