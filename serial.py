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

    def __init__(self,start):
        "Initialize start and initial values"
        self.start = start - 1
        self.initial = start - 1

    def generate(self):
        "Increment start by 1 and return it"
        self.start += 1

        return self.start

    def reset(self):
        "Reset start to initial value"
        self.start = self.initial

