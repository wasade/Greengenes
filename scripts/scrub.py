#!/usr/bin/env python

from sys import argv
from greengenes.util import greengenes_open as open

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2012, Greengenes"
__credits__ = ["Daniel McDonald"]
__license__ = "GPL"
__version__ = "0.1-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"
__status__ = "Development"

fin = open(argv[1])
fout = open(argv[2],'w')
fcrap = open(argv[2] + '.crap.gz','w')

in_html = False

for l in fin:
    if in_html:
        fcrap.write(l)
        if l.startswith('</html>'):
            in_html = False
    else: 
        if l.startswith('LOCUS'): # incomplete locus line
            if len(l.strip().split()) < 3:
                fcrap.write(l)
                continue
            if l.strip().endswith('11.dtd">'): # bailed query
                fcrap.write(l)
                continue
        elif l.startswith('<html>'):
            fcrap.write(l)
            in_html = True
            continue
        fout.write(l)
fin.close()
fout.close()
fcrap.close()
