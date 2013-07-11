#!/usr/bin/env python

import urllib2
import sys

def main(nasdaq):

    """
    Here all work is being done.

    :arg nasdaq: NASDAQ symbol
    """

    #making the link in 'link' string to fetch data'
    link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaq+'&f=l1'
    print 'Fetching data from: '+link

    #data saved into an instance share_value
    share_value = urllib2.urlopen(link)

    #Printing share_value
    print 'Current share price of company '+nasdaq+': '+share_value.read()

if __name__=='__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Syntax: ./sharevalue.py [NASDAQ Symbol]"    
    sys.exit(0)
    
