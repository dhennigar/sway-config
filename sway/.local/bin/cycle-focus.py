#!/bin/python

# cycle-focus.py

# Author: Daniel Hennigar

import i3ipc

i3 = i3ipc.Connection()
current = i3.get_tree().find_focused()
stack = [con for con in current.workspace() if con.name != None]
stack.sort(key = lambda con: (con.rect.y, con.rect.x))

if len(stack) > 1:
    for i in range(0, len(stack)):
        if stack[i].id == current.id:
            if stack.index(stack[i]) == stack.index(stack[-1]):
                i3.command("[con_id=" + str(stack[0].id) + "] focus")
            else:
                i3.command("[con_id=" + str(stack[i + 1].id) + "] focus")
