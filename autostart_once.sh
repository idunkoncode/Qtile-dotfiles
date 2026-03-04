#!/bin/bash

# Export display env vars so dbus-activated apps can connect to Wayland
dbus-update-activation-environment --all &

# Apply wallpaper using wal
wal -b 282738 -i ~/Wallpaper/Aesthetic2.png &&

# Start picom
picom --config ~/.config/picom/picom.conf &
