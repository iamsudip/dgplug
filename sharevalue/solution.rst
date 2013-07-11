
==========
sharevalue
==========


This program will print the current share price of the company whose NASDAQ value is given to the program as an argument like:

::

   ./sharevalue.py [NASDAQ symbol]

Code
----

::

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

Link to code
------------

`sharevalue.py <https://github.com/iamsudip/dgplug/blob/master/sharevalue/sharevalue.py>`_

How to execute code
-------------------

Run the above script like::

    $ ./sharevalue.py [NASDAQ value]

or::

    $ python sharevalue.py [NASDAQ value]

Example output
--------------

Here some example output is given below::

    $ ./sharevalue.py ORCL

    Fetching data from: http://download.finance.yahoo.com/d/quotes.csv?s=ORCL&f=l1

    Current share price of company ORCL: 31.9449

    $ ./sharevalue.py GOOG

    Fetching data from: http://download.finance.yahoo.com/d/quotes.csv?s=GOOG&f=l1

    Current share price of company GOOG: 919.27

    $./sharevalue.py GOOG ORCL

    Syntax: ./sharevalue.py [NASDAQ Symbol]

