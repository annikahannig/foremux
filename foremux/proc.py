
class Proc(object):
    """A Proc represents an entry in the procfile"""

    def __init__(self, name, command):
        """Initialize proc"""
        self.name = name
        self.command = command


