mount v3
========

In this assignment we will display the contents of *mounts* file which is located in /proc directory

:: listing `mount.py <https://github.com/iamsudip/dgplug/blob/master/mount/mount.py>`_::
    
    
    #!/usr/bin/env python

    f=open("/proc/mounts")                                           #Opening the mounts file.

    def func(inp):                                                   #Function to separate ine inputs
        a, b, c, d, e, f=inp                                         #Separating inputs as different words
        return "%s on %s type %s (%s)" % (a, b, c, d)                #Returning the value as user need

    for x in f:                                                      #Iterating through each line
        s=x.split(" ")                                               #Spliting words ie using spaces
        print func(s)                                                #Calling func(inp) Printing return value

    f.close()                                                        #Closing the file

**Hint**: Run the above program like::

    $ python mount.py

or::

    $ chmod +x mount.py
    $ ./mount.py
