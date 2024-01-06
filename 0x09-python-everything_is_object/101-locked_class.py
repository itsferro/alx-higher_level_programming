#!/usr/bin/python3

class LockedClass:
    """
    This is a locked class that restricts attribute assignment to only 'first_name'.

    Attributes:
        __slots__ (list): A list specifying the allowed attributes of the class.

    Methods:
        __init__(): Initializes an instance of the LockedClass.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initializes an instance of the LockedClass.

        Example:
            obj = LockedClass()
        """
        pass
