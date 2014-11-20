i3-wm-scripts
=============

i3 Window Manager Scripts

These are python scripts that read/write to i3 using i3-msg. By using regular expressions it is possible to 
search for windows with particular names and jump to them. 

Dependencies: i3, i3-msg (distributed with i3), dmenu

There are 4 scripts: nextmatch.py, nextfind.py, goto, mark

### nextmatch.py

Syntax: nextmatch.py <regex>

This script takes one regular expression input e.g. '(fire|chrom)' and searches for that name in the list of
available windows. If there is a match then it jumps to the match. If you are already at a match it goes to the
next match (or stays if there is only one)

### nextfind.py

Syntax: nextfind.py

This script works similarly to the previous but takes no arguments and instead
provides a dmenu list of arguments. If you select one a window that is active
and there are multiple with the same name then it jumps to the next one,
otherwise it stays at the current.

### mark/goto
These scripts mark and jump to a specified script. I actually rarely use them,
because I prefer the other two. Basically you can mark the current window by
calling mark (or binding it them using the key-combination). Then you can get a
list of marked windows (similar to nextfind.py, but only with marked windows
included) to jumpt to.

### Install
To install just put the scripts in your path, or bind the scripts in you config
file. I installed mine in ~/bin/ 

### Example Config:
```
bindsym $mod+q exec python ~/bin/nextmatch.py vim # cycle through vim sessions
bindsym $mod+w exec python ~/bin/nextmatch.py '(chromium|firefox)' # cycle through browsers using regex

bindsym $mod+e exec python ~/bin/nextfind.py # use dmenu to select an open window

bindsym $mod+m exec ~/bin/mark # mark a window width a name
bindsym $mod+g exec ~/bin/goto # select from marked windows with dmenu
```

