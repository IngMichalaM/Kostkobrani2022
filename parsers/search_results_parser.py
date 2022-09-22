from bs4 import BeautifulSoup


class AllItemsPage:
    """ Product Page Listing
        24 products fit on the page.
        Each item has its name, price, url, etc. self.ItemParser create a separate object for each item. """

    def __init__(self, page_content):
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def items(self):
        """ Return list of ItemParser objects.
            To get this list call it as: AllItemsPage.items() """
        product_area_items = self.soup_page.select('div#productsArea div.bunka_vypisu h3 a') #  all 24 product on the page

        return [ItemParser(e) for e in product_area_items]

    @property
    def page_count(self):
        """ Return the last 'displayed' number of the search result page.
            The maximum to be displayed is 11.
            Problem is, that if the search returns more items, those pages are not visibly displayed.
            Better use self.next_page_link, which finds the next page, and next page, and so on. """

        locator = 'div#pagination_bottom > div.links > a'
        counters_list = self.soup_page.select(locator)
        counter = [e.text for e in counters_list]
        if counter:
            return int(counter[-3])
        else:
            return 0

    @property
    def next_page_link(self) -> str:
        """ Returns a link for the next search result page.
            Does not matter how many pages there are, it always return the next one. """

        locator = 'div#pagination_bottom > div.links > a.pagination-item'
        next_page_obj = self.soup_page.select_one(locator)
        next_page_link = next_page_obj.get('href')

        return next_page_link


class ItemParser:
    """ From the given parent (Beautifulsoup object) retrieve the properties of the item
        (one particular product on the web). """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Item: {self.item_text} - {self.item_link}>'

    @property
    def item_text(self):
        return self.parent.text.strip()

    @property
    def item_title(self):
        return self.parent.get('title')

    @property
    def item_link(self):
        return self.parent.get('href')
