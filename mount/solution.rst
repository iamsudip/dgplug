mount v2
========

In this assignment we will display the contents of *mounts* file which is located in /proc directory

:: listing `mount.py <https://github.com/iamsudip/dgplug/blob/master/mount/mount.py>`_::
    
    #!/usr/bin/env python
    f=open("/proc/mounts")                       #Opening the mounts file.
    for x in f:
            print x,                             #Iterating through its contents line by line.
    f.close()                                    #Closing the file

**Hint**: Run the above program like::

    $ python mount.py

or::

    $ chmod +x mount.py
    $ ./mount.py
