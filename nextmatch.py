#!/usr/bin/env python

import sys
from subprocess import *
import re

I3MSG = '/usr/bin/i3-msg';

##
# @brief Returns the tree of all windows
#
# @return Giant string with window properties
def get_tree():
    p1 = Popen([I3MSG, "-t", "get_tree"], stdout=PIPE)
    i3input = str(p1.communicate()[0])
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    return i3input

##
# @brief Search for the given expresssion in a name field
#
# @param i3input Raw tree information
# @param expr Search expression (partial regex, matching name)
#
# @return pair of (current id, dictionary of matching windows)
def search_window(i3input, expr):
    count   = 0
    current = -1
    targets = list()
    split_re = re.compile('"id":')

    # ignore 0 width windows, save whether the image is focused
    search_re = re.compile('([0-9]*).*focused":(false|true).*'\
            '"geometry":{.*?"width":(?!0).*"name":.*'+expr, \
            flags=re.IGNORECASE)

    sections = split_re.split(i3input);
    for idset in sections:
        results1 = search_re.search(idset)
        if results1 != None:
            wid = int(results1.group(1))
            targets.append(wid)
            if results1.group(2) == 'true':
                current = wid
            count = count + 1

    #if no matchs were found, do nothing
    if len(targets) == 0:
        return (-1, [])

    #sort the matching windows by id
    targets.sort()

    return (current, targets)

##
# @brief Get the next selected window, cycling through if the current window is
# a match and there are mutliple
#
# @param current ID of the currently focued window
# @param selected Array of (int) ids for selected window(s)
#
# @return
def cycle_selected(current, selected):
    #if the choice is a window type that has multiple values, then pick the next
    #from the current, in order of id
    if current in selected:
        selected.sort();
        pos = list.index(selected, current);
        ii = (pos + 1)%len(selected)
    else:
        ii = 0

    if __debug__:
        print (current,selected)

    return selected[ii]

# @brief Focus the window with the specified id
#
# @param jumpid (int) id of window to jump to
def focus_window(jumpid):
    if __debug__:
        print([I3MSG, '[con_id="%i"] focus'%jumpid])

    p1 = Popen([I3MSG, '[con_id="%i"] focus'%jumpid])


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        exit(0)
    i3input = get_tree()
    current, matches = search_window(i3input, sys.argv[1])
    next_selected = cycle_selected(current, matches)
    focus_window(next_selected)

