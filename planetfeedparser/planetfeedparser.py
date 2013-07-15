#!/usr/bin/env python
import feedparser
import sys

def error():
    """
    Function for any kind of argumental error handling
    """
    print 'Usage: ./rss2parser.py [LINK] [OPTION](optional)'+'\n'
    print './rss2parser.py: error: you must provide URL like: http://planet.fedoraproject.org/rss*.xml'+'\n'
    print '[OPTION]'+'\n'
    print '-l or --link'
    print '    Print links the posts'
    sys.exit(-1)



def make_food(link, flag=0):
    """
    Function to display post titles, respective author and original link to the posts(optional)
    """
    #Parsing the rss20.xml document
    feed = feedparser.parse(link)
    #Counting total posts
    total_posts = len(feed.entries)
    #Counter for loop
    count = 0

    #Loop to do the job
    while count < total_posts:
        
        #Fectching author & post titles from 'feed' object
        author_title = feed.entries[count].title
        
        #List index
        i=0
        length= len(author_title)
        author=''
        post_title=''
        
        #Fetching author
        while author_title[i] != ':':
            author = author + author_title[i]
            i +=1
        #Fetching title
        while i < length:
            post_title = post_title + author_title[i]
            i +=1
        count += 1
        
        #Printing
        print str(count) + ': Post Title' + post_title
        print '        Author: ' + author
        
        #It is optional part when argument -l or --link given then only it will be execute and show all the link to the respective posts
        if flag == 1:
            post_link=feed.entries[count-1].link
            print '         Link: ' + post_link + '\n'

if __name__ == '__main__':
    arg = len(sys.argv) - 1
    if arg == 0 or arg > 2:
        error()
    if arg == 1:
        make_food(sys.argv[1])
        sys.exit(0)
    if arg == 2:
        if sys.argv[2]=='-l' or sys.argv[2]=='--link':
            make_food(sys.argv[1], 1)
            sys.exit(0)
        else:
            error()
