#!/usr/bin/env python

"""
Procfile launcher:
Read procfile, split windows, launch procs
"""

import sys
import os

import tmux

from procfile import Procfile


def _print_usage():
    """Show commandline options"""
    print("foremux [-f Procfile] [start, stop]")
    print("""
        Options:

            -f Procfile    specify a Procfile (e.g. for development)

        Commands:

            start          launch the Procfile
            stop           stop all services
      """)


def _parse_args(argv):
    """Parse commandline options"""
    params = {
        'command': 'start',
        'filename': 'Procfile',
    }

    # Handle commands
    if 'stop' in argv:
        params['command'] = 'stop'
    elif 'help' in argv or '--help' in argv:
        params['command'] = 'usage'

    # Handle options
    if '-f' in argv:
        params['filename'] = argv[argv.index('-f')+1]

    return params


def _launch_procfile(pfile):
    """Split screens, run commands"""
    # Prepare layout
    tmux.split_n(len(pfile.procs))

    for i, proc in enumerate(pfile.procs):
        tmux.run_command(proc.command, i)


def _kill_procfile(pfile):
    """Shutdown all services"""
    for _ in pfile.procs:
        tmux.shutdown_pane()


def main():
    """Get Procfile, split windows, launch procs"""
    params = _parse_args(sys.argv)

    if params['command'] == 'usage':
        _print_usage()
        sys.exit(0)

    filename = params['filename']
    if not os.path.isfile(filename):
        print("Procfile not found.")
        sys.exit(-1)

    # Load and parse Procfile
    pfile = Procfile(filename)

    # Handle commands
    if params['command'] == 'start':
        _launch_procfile(pfile)
    else:
        _kill_procfile(pfile)



if __name__ == '__main__':
    main()
