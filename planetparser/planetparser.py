#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup
import urllib2
import sys

def fetch():
    """
    Function to fetch data from url
    """

    #Fetching html content from Planet Fedora
    html_cont = urllib2.urlopen('http://planet.fedoraproject.org')
    data = html_cont.read()
    html_cont.close()
    return data

def make_soup(food):
    """
    Function to make the parse the html document and return the list as desired output
    
    :arg food: html data
    """

    #Using fetched data BeautifulSoup is giving a BeautifulSoup Object as 'soup'
    soup = BeautifulSoup(food)
    
    #Finding all the 'div' element with attribute class='string'
    post_list = soup.findAll('div', attrs={'class' : 'blog-entry-title'})
    author_list = soup.findAll('div', attrs={'class' : 'blog-entry-author'})
    
    #post_list, author_list: List of required data
    return post_list, author_list

def printem(post_name_list, author_list):
    """
    Function to print Post titles and respectives authors
    """

    #Initialized counter
    count = 0
    
    #Finding how many list element
    length = len(post_name_list)
    
    #Looping both post titles and corresponding author
    while count < length:
        
        #Finding the text
        post = post_name_list[count].find('a').string
        by_author = author_list[count].find('a').string        
        
        #Printing them
        count += 1
        print str(count) + ': Post Title: ' + post
        print '        Author: ' + by_author + '\n'

if __name__ == '__main__':
    data=fetch()
    post, author=make_soup(data)
    printem(post, author)
    sys.exit(0)
