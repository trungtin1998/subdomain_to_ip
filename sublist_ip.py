#!/usr/bin/env python
import requests
import os
import sys

os.system('sublist -d %s -o out.log' % (sys.argv[1]))

f = open("out.log", "r")
if (len(sys.argv) >= 3):
	fw = open(sys.argv[2], "w")

for lines in f:
    lines = lines.rstrip("\n")
    if lines == "":
        break
    s = os.popen("nslookup " + lines).read()
    if (s.find("server can't find") == -1):
    	for l in s.split('\n'):
    		if (l.find("127.0.0.53") == -1 and l.find("Non-authoritative answer") == -1 and l != ''):
    			print(l)
    			if (len(sys.argv) >= 3):
    				fw.write("%s\n"%l)
    	print("")
    	if (len(sys.argv) >= 3):
    		fw.write("\n")


f.close()
fw.close()
os.system('rm out.log')
