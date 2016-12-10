from bs4 import BeautifulSoup
from urllib2 import urlopen

start_day = input("input start day, if you want see from 11/01 then type \"20161101\" :")

for i in range(32):
    try:
        html = urlopen("http://kamenoko.chobi.net/blog/data/2016/11/%d.txt"%start_day)
        file = open("commet_%d"%start_day, "w")
        for line in html:
            file.write(line)
        file.close()
    except :
        print(start_day)
        print("today is not the day")
    start_day = start_day + 1
