#!/usr/bin/env python
f=open("/proc/mounts") #Opening the mounts file.
for x in f:
    print x, #Iterating through its contents and printing it line by line.
f.close() #Closing the file
