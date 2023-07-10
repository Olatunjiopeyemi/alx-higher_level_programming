#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """Invert a class MyInt"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
