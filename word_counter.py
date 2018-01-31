'''
Author: Venkata Sai Vamsi Komaravolu

Date: 30th December 2017

File Name: word_counter.py

Description:
This python program performs the word count in a web-page given the URL. It makes use of certain 
methods and packages available in python.

The working of this program classified as mentioned below:

1. Open the given URL

2. Read the web-page and using the utf-8 format decoding

3. Remove the tags in the web page

4. Remove all the non-alphanumeric characters in the word string

5. Count the words and form a dictionary

6. Finally sorting and displaying the top 5 most used words in the web-page


'''

import re                                                                               #regular expression package
from urllib.request import urlopen                                                      #urlopen is used to open the web-page using the given URL

def main(url):
    opened_url = urlopen(url)                                                           #open the given web-page from the given url
    decoded_url = opened_url.read().decode('utf-8')                                     #read the web-page and decode according to utf-8 format 
    text = remove_tags(decoded_url).lower()                                             #remove the tags in the webpage and lower() makes all case-based characters lowercased
    words = remove_non_alp_num(text)                                                    #remove all non-alphanumeric characters
    dict = word_counter(words)                                                          #creates a dictionary with the words and their count
    sorted_words = sort_counter(dict)                                                   #sorts the dictionary and returns the words and their count in descending order

    count=0
    for s in sorted_words:                                                              #displays the 5 top most used words in the given web-page
        if(count<5):
            print(str(s))
        count+=1
    return
    
def remove_tags(page_info):                                                             #method to remove the tags in the the given web-page
    start = page_info.find("</a>")
    end = page_info.rfind("</li>")                                                      #rfind() returns the last index where the substring is found

    page_info = page_info[start:end]                                                    

    ins = 0
    word_form = ''

    for char in page_info:                                                              # creating a word form from the characters
        if char == '<':                                                                 # word string is between the < and > characters
            ins = 1
        elif (ins == 1 and char == '>'):
            ins = 0
        elif ins == 1:
            continue
        else:
            word_form += char

    return word_form


def remove_non_alp_num(text):                                                           #method for removing all non-alphanumeric characters using UNICODE definition
    return re.compile(r'\W+', re.UNICODE).split(text)                                   #re.compile() is used to compile a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods

def word_counter(words):                                                                #method for creating a Python dictionary with words and their respective count
    wordfreq = [words.count(p) for p in words]
    return dict(zip(words,wordfreq))
	
def sort_counter(dict):                                                                 #method for sorting and displaying the words with their count in descending order
    out = [(dict[key], key) for key in dict]
    out.sort()
    out.reverse()
    return out
