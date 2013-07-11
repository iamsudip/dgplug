#!/usr/bin/env python

f=open("/proc/mounts")                                           #Opening the mounts file.

def func(inp):                                                   #Function to separate ine inputs
    a, b, c, d, e, f=inp                                         #Separating inputs as different words
    return "%s on %s type %s (%s)" % (a, b, c, d)                #Returning the value as user need

for x in f:                                                      #Iterating through each line
    s=x.split(" ")                                               #Spliting words ie using spaces
    print func(s)                                                #Calling func(inp) Printing return value

f.close()                                                        #Closing the file
