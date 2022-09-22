import re
from bs4 import BeautifulSoup


class ProductPage:
    """ Product Page of the particular item. Main focus here is to find the dice-code
        within the product area. """

    def __init__(self, page_content):
        self.soup_page = BeautifulSoup(page_content, 'html.parser')

    @property
    def dice_code(self):
        """ Only think that we need on the Product Page is, whether it contains the dice code or not.
            If yes, then we want the code.  """

        locator = 'div.product_detail'

        try:
            desired_div_with_text = self.soup_page.select_one(locator)  # finds first paragraph with the product
                                                                        # description
            # desired_div_with_text = self.soup_page.select(locator) # there are actually three paragraphs,
                                                                     # but only the first one is of interest
            # look for the dice code within it. A list can be returned
            dice_codes = self.find_dice_expression(desired_div_with_text)

            return dice_codes

        except AttributeError:
            return None

    def find_dice_expression(self, desired_div_with_text):
        """ Look through the parent element and find dice code (e.g. K6XB65H59Q) if it is there. """

        pattern = '[0-9A-Z]{10}'  # 10 char long element with numbers and capital letters

        # matcher = re.search(pattern, item_description_paragraph)
        # dice_code = matcher.group(1)
        dice_codes = re.findall(pattern, str(desired_div_with_text))

        # sometimes it happens that a number 10 char long is found, which is not the proper structure of the code
        for dice_code in dice_codes:

            if self.contains_capital_letter(dice_code):
                return dice_code
            else:
                return []

        # todo: now the opposit can maybe happen and we would need to check if the string contains any numbers
        #       will desl with it when it comes.

    def contains_capital_letter(self, expression: str) -> bool:
        """ Check if the string does contain a capital letter.  """

        pattern = '[A-Z]+'
        expr_with_cap_letter = re.findall(pattern, expression)

        if len(expr_with_cap_letter) >= 1:
            # the expression contains a capital letter
            return True
        else:
            return False


if __name__ == '__main__':
    import requests

    search_res_content = requests.get('https://www.imago.cz/funko-pop-therizinosaurus-1206').content
    pp = ProductPage(search_res_content)
    print(pp.dice_code)