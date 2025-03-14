#!/usr/bin/bash
setxkbmap latam
setxkbmap -layout latam
# xrandr --output eDP1 --primary --scale 0.8x0.8
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xautolock -time 5 -locker "lock" &
clipmenud &
emacs --daemon &
# redshift-gtk &
nm-applet &
urxvtd -q -f -o &
walp & 
