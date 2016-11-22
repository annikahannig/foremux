"""
Read a procfile and return list of procs.
"""

import re
from foremux.proc import Proc

class Procfile(object):
    """Handle a Procfile"""

    # Identify a proc line and match name and command
    PROC_RE = re.compile(r'(\w+):(.*)')

    def _parse_proc(self, line):
        """
        Test if the line is a proc description,
        identified by a <name>: <command> pair.
        """
        match = self.PROC_RE.match(line)
        if not match:
            return None

        return Proc(*[m.strip() for m in match.groups()])


    def _read_procs(self, lines):
        """Get procfile procs"""
        return [p for p in (self._parse_proc(l) for l in lines)
                if p is not None]


    def _read_meta(self, lines):
        """Get meta comments, like layout"""
        return []


    def _read_procfile(self, filename):
        """Read Procfile and return content"""
        with open(filename, 'r') as f:
            lines = [l.strip() for l in f]
            return lines


    def __init__(self, filename):
        """Read and parse procfile"""
        content = self._read_procfile(filename)
        self.procs = self._read_procs(content)
        self.meta = self._read_meta(content)
