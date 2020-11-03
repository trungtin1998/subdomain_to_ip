#!/usr/bin/env python
import requests
import os
import sys

f = open(sys.argv[1], "r")

for lines in f:
    lines = lines.rstrip("\n")
    if lines == "":
        break
    s = os.popen("nslookup " + lines).read()
    if (s.find("server can't find") == -1):
    	for l in s.split('\n'):
    		if (l.find("127.0.0.53") == -1 and l.find("Non-authoritative answer") == -1 and l != ''):
    			print l
    	print ""