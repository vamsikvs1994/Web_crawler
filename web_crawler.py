"""
Author: Venkata Sai Vamsi Komaravolu

Date: 30th December 2017

File Name: web_crawler.py

Description:
The working of this program classified as mentioned below:

1. Go to the given web-page and grep all the web-links in the page.

2. print out the 5 top most words in the web-page.
 
3. Go to each web-link page and repeat the process.

4. Perform the web crawling up to the depth of 3 using DFS. 

5. Implemented everything in python. Used Class structure in the python.
"""

import requests                                                                                                                 #Requests Library is used to send HTTP requests and obtain response                                                                                                                                                                                                                                                                
from bs4 import BeautifulSoup                                                                                                   #BeautifulSoup Library is used to pull data out of the HTML files

import word_counter                                                                                                             #importing the word_counter file for finding and counting the words in a web page
from urllib.request import urlopen                                                                                              #urlopen is used to open a network object denoted by a URL for reading


class web_crawler():                                                                                                            #web_crawler class which performs web crawling upto depth of 3

    def __init__(self,url):                                                                                                     # __init__ is the constructor method for the class which passes the arguments to it when the object is first created
        
        web_page_info = requests.get(url)                                                                                       # requests.get() is used to request data from a webpage  
        normal_text = web_page_info.text                                                                                        #takes the text from the web_page we are going to crawl 
        soup = BeautifulSoup(normal_text, "html.parser")                                                                        #coverting the text into a BeautifulSoup object for the web crawling and other things to take place in a idiomatic way
        for link in soup.findAll('a',{'class':''}):                                                                             #finds the links represented by anchors (a) which have a class 
            href = link.get('href')                                                                                             #takes out the href part of the link, which is nothing but the URL links in the web-page
            if link.get('href') is not None:                                                                                    #makes sure that the 'href' is not an empty string before proceeding
                href = link.get('href')                     
                if (link['href'].startswith("/w/") or link['href'].startswith("#") or link['href'].startswith("//")):           #if the links starts with an invalid formaat, those links are ignored
                    continue
                elif link['href'].startswith("/wiki/"):                                                                         #if the links start with '/wiki/' , deafault url of "https://en.wikipedia.org" is added to href to form the complete url
                    l1ref = "https://en.wikipedia.org" + href
                    title = link.string
                else:                                                                                                           #else the link is valid and is left as it is                           
                    l1ref = link.get('href')
                    title = link.string
                print("\n********************Main Page article:",title,"********************\n")
                
                web_page_info = requests.get(l1ref)                                                                             #the links found in the main web-page are passed as as argument for requests.get() to crawl the level-1 page
                normal_text = web_page_info.text
                soup = BeautifulSoup(normal_text, "html.parser")
                for link in soup.findAll('a',{'class':''}):
                    href = link.get('href')
                    if link.get('href') is not None:
                        href = link.get('href')
                        if (link['href'].startswith("/w/") or link['href'].startswith("#") or link['href'].startswith("//")):
                            continue    
                        elif link['href'].startswith("/wiki/"):  
                            l2ref = "https://en.wikipedia.org" + href
                            title_level1 = link.string
                        else:
                            l2ref = link.get('href')
                            title_level1 = link.string
                        print("\n********************Main Page article:",title, "/ Level-1 article:",title_level1,"********************\n")
                        
                        web_page_info = requests.get(l2ref)                                                                     #the links found in the level-1 web-page are passed as as argument for requests.get() to crawl the level-2 page
                        normal_text = web_page_info.text
                        soup = BeautifulSoup(normal_text, "html.parser")
                        for link in soup.findAll('a',{'class':''}):
                            href = link.get('href')
                            if link.get('href') is not None:
                                href = link.get('href')
                                if (link['href'].startswith("/w/") or link['href'].startswith("#") or link['href'].startswith("//")):
                                    continue
                                elif link['href'].startswith("/wiki/"):  
                                    l3ref = "https://en.wikipedia.org" + href
                                    title_level2 = link.string
                                else:
                                    l3ref = link.get('href')
                                    title_level2 = link.string
                                print("\n********************Main Page article:",title, "/ Level-1 article:",title_level1, "/ Level-2 article:",title_level2,"********************\n")
                                
                                web_page_info = requests.get(l3ref)                                                             #the links found in the level-2 web-page are passed as as argument for requests.get() to crawl the level-3 page
                                normal_text = web_page_info.text
                                soup = BeautifulSoup(normal_text, "html.parser")
                                for link in soup.findAll('a',{'class':''}):
                                    href = link.get('href')
                                    if link.get('href') is not None:
                                        href = link.get('href')
                                        if (link['href'].startswith("/w/") or link['href'].startswith("#") or link['href'].startswith("//")):
                                            continue
                                        elif link['href'].startswith("/wiki/"):  
                                            l4ref = "https://en.wikipedia.org" + href
                                            title_level3 = link.string
                                        else:
                                            l4ref = link.get('href')
                                            title_level3 = link.string
                                        print("\n********************Main Page article:",title, "/ Level-1 article:",title_level1, "/ Level-2 article:",title_level2, "/ Level-3 article:",title_level3,"********************\n")
                                        
                                        print("******Top-5 most used words in Level-3 crawled web page:--",title_level3,"--are", "******\n")
                                        word_counter.main(l4ref)                                                                #prints the Top 5 most used words in level-3 crawled pages
                                        
                                print("******Top-5 most used words in Level-2 crawled web page:--",title_level2,"--are", "******\n")
                                word_counter.main(l3ref)                                                                        #prints the Top 5 most used words in level-2 crawled pages
                                
                        print("******Top-5 most used words in Level-1 crawled web page:--",title_level1,"--are", "******\n") 
                        word_counter.main(l2ref)                                                                                #prints the Top 5 most used words in level-1 crawled pages
                        
                print("******Top-5 most used words in Main page crawled web page:--",title,"--are", "******\n") 
                word_counter.main(l1ref)                                                                                        #prints the Top 5 most used words in Main page crawled pages
        
        print("******Top-5 most used words in Main URL page are", "******\n") 
        word_counter.main(url)                                                                                                  #prints the Top 5 most used words in the given Main URL page
        
                
obj1 = web_crawler("https://en.wikipedia.org/wiki/Main_Page")                                                                   #creating an object for the web_crawler class
