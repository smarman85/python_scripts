import os, datetime, time

file = os.path.getmtime("quote.txt")
print "file modified time: " + time.str(datetime.datetime.fromtimestamp(file))
print "file time stamp: " + str(datetime.datetime.fromtimestamp(file))

now = time.strftime("%Y-%m-%d")
print now
