#!/usr/bin/env python
import argparse
import os
import sys
import json


def make_json(path_to_file, filename=False, date=False):
    '''
    Function to convert .log files to json data with desired name and date.
    '''
    with open(path_to_file) as data:
        content = {"filename" : filename, "date" : date, "content" : data.read()}
    if os.path.exists('database.json') == False:
        temp = {"logs" : {"log_id_%s" %date : content}}
        with open("database.json", 'a') as jdata:
            json.dump(temp, jdata)
    else:
        with open("database.json", 'r') as jdata:
            temp = json.load(jdata)
            temp["logs"]["log_id_%s" %date] = content
        with open("database.json", 'w') as jdata:
            json.dump(temp, jdata)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Creates json database')
    parser.add_argument("path", help = "Give the path to log")
    parser.add_argument("-n", "--filename", type = str,
                        help = "Give the name to log")
    parser.add_argument("-d", "--date", type = str, 
                        help = "Give the date to add")
    args = parser.parse_args()

    if os.path.exists(args.path):
        make_json(args.path, args.filename, args.date)
    else:
        print "File does not exist"
        sys.exit(-1)
    sys.exit(0)
