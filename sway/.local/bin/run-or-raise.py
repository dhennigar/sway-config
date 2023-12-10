#!/bin/python

# run-or-raise.py
# Author: Daniel Hennigar

import i3ipc
import argparse

parser = argparse.ArgumentParser(
    prog = "run-or-raise.py",
    description = "focuses a program if it exists, or launches a new instance."
)
parser.add_argument("-b", "--bring", action = "store_true", default = False)
parser.add_argument("appid")
args = parser.parse_args()

ipc = i3ipc.Connection()
appids = [con.app_id for con in ipc.get_tree().descendants()]

if args.appid in appids:
    if args.bring:
        ws = ipc.get_tree().find_focused().workspace()
        ipc.command("[app_id=" + args.appid + "] move to workspace " + ws.name)
    ipc.command("[app_id=" + args.appid + "] focus")
else:
    ipc.command("exec " + args.appid)
