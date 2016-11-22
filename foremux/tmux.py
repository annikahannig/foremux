"""
Tmux wrapper
"""

import subprocess
import time

def split_v():
    """Split tmux screen vertically"""
    subprocess.call(['tmux', 'split-window', '-v'])


def split_h():
    """Split tmux screen horizontally"""
    subprocess.call(['tmux', 'split-window', '-h'])


def select_pane(pane_id):
    """Go to pane in split layout"""
    subprocess.call(['tmux', 'select-pane', '-t', pane_id])

def list_panes():
    """Returns a list of panes"""
    res = subprocess.check_output(['tmux', 'list-panes'])
    return res.strip().decode().split('\n')


def send_keys(keys, pane_id=0):
    """Send command sequence to pane"""
    subprocess.call(['tmux', 'send-keys', '-t', str(pane_id)] + keys)


def run_command(command, pane_id=0):
    """Execute command in pane"""
    send_keys([command, 'Enter'], pane_id)


def shutdown_pane(pane_id=0):
    """Terminates the running command and sends EOF"""
    pane_count = len(list_panes())

    send_keys(['C-c', 'C-d'], pane_id=pane_id)
    while len(list_panes()) >= pane_count:
        time.sleep(0.2)


def next_layout():
    """Reorder panes with next layout"""
    subprocess.call(['tmux', 'next-layout'])


def previous_layout():
    """Reorder panes with previous layout"""
    subprocess.call(['tmux', 'previous-layout'])


def select_layout(preset):
    """
    Select a specific layout. Default layouts
    include:
        main-vertical
        main-horizontal
        even-vertical
        even-horizontal
        tiled
    """
    subprocess.call(['tmux', 'select-layout', preset])


def tiled_layout():
    """Shortcut for tiled window"""
    select_layout('tiled')


def split_n(panes):
    """Split and reorder panes"""
    for i in range(1, panes):
        split_h()

    # Reorder panes
    tiled_layout()

