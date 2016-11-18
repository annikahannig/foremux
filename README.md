
# Foremux - A Procfile launcher using tmux

Launch your `Procfile` in a tmux session.


## Installation

To install this littel tool, just clone this repository and run

    python setup.py install


## Usage

In you project directory just run `foremux`.

More advanced stuff:

    Options:

        -f Procfile    specify a Procfile (e.g. for development)

    Commands:

        start          launch the Procfile
        stop           stop all services


**CAVEAT:** `foremux` will split and reorder all panes and will
run the commands as specified in the Procfile.

Running `foremux` in an empty window is advised.

