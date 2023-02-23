"""
Contains the Increment class.

This modules creates an object that can easily be incremented
or decremented (or even reset) for carrying values over a
large range of code. Vaguely similar to iota in GoLang.
"""


class Increment:
    """
    Creates an object that increments when simple operations are used
    """

    def __init__(self, start=0):
        self._start = start
        self._val = start

    def __str__(self):
        return str(self._val)

    def __pos__(self):
        """
        Increment the value by 1 and return the value
        """
        self._val += 1
        return self._val

    def __neg__(self):
        """
        Decrement the value by 1 and return the value
        """
        self._val -= 1
        return self._val
    
    def __invert__(self):
        """
        Reset back to start and return the value
        """
        self._val = self._start
        return self._val
    
    @property
    def val(self):
        """
        Return the current value for assignment operators
        """
        return self._val
        

if __name__ == "__main__":
    inc = Increment()
    
    print("Initial value: ", inc)
    
    print("Increment value: ", +inc)
    
    print("Decrement value: ", -inc)

    print("Decrement value: ", -inc)
    
    print("Reset value: ", ~inc)