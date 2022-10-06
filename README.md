# Kostkobrani 2022 - annual "dice harvest" at imago.cz

## Introduction
This is a small project for my use for the annual "dice harvest" at 
the czech fantasy shop www.imago.cz. 

## Details
As I have only this year learned, this mystery-riddle-puzzle-track-game is already a tradition.
Every day (for app. a month), a hint appears on imago's blog. Using this hint you have to find a special
dice-encrypted-code (10 char long string of capital letters and numbers).
And either your are really good with the hints (and you can find the particular page with the particular product
and the dice code), or you are not that good and you have to use a little bit of brute-force. 
I am a combination of both. I can narrow it down using the hint, but then I need to go through
several pages of products to find the right one. 
And that is when this script comes handy. 

There are basically three (plus one) ways of finding what I am looking for:
1) I know the word I am looking for (e.g. bow). So this word will be used by this script to search all products with bows
 and to go through one by one.
2) Or I have the URL where I want to be searching (for example some subcategory on the pages). So I use this for the search.
3) A separate search is for the Blog. Its structure is slightly different, so the search uses a different locator. 
4) See section 'Problems'.

The script then looks through the paragraphs of the Product Pages (or individual Blog entries) from the Product Listing Pages and as soon as 
it finds the proper string, it returns it and finishes.

It might happen that the search finds a dice code which we have already found previously (e.g. a hint from previous days leads us to a blog entry, 
and today's hint leads again to blog. Since the search goes through ALL the Blog's entries, it will definitely find the old code as well).
To prevent the search to stop after first code found, user has to provide a list of known codes (in the config.txt). The 
search then checks if the code from the current search is known or a new one. 

## Problems
Sometimes,
- the dice-codes are within an image
- the dice-codes are within subtitles of a youtube video
- the dice-code is created by putting together several parts of the string (which can be found on several different pages)
or result of a crossword puzzle

In these situations I really have to look for the code by myself :-) (but that is the fun part after all).
For this third part, when the code is cut to small pieces, I came up with a fourth method - the search does not look for 
the dice code directly, but rather it looks for the text that accompanies the dice code. Usually it is something like:
'Gratulujeme' (EN: Congratulations) or 'Jste na lovu kostek' (EN: You are on the dice hunt). In this case, the script returns
the url of the product where he found these words.

## Big final
And what is all this good for? After a month of searching for the dice-codes, you receive virtual dice according to the codes you 
have collected and you can virtually throw them. Based on the score you receive virtual money and you can buy items in the shop 
with discount.

## Config file
 - In the configuration file config.txt your define the parameters for the search.  
 - Mind the special characters - they are not properly loaded from the config file.
 - There are three methods: text, url, blog. 
   - text - this is the string you would insert on the web page into the search input field. It finds all the products that fit the word and look through it. 
   You define the search worked in the variable "search_text_word".
   - url - you want to look through this particular url. It hase to be a page with the products listing, not one particular 
    product page or blog entry. You define the url in the parameter "search_text_url".
   - blog - the search goes through the whole blog, all blog entries. No need to define anything else.
 - Known Codes - comma separated known codes, so that teh script does not stop after finding the fist code, but first, check if the code is already known or not.
 - Code problem - use in case you are looking for only a part of the code. If you want to use this feature: enable = True. You need to define the word we are looking for, e.g. "Gratulujeme".
 
## Technologies
Python 3.9
