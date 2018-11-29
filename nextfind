#!/usr/bin/env python
"""
Tool for jumping to a window by looking through the window names.

Usage:

    nextfind.py [dmenu options]


Too pull up a list of windows in dmenu:

    nextfind.py -sb green -nb red

"""


from sys import exit, argv
from subprocess import *
import re

I3MSG = '/usr/bin/i3-msg'
DMENU = '/usr/bin/dmenu'
DMENU_ARGS = argv[1:]

##
# @brief Returns the giant list of windows in from i3
#
# @return
def get_tree():
    p1 = Popen([I3MSG, "-t", "get_tree"], stdout=PIPE)
    i3input = str(p1.communicate()[0])
    p1.stdout.close()
    return i3input

##
# @brief Gets the list of named windows in stored as a name:[id, id...] dict
#
# @return Current active window (id), dictionary of windows name:[id, id, ...]
def get_named_windows():

    i3input = get_tree()

    count = 0
    current = -1
    windows = dict()
    # ignore 0 width windows, save whether the image is focused
    splitter = re.compile('([0-9]*).*focused":(false|true).*'\
            '"geometry":{.*?"width":(?!0).*"name":"(.*?)"')

    sections = re.split('"id":', i3input);
    for idset in sections:
        results1 = splitter.search(idset)
        if results1 != None:
            if results1.group(2) == "true":
                current = int(results1.group(1))

            if windows.get(results1.group(3)) == None:
                windows[results1.group(3)] = []
            windows[results1.group(3).strip()].append(results1.group(1))

    return (current, windows)


##
# @brief Open dmenu with the current set of all windows so that the user can
# select one
#
# @param windows Dictionary of all windows with name : [ids...]
# @param current ID of current window
#
# @return list of ids for the selected option
def select_window(current, windows):
    #modify keys to indicate the number of matching windows
    options = dict()
    for key in windows:
        if __debug__:
            print(key)

        newkey = "(" + str(len(windows[key])) + ") " + key
        options[newkey] = windows[key]

    p1 = Popen([DMENU, '-i']+DMENU_ARGS, stdout=PIPE, stdin=PIPE)
    concat = '\n'.join(options.keys())
    ret = p1.communicate(bytes(concat,'UTF-8'))[0].decode('UTF-8').rstrip()
    p1.stdout.close()

    selected = [int(i) for i in options[ret]]
    return selected

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

##
# @brief Focus the window with the specified id
#
# @param jumpid (int) id of window to jump to
def focus_window(jumpid):
    if __debug__:
        print([I3MSG, '[con_id="%i"] focus'%jumpid])

    p1 = Popen([I3MSG, '[con_id="%i"] focus'%jumpid])


if __name__ == '__main__':
    current, windows = get_named_windows()
    if not windows:
        sys.exit(0)

    selected = select_window(current, windows)
    if not selected:
        sys.exit(0)

    next_selected = cycle_selected(current, selected)
    focus_window(next_selected)

