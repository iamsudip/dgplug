mount
=====

In this assignment we will display the contents of *mounts* file which is located in /proc directory

.. listing: https://github.com/iamsudip/dgplug/blob/master/mount/mount.py python
    #!/usr/bin/env python
    file=open("/proc/mounts") #Opening the mounts file.
    for x in file:
            print x, #Iterating through its contents line by line.
            file.close() #Closing the file

Solution to the above problem is `mount.py <https://github.com/iamsudip/dgplug/blob/master/mount/mount.py>`_

**Hint**: Run the above program like::

    $ sudo python mount.py
