i3-wm-scripts
=============

i3 Window Manager Scripts

These are python scripts that read/write to i3 using i3-msg. By using regular expressions it is possible to 
search for windows with particular names. This makes it much easier to jump to a particular window. Just
what you always dreamed!

Example usage in my .i3/config file:

bindsym $mod+q exec python ~/bin/nextmatch.py vim

bindsym $mod+w exec python ~/bin/nextmatch.py '(chromium|firefox)'

bindsym $mod+e exec python ~/bin/nextfind.py