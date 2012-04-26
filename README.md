i3-wm-scripts
=============

i3 Window Manager Scripts

These are python scripts that read/write to i3 using i3-msg. By using regular expressions it is possible to 
search for windows with particular names. This makes it much easier to jump to a particular window. Just
what you always dreamed!

Dependencies: i3, i3-msg (distributed with i3), dmenu

nextmatch.py <regex>
This script takes one regular expression input e.g. '(fire|chrom)' and searches for that name in the list of
available windows. If there is a match then it jumps to the match. If you are already at a match it goes to the
next match (or stays if there is only one)

nextfind.py
This script works similarly to the previous but creates a dictionary of available windows, complete with repeated names
and presents that list using dmenu. If you select one a window that is active and there are multiple with the same name 
then it jumps to the next one, otherwise it stays at the current.

Example usage in my .i3/config file:

bindsym $mod+q exec python ~/bin/nextmatch.py vim

bindsym $mod+w exec python ~/bin/nextmatch.py '(chromium|firefox)'

bindsym $mod+e exec python ~/bin/nextfind.py