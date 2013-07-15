
================
planetfeedparser
================

The assignment was to display all the blog post title and author from `Planet Fedora <http://planet.fedoraproject.org>`_ in the terminal.

The script is completely able to do this job and for extra it can show user the links to blogposts if needed.


Code
----

.. code:: python
    :number-lines:

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


Link to code
------------

`planetfeedparser.py <https://github.com/iamsudip/dgplug/blob/master/planetfeedparser/planetfeedparser.py>`_


Usage
-----
::

    $ ./planetfeedparser.py [LINK] [OPTION](optional)

Link must be like: `link1 <http://planet.fedoraproject.org/rss10.xml>`_ or `link2 <http://planet.fedoraproject.org/rss20.xml>`_

Options available are: -l or --link, to display the links to blogposts


How to execute code
-------------------

Run the above script like::

    $ ./planetfeedparser.py http://planet.fedoraproject.org/rss10.xml -l

or::

    $ python planetfeedparser.py http://planet.fedoraproject.org/rss20.xml


Example output
--------------

Here example output is given below::

    sudip@sudip-mint planetfeedparser $ (master) python planetfeedparser.py http://planet.fedoraproject.org/rss10.xml --link

    1: Post Title: Converting LibreOffice dialogs to .ui format, 300 conversions milestone
            Author: Caolán McNamara
             Link: http://blogs.linux.ie/caolan/2013/07/15/converting-libreoffice-dialogs-to-ui-format-300-conversions-milestone/

    2: Post Title: The GNOME pants are still alive?
            Author: Thomas Vander Stichele
            Link: http://thomas.apestaart.org/log/?p=1559

    3: Post Title: How XMir and Mir fit together
            Author: Matthew Garrett
            Link: http://mjg59.dreamwidth.org/26254.html

    4: Post Title: Linux init-systems
            Author: Daniel Pocock
            Link: http://danielpocock.com/linux-init-systems

    5: Post Title: Fedora 20 kommt ohne SendMail
            Author: Fedora-Blog.de
            Link: http://feedproxy.google.com/~r/Fedora-blogde/~3/rAjpi5VdAhQ/

    6: Post Title: Week-end hacks
            Author: Bastien Nocera
            Link: http://www.hadess.net/2013/07/week-end-hacks.html
