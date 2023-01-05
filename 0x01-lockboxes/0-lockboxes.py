#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""

unlocked_boxes = {}


def unlock_box(key, my_boxes):
    """
    unlock a box with the provided key
    """

    for i in my_boxes[key]:
        if unlocked_boxes[i]:
            continue
        unlocked_boxes[i] = True
        unlock_box(i, my_boxes)


def canUnlockAll(boxes):
    """
    check if all boxes can be opened
    """

    length = len(boxes)

    for i in range(0, length):
        unlocked_boxes[i] = False

    unlock_box(0, boxes)

    for i in range(0, length):
        if unlocked_boxes[i] is False and i != 0:
            return False

    return True
