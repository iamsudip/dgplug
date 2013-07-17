#!usr/bin/env python

from sys import exit

def display_users():
    """
    Function to display those usernames who can login
    """
    #Opening the file /etc/passwd in read mode
    f = open('/etc/passwd', 'r')
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
