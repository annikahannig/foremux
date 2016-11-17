
# Foremux - A Procfile launcher using tmux

Launch your `Procfile` in a tmux session.


## Installation

To install this littel tool, just clone this repository and run

    python setup.py install


## Usage

In you project directory just run `foremux`.

You can specify a different Procfile as first argument.

_CAVEAT:_ `foremux` will split and reorder all panes and will
run the commands as specified in the Procfile.

Running `foremux` in an empty window is advised.



