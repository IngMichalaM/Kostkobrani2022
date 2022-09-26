# Kostkobrani 2022 - annual "dice harvest" at imago.cz

## Introduction
This is a small project for my use for the annual "dice harvest" at 
the czech fantasy shop www.imago.cz. 

## Details
As I have only this year learned, this mystery-riddle-puzzle-track-game is already a tradition.
Every day (for app. a month), a hint appears on imago's blog. Using this hint you have to find a special
dice-encrypted-code (10 char long string of capital letters and numbers).
And either your are really good with the hints (and your can find the particular page with the particular product
and the dice code), or you are not that good and you have to use a little bit of brute-force. 
I am a combination of both. I can narrow it down using the hint, but then I need to go through
several pages of products to find the right one. 
And that is when this script comes handy. 

There are basically three ways of finding what I am looking for:
1) I know the word I am looking for (e.g. bow). So this word will be used by this script to search all products with bows
 and to go through one by one.
2) Or I have the URL where I want to be searching (for example some subcategory on the pages). So I use this for the search.
3) A separate search is for the Blog. It's structure is slightly different, so the search uses a different locator. 

The script then looks through the paragraphs of the Product Pages (or individual Blog entries) from the Product Listing Pages and as soon as 
it finds the proper string, it returns it and finishes.

It might happen that the search finds a dice code which we have already found previously (e.g. a hint from previouis days lead us to a blog entry, 
and today's hint leads again to blog. Since the search goes through ALL the Blog's entries, it will definitely find the old code as well).
To prevent the search to stop after first code found, user has to provide a list of known codes (in the config.txt). The 
search then check if the code from the current search is known or new. 

## Problems
Sometimes,
- the dice-codes are within an image
- the dice-codes are within subtitles of an youtube video
- the dice-code is created by putting together several parts of the string (which can be found on several different pages)
or result of a crossword puzzle


In these situation I really have to look for the code by myself :-) (but that is the fun part after all).

## Big final
And what is all this good for? After a month of searching for the dice-codes, you receive virtual dice according to the codes you 
have collected and you can virtually throw them. Based on the score you recieve virtual money and you can buy items in the shop.

## Config file
 - Mind the special characters - they are not properly loaded from the config file.
 - You can choose between the 'search word' or 'search url'
 - You have to provide either a word (for the search word method), or an url (for the search url method) 
 
## Technologies
Python 3.9
