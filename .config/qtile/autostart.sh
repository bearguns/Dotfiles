#!/bin/bash
picom &
my_wallpaper=(cat ~/.cache/wal/wal) &
nitrogen --set-auto $my_wallpaper &

