import requests

from pages.product_page import ProductPage
from parsers.search_results_parser import AllItemsPage
from configuration import MainConfig
from parsers.blog_parser import BlogParser

""" This is the main page for the version with only the parsers used (no driver) """

# Get the method and search text/url from config file
config = MainConfig()
current_search_link, method = config.url()

# Get the content of the URL and go through each item on the page
search_res_content = requests.get(current_search_link).content
if method == 'blog':
    # only for blo
    search_res_page = BlogParser(search_res_content)
else:
    search_res_page = AllItemsPage(search_res_content)  # returns list of ItemParser objects
                                                    # go through the individual web pages
counter = 1  # counts the pages with results, only for dispaly purposes
dice_code_bol = True

while dice_code_bol:
    print(f'------- Search page {counter} -------------')

    for i in search_res_page.items:

        current_link_content = requests.get(i.item_link).content
        pp = ProductPage(current_link_content, method)  # product page of current item

        if pp.dice_code:

            # check if this code is in the list of known codes
            # You may find the known code if you go throug for examply the Blog again with a new hint.
            known_codes = config.known_codes()
            # todo - what if pp.dice_code is a list (might happen if some id or similar tag value has the same
            #  structure as the dice code)
            if pp.dice_code not in known_codes:
                print(f'The dice code is <{pp.dice_code}>. Found on {i.item_link}. We are done here.')
                dice_code_bol = False
                break
            else:
                print(f'The dice code <{pp.dice_code}> is already known. Going on with the search.')

    else:
        try:
            # there were no dice code within the items on the current search page. Go to the other, if there is any
            next_search_link = search_res_page.next_page_link
            search_res_content = requests.get(next_search_link).content
            if method == 'blog':
                search_res_page = BlogParser(search_res_content)
            else:
                search_res_page = AllItemsPage(search_res_content)
            # print(f'Current ({counter}.) result page is done, going to the next one.')
            counter += 1
        except Exception:
            print(f'Current ({counter}.) result page is done and there is no other result page. We are done here.')
            dice_code_bol = False
            break
