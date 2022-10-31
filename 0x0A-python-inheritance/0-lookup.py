#!/usr/bin/python3

"""
File: 0-lookup.py
Desc: This module conatins a single function called lookup.
Author: Oduoronyina
Date Created: Tuesday, November 01 2022
"""


def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object.
    """
    return (dir(obj))
