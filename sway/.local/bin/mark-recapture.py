#!/bin/python

# mark-recapture.py

# Author: Daniel Hennigar

import i3ipc
import argparse

parser = argparse.ArgumentParser(
    prog = "mark-recapture.py",
    description = "mark windows for quick recall."
)
parser.add_argument("-n", "--new", action = "store_true")
parser.add_argument("-b", "--bring", action = "store_true")
args = parser.parse_args()

ipc = i3ipc.Connection()
marks = ipc.get_marks()
current_ws = ipc.get_tree().find_focused().workspace()

if "mark" in marks and not args.new:
    if args.bring:
        ipc.command("[con_mark=mark] move to workspace " + current_ws.name)
    ipc.command("[con_mark=mark] focus")
else:
    ipc.command("[con_id=__focused__] mark --add 'mark'")        

        
