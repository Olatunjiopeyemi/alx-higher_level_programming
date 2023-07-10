#!/usr/bin/python3

"""
Defines a class MyList.
"""


class MyList(list):
    """A subclass inherited from `list`."""
    def print_sorted(self):
        """Prints list in sorted order."""
        print(sorted(self))
