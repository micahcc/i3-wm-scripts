#!/bin/python

from sys import exit
from subprocess import *
import re

I3MSG = '/usr/bin/i3-msg'
DMENU = '/usr/bin/dmenu'

def get_tree():
    p1 = Popen([I3MSG, "-t", "get_tree"], stdout=PIPE)
    i3input = str(p1.communicate()[0])
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    get_named_windows(i3input)

def get_named_windows(i3input):
    count = 0
    current = -1
    targets = dict()

    sections = re.split('"id":', i3input);
    for idset in sections:
	    results1 = re.search('([0-9]*).*focused":(false|true).*"geometry":{.*?"width":(?!0).*"name":"(.*?)"', idset)
	    if results1 != None:
		    if results1.group(2) == "true":
			    current = int(results1.group(1))

		    if targets.get(results1.group(3)) == None:
			    targets[results1.group(3)] = []
		    targets[results1.group(3)].append(results1.group(1))

    if len(targets) == 0:
	    exit(1)

    number_of_matching_window(i3input,targets,current)

def number_of_matching_window(i3input,targets,current):
    #modify keys to indicate the number of matching windows
    options = dict()
    for key in targets:
        print(key)
        newkey = "(" + str(len(targets[key])) + ") " + key
        options[newkey] = targets[key]

    p1 = Popen([DMENU, '-i'], stdout=PIPE, stdin=PIPE)
    concat = '\n'.join(options.keys())
    i3input = p1.communicate(bytes(concat,'UTF-8'))[0]
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.

    #get the choice
    print(i3input)
    key = i3input.decode('UTF-8').rstrip('\n');
    print(key)
    print(options[key])

    #if the choice is a window type that has multiple values, then pick the next
    #from the current, in order of id
    numtargs = [int(val) for val in options[key]]
    print(current)
    print(numtargs)
    if current in numtargs:
        numtargs.sort();
        pos = list.index(numtargs, current);
        ii = (pos + 1)%len(numtargs)
    else:
        ii = 0

    focus_window(ii,numtargs)

def focus_window(ii,numtargs):
    print([I3MSG, '[con_id="'+str(numtargs[ii])+'"] focus'])
    p1 = Popen([I3MSG, '[con_id="'+str(numtargs[ii])+'"] focus'])

if __name__ == '__main__':
    get_tree()
