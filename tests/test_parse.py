#!/usr/bin/env python

from cogent.util.unit_test import TestCase, main
from greengenes.parse import parse_column, parse_gg_summary_flat, \
        parse_invariants
from greengenes.util import GreengenesRecord
from StringIO import StringIO

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2012, Greengenes"
__credits__ = ["Daniel McDonald"]
__license__ = "GPL"
__version__ = "1.5.0-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"
__status__ = "Development"
    
class ParseTests(TestCase):
    def setUp(self):
        pass

    def test_parse_invariants(self):
        """Parse the invariants file"""
        exp = [('inv_a','NNNNAANNANNTTNGNANNNAAANN',10),
               ('inv_b','AANNANNANANANANNTTATTANNN',13)]
        obs = parse_invariants(StringIO(invariants))    
        self.assertEqual(obs,exp)

    def test_parse_column(self):
        """Parse existing records"""
        recs = StringIO(existing_records)
        exp = set(['abc','def','xyz','foo','bar'])
        obs = parse_column(recs)
        self.assertEqual(obs,exp)

    def test_parse_gg_summary_flat(self):
        """Parse the gg summary files from flat_files.py"""
        exp = [GreengenesRecord({'prokMSA_id':'1', 'ncbi_acc_w_ver':'xyzf'}),
               GreengenesRecord({'prokMSA_id':'25', 'ncbi_acc_w_ver':'abcd',
                                 'country':'australia'}),
               GreengenesRecord({'prokMSA_id':'50', 'ncbi_acc_w_ver':'223xx'})]
        obs = list(parse_gg_summary_flat(StringIO(gg_summary)))

        self.assertEqual(obs,exp)

invariants = """>inv_a
NNNNAANNANNTTNGNANNNAAANN
>inv_b
AANNANNANANANANNTTATTANNN
"""

existing_records = """#accession\tprokMSA_id
abc\t10
def\t20
xyz
foo\t
bar\t30
"""

gg_summary = """#prokMSA_id\tncbi_acc_w_ver\tcountry
1\txyzf\t
25\tabcd\taustralia
50\t223xx\t
"""

if __name__ == '__main__':
    main()
