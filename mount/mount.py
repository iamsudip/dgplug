#!/usr/bin/env python
file=open("/proc/mounts") #Opening the mounts file.
for x in file:
    print x, #Iterating through its contents and printing it line by line.
file.close() #Closing the file
