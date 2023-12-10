#!/bin/bash

DATE=$(date "+%a %b %d, '%y")
TIME=$(date "+%H:%M")

notify-send "$TIME" "$DATE"

