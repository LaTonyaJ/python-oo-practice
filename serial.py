"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.original = start

    def generate(self):
        """Generate Serial numbers"""
        num = self.start
        num = num + 1
        self.start = num
        return(num - 1)

    def reset(self):
        """Reset Serial to start"""
        return self.original
