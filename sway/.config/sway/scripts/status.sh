#!/bin/bash

battery_percent=$(cat /sys/class/power_supply/BAT0/capacity)
battery_status=$(cat /sys/class/power_supply/BAT0/status)
date_formatted=$(date "+%y-%m-%d %H:%M")

echo "$battery_status: $battery_percent% | $date_formatted  "
