
==========
dup_images
==========

The assignment was to find all the duplicate images from the given direcories as commandline arguments.

*dup_images* can find any type of duplicate files not only the images.


Code
----

.. code:: python
    :number-lines:

    #!/usr/bin/env python
    import os
    import sys
    import hashlib

    data = {}  # A dictionary to keep all data.
    arranged_data = {}  # A dictionary to keep data in an arranged way.

    def hash_it(directory):
        """Function to generate md5 hash
        """
        for path, sub_directories, files in os.walk(directory):
            # Picks each file as 'filename' and generating hash.
            for filename in files:
                path_to_file = os.path.join(path, filename)
                # Appends file as key and generated md5 hash as value to 'data'.
                data[str(path_to_file)] = hashlib.md5(open(str(path_to_file)).read()).hexdigest()

    def find_duplicates():
        """Function to find duplicate files
        """
        # Iterates through each key and value at a time.
        for pair in data.items():
            if pair[1] not in arranged_data.keys():
                # If new hash value found appends it to 'arranged_data' as key.
                arranged_data[pair[1]] = []
            # Keeps all the files as a list in value to the same hash(key).
            arranged_data[pair[1]].append(pair[0])

        # Iterates through the new dictionary, the files which are duplicates keeps them as a list.
        dup_list = [files for hashes, files in arranged_data.items() if len(files) > 1]

        # A simple counter to count no. of duplicate files.
        count = 1
        # Iterates through each list and prints them.
        for files in dup_list:
            print str(count) + '.'
            for dup_file in files:
                print dup_file
            count += 1

    if __name__ == '__main__':
        for i in range(1,len(sys.argv)):
            if os.path.exists(sys.argv[i]):
                hash_it(sys.argv[i])
            else:
                print "Wrong path: %s" %(sys.argv[i])
        find_duplicates()
        sys.exit(0)

Link to code
------------

You canfind it `here. <https://github.com/iamsudip/dgplug/blob/master/dup_images/dup_images>`_

How to execute code
-------------------

Run the above script like::

    $ ./dup_images <PATH> <PATH> <PATH>

Example output
--------------

Here example output is given below::

    sudip@sudip-mint dup_images $  pwd
    /home/sudip/tmp/code/dup_images
    sudip@sudip-mint dup_images $  ls -R
    .:
    dup_images  new1  new2  new3

    ./new1:
    fb.jpg  fdgdg.txt

    ./new2:
    ds.bmp  newsub1  wfdss.jpg

    ./new2/newsub1:
    fb.jpg  newsub2

    ./new2/newsub1/newsub2:
    dgg.bmp  viewer.py

    ./new3:
    cs.jpg  sdf.png
    sudip@sudip-mint dup_images $  python dup_images /home/sudip/tmp/code/dup_images /asshddk/ahdjd/ddjf
    Wrong path: /asshddk/ahdjd/ddjf
    1.
    /home/sudip/tmp/code/dup_images/new2/newsub1/newsub2/dgg.bmp
    /home/sudip/tmp/code/dup_images/new2/ds.bmp
    2.
    /home/sudip/tmp/code/dup_images/new1/fdgdg.txt
    /home/sudip/tmp/code/dup_images/new2/newsub1/newsub2/viewer.py
    3.
    /home/sudip/tmp/code/dup_images/new2/wfdss.jpg
    /home/sudip/tmp/code/dup_images/new3/cs.jpg
    /home/sudip/tmp/code/dup_images/new1/fb.jpg
    /home/sudip/tmp/code/dup_images/new2/newsub1/fb.jpg

