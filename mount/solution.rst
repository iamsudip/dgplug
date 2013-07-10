mount
=====

In this assignment we will display the contents of *mounts* file which is located in /proc directory

:: listing::
    
    #!/usr/bin/env python
    f=open("/proc/mounts") #Opening the mounts file.
    for x in f:
            print x, #Iterating through its contents line by line.
    f.close() #Closing the file

Solution to the above problem is `mount.py <https://github.com/iamsudip/dgplug/blob/master/mount/mount.py>`_

**Hint**: Run the above program like::

    $ sudo python mount.py
