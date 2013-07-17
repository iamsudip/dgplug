
=============
userfinder v1
=============

The assignment was to display all the users who can login. Recommended to use the python module *pwd* but instead of using the module I have done in it different way, output wise one can say both are same but I have opened */etc/passwd* manually which is not recommended. I just wanted to post a differnt solution.

So, here I considered that login users means those users who have a home directory. For that we are checking if any home directory for any user present or not. The code snippet is given below.


Code
----

.. code:: python
    :number-lines:

    #!usr/bin/env python

    from sys import exit

    def display_users():
        """
        Function to display those usernames who can login
        """
        #Opening the file /etc/passwd in read mode
        f = open('/etc/passwd')
        #Accessing the instance 'f' line by line
        for i in f:
            #Splitting the string
            data = i.split(':')
            #Finding the name of the home directories if present then print
            if data[5].find('/root') != -1 or data[5].find('/home') != -1:
                print data[0]
        #Closing the file handle
        f.close()

    if __name__ == '__main__':
        display_users()
        exit(0)

Link to code
------------

`userfinderv1.py <https://github.com/iamsudip/dgplug/blob/master/userfinder/userfinderv1.py>`_


How to execute code
-------------------

Run the above script like::


    $ python userfinderv1.py


Example output
--------------

Here example output is given below::

    sudip@sudip-mint userfinder $ (master) python userfinderv1.py
    root
    syslog
    usbmux
    saned
    sudip

