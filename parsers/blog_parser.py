from bs4 import BeautifulSoup
from pages.base_page import BasePage

from parsers.base_items_parser import BaseItemParser


class BlogParser(BasePage):

    def __init__(self, page_content):
        super().__init__(page_content)
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def items(self):
        """ Return list of ItemParser objects.
            To get this list call it as: BlogParser.item() """
        blog_area_items = self.soup_page.select('div#blog_menu ul a.menu')  # all glog entries on that page

        return [BlogItemParser(e) for e in blog_area_items]


class BlogItemParser(BaseItemParser):
    """ From the given parent (Beautifulsoup object) retrieve the properties of the item
        (one particular product on the web). Some of the features are defined in the BaseItemParser. """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
