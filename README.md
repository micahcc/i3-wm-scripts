i3-wm-scripts
=============

i3 Window Manager Scripts

These are python scripts that read/write to i3 using i3-msg. By using regular expressions it is possible to 
search for windows with particular names and jump to them. 

Dependencies: i3, i3-msg (distributed with i3), dmenu

There are 4 scripts: nextmatch, nextfind, goto, mark

### nextmatch

Syntax: nextmatch \<regex\>

This script takes one regular expression input e.g. '(fire|chrom)' and searches for that name in the list of
available windows. If there is a match then it jumps to the match. If you are already at a match it goes to the
next match (or stays if there is only one)

Example Binding:
```
bindsym $mod+q exec python ~/bin/nextmatch vim # cycle through vim sessions
bindsym $mod+w exec python ~/bin/nextmatch '(chromium|firefox)' # cycle through browsers using regex
```
### nextfind

Syntax: nextfind

This script works similarly to the previous but takes no arguments and instead
provides a dmenu list of arguments. If you select one a window that is active
and there are multiple with the same name then it jumps to the next one,
otherwise it stays at the current.

Example Binding:
```
bindsym $mod+e exec python ~/bin/nextfind # use dmenu to select an open window
```

### mark/goto/unmark
These scripts mark and jump to a specified script. I rarely use them,
because I prefer the other two, but they can be useful if you are jumping to a
lot of windows with the same name (like terminals). Basically you can mark the
current window by calling mark (or binding it them using the key-combination).
Then you can get a list of marked windows (similar to nextfind, but only
with marked windows included) to jumpt to. 

Example bindings:
```
bindsym $mod+Shift+grave exec ~/bin/unmark # unmark the current window
bindsym $mod+grave exec ~/bin/mark # mark the current window
bindsym $mod+Tab exec exec ~/bin/goto # get dmenu of marked windows
```

### Install
To install just put the scripts in your path, or bind the scripts in you config
file. I installed mine in ~/bin/, then made the bindings in my config file.

