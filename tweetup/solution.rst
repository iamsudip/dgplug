
==============
tweetup v0.1.4
==============

The name is tweetup but unfortunately I do not like/use twitter so it works on facebook. The script can update text status also with the previous one(uploading a pic with description).

Code
----

.. code:: python
    :number-lines:

    #!/usr/bin/env python
    import fbconsole
    import argparse
    import os
    import sys

    flag_path = 0
    flag_desc = 0

    def update_it(status_update):
        '''
        function to update text status
        '''

        fbconsole.post('/me/feed', {'message': status_update})

    def post_it(path, desc):
        '''
        function to post a image with or without description
        '''

        if desc == 1:
            fbconsole.post('/me/photos', {'source':open(args.file), 'message':args.description})
        else:
            fbconsole.post('/me/photos', {'source':open(args.file)})

    parser = argparse.ArgumentParser(description = 'Update your facebook status')
    parser.add_argument("-f", "--file", type = str,
                    help = "Path to file to upload")
    parser.add_argument("-d", "--description", type = str, 
                    help = "Give the description of the file")
    parser.add_argument("-p", "--post", type = str, 
                    help = "Give the status update to post")
    args = parser.parse_args()


    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins']
    fbconsole.authenticate()

    if args.file:
        if os.path.exists(args.file):
            flag_path = 1
            if args.description:
                flag_desc = 1
        else:
            print "File does not exist"
            sys.exit(-1)
        post_it(flag_path, flag_desc)

    if args.post:
        update_it(args.post)

    fbconsole.logout()
    sys.exit(0)


Installation procedure
----------------------

::

    $  sudo pip install -i https://testpypi.python.org/pypi tweetup

will do the job.

Link to code
------------

You can check the code `here <https://github.com/iamsudip/dgplug/blob/master/tweetup/tweetup>`_

How to upload a pic?
--------------------

The command is::

    $  tweetup -f <path_to_image> -d <descrption>

The above will upload a picture with the given description.
You can upload a picture without a description too. For this do::

    $  tweetup -f <path_to_image>

Notes
-----

When you give the command for the very first time in your computer it will open your default browser window. It will ask you to login. Authorize the application and then set up the settings for this application and all done.

Usage
-----

::

    (virt3)sudip@sudip-mint $  tweetup -h
    usage: tweetup.py [-h] [-f FILE] [-d DESCRIPTION] [-p POST]

    Update your facebook status

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  Path to file to upload
      -d DESCRIPTION, --description DESCRIPTION
                            Give the description of the file
      -p POST, --post POST  Give the status update to post

    (virt3)sudip@sudip-mint $  tweetup -f /home/sudip/fb.jpg -d "It was awesome"

    (virt3)sudip@sudip-mint $  tweetup -p "Updated status via fbconsole"

