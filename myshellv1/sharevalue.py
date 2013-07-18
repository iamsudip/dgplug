#!/usr/bin/env python

import requests
import sys

def share(nasdaq):

    """
    Here all work is being done.

    :arg nasdaq: NASDAQ symbol
    """

    #Making the link in 'link' string to fetch data
    link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaq+'&f=l1'
    print 'Fetching recent share value of '+nasdaq

    share_value = requests.get(link)

    print '\n'+'Current share price of company '+nasdaq+': '+share_value.text
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
            share(sys.argv[i])
