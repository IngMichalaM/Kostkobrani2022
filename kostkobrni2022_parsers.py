import time
import requests

from pages.product_page import ProductPage
from parsers.search_results_parser import AllItemsPage
from configuration import MainConfig
from parsers.blog_parser import BlogParser

""" This is the main page for the version with only the parsers used (no driver) """

start_time = time.time()

# Get the method and search text/url from config file
config = MainConfig()
current_search_link, method = config.url()
known_codes = config.known_codes()
dice_code_part, dice_code_pattern = config.dice_code_partition()  # tuple (bool, string)

# Get the content of the URL and go through each item on the page
search_res_content = requests.get(current_search_link).content
if method == 'blog':
    search_res_page = BlogParser(search_res_content)
else:
    search_res_page = AllItemsPage(search_res_content)  # returns list of ItemParser objects
                                                    # go through the individual web pages
counter = 1  # counts the pages with results, only for dispaly purposes
dice_code_bol = True


while dice_code_bol:
    print(f'------- Search page {counter} -------------')

    for i in search_res_page.items:
        print(i.item_title)
        current_link_content = requests.get(i.item_link).content
        pp = ProductPage(current_link_content, method, (dice_code_part, dice_code_pattern))  # product page of current item

        if dice_code_part:
            if pp.dice_code:
                # The partial code is most probably here, display the link and check it out
                print(f'The partial dice code is here {i.item_link}.')
        else:
            # print('We are looking for the whole dice code ')
            if pp.dice_code:

                # check if this code is in the list of known codes
                # You may find the known code if you go through for example the Blog again with a new hint.

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
            # there were no dice code within the items on the current search page. Go to the other page, if there is any
            next_search_link = search_res_page.next_page_link
            # print(f'(main) Next page link is <{next_search_link}>.')
            search_res_content = requests.get(next_search_link).content
            if method == 'blog':
                search_res_page = BlogParser(search_res_content)
            else:
                search_res_page = AllItemsPage(search_res_content)
            # print(f'Current ({counter}.) result page is done, going to the next one.')
            counter += 1
        except AttributeError:
            print(f'Current ({counter}.) result page is done and there is no other result page. We are done here.')
            dice_code_bol = False
            break
        except Exception:
            raise ValueError

end_time = time.time()
elapsed_time = end_time - start_time
if elapsed_time > 60*60:
    print(f'Total elapsed time is: {elapsed_time/60/60:.2f} h.')
elif elapsed_time > 60:
    print(f'Total elapsed time is: {elapsed_time / 60:.2f} min.')
else:
    print(f'Total elapsed time is: {elapsed_time:.2f} s.')
