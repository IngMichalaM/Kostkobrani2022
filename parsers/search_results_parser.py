from bs4 import BeautifulSoup
from pages.base_page import BasePage

from parsers.base_items_parser import BaseItemParser


class AllItemsPage(BasePage):
    """ Product Page Listing
        24 products fit on the page.
        Each item has its name, price, url, etc. self.ItemParser create a separate object for each item. """

    def __init__(self, page_content):
        super().__init__(page_content)
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def items(self):
        """ Return list of ItemParser objects.
            To get this list call it as: AllItemsPage.items() """
        product_area_items = self.soup_page.select('div#productsArea div.bunka_vypisu h3 a') #  all 24 product on the page

        return [ItemParser(e) for e in product_area_items]


class ItemParser(BaseItemParser):
    """ From the given parent (Beautifulsoup object) retrieve the properties of the item
        (one particular product on the web). Some of the features are defined in the BaseItemParser. """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def __repr__(self):
        return f'<Item: {self.item_text} - {self.item_link}>'

    @property
    def item_text(self):
        return self.parent.text.strip()

    @property
    def item_title(self):
        return self.parent.get('title')

