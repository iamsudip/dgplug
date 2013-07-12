#!/usr/bin/env python

import urllib2
import sys

def main(nasdaq):

    """
    Here all work is being done.

    :arg nasdaq: NASDAQ symbol
    """

    #Making the link in 'link' string to fetch data
    link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaq+'&f=l1'
    print 'Fetching recent share value of '+nasdaq

    #share value saved into an instance share_value
    share_value = urllib2.urlopen(link)

    #Fetching data to find company name
    html_data=urllib2.urlopen('http://www.nasdaq.com/symbol/'+nasdaq)
    name=html_data.read()
    
    #Finding the Company name & Displaying
    start=name.find('<title>')+7
    end=name.find('</title>')-25
    while start < end:
        print name[start],
        start+=1
    html_data.close()

    #Printing share_value which was saved ti share_value
    print '\n'+'Current share price of company '+nasdaq+': '+share_value.read()
    share_value.close()

if __name__ == '__main__':
    
    #Counting the NASDAQ Symbol (Arguments)
    count = len(sys.argv) - 1 
    
    #Checking if atleast one symbol available or not
    if count >= 1:
        
        #NASDAQ symbol available passing it to main() function 
        i=0
        while i < count:
            i+=1
            main(sys.argv[i])
    
    else:
        #If nothing given as argument it will print the syntax to use this code"
        print 'Atleast 1 Argument needed'+'\n'+'Syntax: ./sharevalue.py [NASDAQ Symbol] [NASDAQ Symbol]'   
    sys.exit(0)
