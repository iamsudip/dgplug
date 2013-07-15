
=============
planetparser
=============

The assignment was to display all the blog post title and author from `Planet Fedora <http://planet.fedoraproject.org>`_ in the terminal using a virtual environment.

So, for this work first we have to create a virtual environment. First created a temporary directory like *virtual* and I am already in it. Now we are creating and activating the env:

::

    $ virtualenv virt0
    New python executable in virt0/bin/python
    Installing distribute.............................................................................................................................................................................................done.
    Installing pip...............done.
    $ source virt0/bin/activate

Now the termianl will look like::

    (virt0)sudip@sudip-mint virtual $

Now the environment is created and we are in it. We need a module named BeautifulSoup to do this job. Let us download it::

    $ pip install beautifulsoup
    Downloading/unpacking beautifulsoup
      Downloading BeautifulSoup-3.2.1.tar.gz
      Running setup.py egg_info for package beautifulsoup

    Installing collected packages: beautifulsoup
      Running setup.py install for beautifulsoup

    Successfully installed beautifulsoup
    Cleaning up...

Now setup is complete.


Code
----

.. code:: python
    :number-lines:

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

Link to code
------------

`planetparser.py <https://github.com/iamsudip/dgplug/blob/master/planetparser/planetparser.py>`_

How to execute code
-------------------

Run the above script like::

    $ ./planetparser.py

or::

    $ python planetparser.py

Example output
--------------

Here example output is given below::

    1: Post Title: Week-end hacks
        Author: Bastien Nocera

    2: Post Title: kernel news – 15.07.2013
        Author: Rares Aioanei

    3: Post Title: morituri 0.2.1 “married” released
        Author: Thomas Vander Stichele

    4: Post Title: Fedora 19 With Google-authenticator login
        Author: Onuralp SEZER

    5: Post Title: Alistando Fedora 19 Release Party Managua
        Author: Neville A. Cross - YN1V

    6: Post Title: How to run Pidora in QEMU
        Author: Ruth Suehle
