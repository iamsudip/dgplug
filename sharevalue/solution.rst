
=============
sharevalue v2
=============

The assignment was to print share value of a given company NASDAQ symbol.

This script can take many NASDAQ symbol at one go & will give desired output.

It is able to print the corresponding company name (if any) from given NASDAQ symbol.

This program will print the current share price of the company whose NASDAQ value is given to the program as an argument like:

::

   ./sharevalue.py [NASDAQ symbol] [NASDAQ symbol] [NASDAQ symbol]

Code
----

.. code:: python
   :number-lines:

   #!/usr/bin/env python

   import urllib2
   import sys

   def main(nasdaq):

       """
       Here all work is being done.

       :arg nasdaq: NASDAQ symbol
       """

       #Making the link in 'link' string to fetch share value
       link = 'http://download.finance.yahoo.com/d/quotes.csv?s='+nasdaq+'&f=l1'
       print 'Fetching recent share value of '+nasdaq

       #Share value saved into an instance share_value
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

       #Printing share_value which was saved in share_value previously
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

Link to code
------------

`sharevalue.py <https://github.com/iamsudip/dgplug/blob/master/sharevalue/sharevalue.py>`_

How to execute code
-------------------

Run the above script like::

    $ ./sharevalue.py [NASDAQ value] [NASDAQ symbol] [NASDAQ symbol] [NASDAQ symbol]

or::

    $ python sharevalue.py [NASDAQ value] [NASDAQ symbol] [NASDAQ symbol] [NASDAQ symbol]

Example output
--------------

Here some example output is given below::

    $ ./sharevalue.py ORCL
    Fetching recent share value of ORCL
    O R C L   s t o c k   q u o t e   -   O r a c l e   C o r p o r a t i o n
    Current share price of company ORCL: 31.86

    $ ./sharevalue.py ORCL GOOG RHT
    Fetching recent share value of ORCL
    O R C L   s t o c k   q u o t e   -   O r a c l e   C o r p o r a t i o n
    Current share price of company ORCL: 31.86

    Fetching recent share value of GOOG
    G O O G   s t o c k   q u o t e   -   G o o g l e   I n c .
    Current share price of company GOOG: 920.24

    Fetching recent share value of RHT
    R H T   s t o c k   q u o t e   -   R e d   H a t ,   I n c .
    Current share price of company RHT: 50.57

    $./sharevalue.py
    Atleast 1 Argument needed
    Syntax: ./sharevalue.py [NASDAQ Symbol] [NASDAQ Symbol]
