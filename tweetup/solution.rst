
=======
tweetup
=======

The name is tweetup but unfortunately I do not like/use twitter so it works on facebook.

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
