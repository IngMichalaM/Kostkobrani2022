from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod


class BasePage(metaclass=ABCMeta):
    """ Common methods for all the pages.  """

    def __init__(self, page_content):
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def next_page_link(self) -> str:
        """ Returns a link for the next search result page.
            Does not matter how many pages there are, it always returns the next one.
            This is common for all the pages - normal product pages AND the blog entries as well. """

        locator = 'div#pagination_bottom > div.links > a.pagination-item'
        next_page_obj = self.soup_page.select_one(locator)
        next_page_link = next_page_obj.get('href')

        return next_page_link

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

    @abstractmethod
    def items(self):
        """ Return list of ItemParser objects.
            Must be properly implemented in the classes that inherit from the BasePage. """
        pass
