
=============
userfinder v1
=============

The assignment was

1. To write a command *greet*, which will say Hi! to user. Solution: Imported *getpass* module. It did the rest

2. To write a command *stock [NASDAQ]*, which will show the current share price of given NASDAQ symbol. Solution: Imported *sharevalue* module, which was our previous assignment. So just used it. I am too lazy to write same code again.

Code
----

.. code:: python
    :number-lines:

    from cmd2 import Cmd
    from getpass import getuser
    from sharevalue import share

    __version__ = '0.1'

    class Application(Cmd):
        """
        The main Application class

        """

        def __init__(self):
            Cmd.__init__(self)

        def do_hello(self, line):
            print "Hello:", line

        def do_sayit(self, line):
            print "Python Rocks!"

        def do_greet(self, line):
            print "Hi! %s" %(getuser())

        def do_stock(self, line):
            share(line)

    if __name__ == '__main__':
        app = Application()
        app.cmdloop()

Link to code
------------

`psh.py <https://github.com/iamsudip/dgplug/blob/master/myshellv1/psh.py>`_



How to execute code
-------------------

Run the above script like::


    $ python psh.py


Example output
--------------

Here example output is given below::

    (Cmd) (virt0)sudip@sudip-mint virtual $  python psh.py
    (Cmd) stock GOOG
    Fetching recent share value of GOOG

    Current share price of company GOOG: 915.60

    (Cmd) (virt0)sudip@sudip-mint virtual $  python psh.py
    (Cmd) greet
    Hi! sudip
