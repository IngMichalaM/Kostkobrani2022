import configparser

class MainConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_file(open(r'config.txt'))

    def url(self):
        """ Read from the config file, which search method
         is used. Return url that will be used for searching through. """

        search_text_method = self.config.get('Search mode', 'search_text')
        if search_text_method == 'True':
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

        else:
            current_search_link = self.config.get('Search mode', 'search_text_url')

        print(f'The current_search_link is: {current_search_link}.')
        return current_search_link

if __name__ == '__main__':

    config = MainConfig()
    url =config.url()
    print(url)
