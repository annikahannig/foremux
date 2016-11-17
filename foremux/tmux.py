
"""
Tmux wrapper
"""

import subprocess

def split_v():
    """Split tmux screen vertically"""
    subprocess.call(['tmux', 'split-window', '-h'])



class Layout(object):
    """Define a tmux layout"""

    def apply(self):
        """Send tmux commands"""
        pass




