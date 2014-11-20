i3-wm-scripts
=============

i3 Window Manager Scripts

These are python scripts that read/write to i3 using i3-msg. By using regular expressions it is possible to 
search for windows with particular names. This makes it much easier to jump to a particular window. 

Dependencies: i3, i3-msg (distributed with i3), dmenu

nextmatch.py <regex>
This script takes one regular expression input e.g. '(fire|chrom)' and searches for that name in the list of
available windows. If there is a match then it jumps to the match. If you are already at a match it goes to the
next match (or stays if there is only one)

nextfind.py
This script works similarly to the previous but creates a dictionary of available windows, complete with repeated names
and presents that list using dmenu. If you select one a window that is active and there are multiple with the same name 
then it jumps to the next one, otherwise it stays at the current.

To install just py the scripts in your path, (I put mine in ~/bin/).

Example usage in my .i3/config file:

#To search for a hardcoded program
I like to be able to jump to a partiuclar program using a single shortcut. This
will cycle through all of the window that match. So for example, to jump to vim
with mod+q, use the following:
```
bindsym $mod+q exec python ~/bin/nextmatch.py vim
```
You can also use a regular expression (see python re library for more on this):
```
bindsym $mod+w exec python ~/bin/nextmatch.py '(chromium|firefox)'
```

#Bind dmenu to search for a particular program:
```
bindsym $mod+e exec python ~/bin/nextfind.py
```

#Bind marking a window:
```
bindsym $mod+m exec ~/bin/mark
```

#Bind jumping to a marked program:
```
bindsym $mod+g exec ~/bin/goto
```

