#!/usr/bin/env python

import urllib2
import sys

def share(nasdaq):

    """
    Here all work is being done.

    :arg nasdaq: NASDAQ symbol
    """

    #Making the link in 'link' string to fetch data
    link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaq+'&f=l1'
    print 'Fetching recent share value of '+nasdaq

    #share value saved into an instance share_value
    share_value = urllib2.urlopen(link)

    #Printing share_value which was saved ti share_value
    print '\n'+'Current share price of company '+nasdaq+': '+share_value.read()
    share_value.close()
