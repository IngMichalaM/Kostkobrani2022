from bs4 import BeautifulSoup

class BasePage(object):

    """ Common methods for all the pages.  """

    def __init__(self, page_content):
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def next_page_link(self) -> str:
        """ Returns a link for the next search result page.
            Does not matter how many pages there are, it always return the next one.
            This is common for all the pagest - normal product pages AND the blog as well. """

        locator = 'div#pagination_bottom > div.links > a.pagination-item'
        next_page_obj = self.soup_page.select_one(locator)
        next_page_link = next_page_obj.get('href')

        return next_page_link