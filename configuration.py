import configparser
from typing import List


class MainConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_file(open(r'config.txt'))

    def url(self):
        """ Read from the config file, which search method
         is used. Return url that will be used for searching through. """

        search_method = self.config.get('Search mode', 'search_method')

        # text, url, blog
        if search_method == 'blog':
            current_search_link = 'https://www.imago.cz/blog'
        elif search_method == 'text':
            # 1) get the search word
            search_text_word = self.config.get('Search mode', 'search_text_word')
            search_text_word.title()

            # 2) Construct the search url
            basic_search_string = 'https://www.imago.cz/hledani?q='
            check_search_text = search_text_word.split(' ')

            if len(check_search_text) == 1:  # one word
                current_search_link = basic_search_string + search_text_word
            else:
                current_search_link = basic_search_string + ('%20').join(check_search_text)
        elif search_method == 'url':
            current_search_link = self.config.get('Search mode', 'search_text_url')
        else:
            raise ValueError(f'The method {search_method} is not implemented (choose between: blog, text, url).')

        print(f'The current_search_link is: {current_search_link}.')
        return current_search_link, search_method

    def known_codes(self) -> List[str]:
        known_codes = self.config.get('Known Codes', 'codes')  # str
        known_codes = known_codes.split(',')
        list_of_codes = [code.strip() for code in known_codes]

        return list_of_codes

    def dice_code_partition(self) -> tuple[bool, str]:
        """ Sometimes wer are not looking for the whole code, but for its fragments.
            And we do not know how the fragments are structured.
            In this case, we do not look for the code itself, but for the anoncment abou the dice:
            'Jste na lovu kostek' """

        if self.config.get('Code problem', 'enable') == 'True':
            return True, str(self.config.get('Code problem', 'pattern'))
        else:
            return False, ''


if __name__ == '__main__':
    config = MainConfig()
    # url =config.url()
    # print(url)

    known_codes = config.known_codes()
    print(known_codes)
    print(type(known_codes))

