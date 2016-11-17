
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

    print(pfile.procs)



if __name__ == '__main__':
    main()
