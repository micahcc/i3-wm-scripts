#!/bin/python

from sys import argv, exit
from subprocess import *
import re

I3MSG = '/usr/bin/i3-msg';

def get_tree():
    p1 = Popen([I3MSG, "-t", "get_tree"], stdout=PIPE)
    i3input = str(p1.communicate()[0])
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    search_window(i3input)

def search_window(i3input):
    count   = 0
    current = -1
    targets = list()

    sections = re.split('"id":', i3input);
    for idset in sections:
        results1 = re.search('([0-9]*).*focused":(false|true).*"geometry":{.*?"width":(?!0).*"name":.*'\
		    +argv[1], idset, flags=re.IGNORECASE)
        if results1 != None:
	        targets.append(results1.group(1))
	        if results1.group(2) == 'true':
		        current = count
	        count = count + 1

    #if no matchs were found, do nothing
    print(targets)
    print(current)
    if len(targets) == 0:
        exit(1)

    #sort the matching windows by id then go to the next if we are currently on one
    targets = [int(val) for val in targets]
    targets.sort()
    focus_window(current,targets)

def focus_window(current,targets):
    print([I3MSG, '[con_id="'+str(targets[(current+1)%len(targets)])+'"] focus'])
    p1 = Popen([I3MSG, '[con_id="'+str(targets[(current+1)%len(targets)])+'"] focus'])

if __name__ == '__main__':
    if(len(argv) != 2):
        exit(0)
    get_tree()
