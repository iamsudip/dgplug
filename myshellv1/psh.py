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
