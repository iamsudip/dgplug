#!/usr/bin/env python


from commands import getoutput
import sqlite3
from time import sleep

def load():
    conn = sqlite3.connect('loadavgs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE loadaverages
             (current time, users, loadaverage1min, loadaverage5min, loadaverage15min)''')
    try:
        while True:
            datas = getoutput("uptime")
            data = datas.split(', ')
            data[2] = data[2].split(': ')[1]
            #print data
            c.execute("INSERT INTO loadaverages VALUES (?, ?, ?, ?, ?)", data)
            conn.commit()
            sleep(1)
            print data[2]
    except:
        getoutput("rm -rf loadavgs.db")
        c.close()
