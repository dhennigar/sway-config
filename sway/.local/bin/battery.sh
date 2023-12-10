#!/bin/bash

CAPACITY=$(cat /sys/class/power_supply/BAT0/capacity)
STATUS=$(cat /sys/class/power_supply/BAT0/status)

notify-send "$CAPACITY%" "$STATUS"
