#!/usr/bin/env python

"""
Procfile launcher:
Read procfile, split windows, launch procs
"""

import sys
import os

import tmux

from procfile import Procfile

def main():
    """Get Procfile, split windows, launch procs"""
    filename = 'Procfile'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    if not os.path.isfile(filename):
        print("Procfile not found.")
        sys.exit(-1)

    pfile = Procfile(filename)

    # Prepare layout
    tmux.split_n(len(pfile.procs))

    for i, proc in enumerate(pfile.procs):
        tmux.run_command(proc.command, i)


if __name__ == '__main__':
    main()
