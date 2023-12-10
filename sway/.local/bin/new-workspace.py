#!/bin/python

# new-workspace.py
# Author: Daniel Hennigar

import i3ipc
import argparse

parser = argparse.ArgumentParser(
    prog = "new-workspace.py",
    description = "finds and opens a new i3/sway workspace.",
)
parser.add_argument("-s", "--send", action = "store_true")
args = parser.parse_args()

ipc = i3ipc.Connection()
ws_nums = [ws.num for ws in ipc.get_workspaces()]
new_ws = [n for n in range(1, 10) if n not in ws_nums][0]

if ipc.get_tree().find_focused():
    if args.send:
        ipc.command("move to workspace " + str(new_ws))
    ipc.command("workspace " + str(new_ws))
