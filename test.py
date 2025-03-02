from createUtils import recursive_split
import unittest

class RecursiveSplitTest(unittest.TestCase):
    def test_normal_two_double_quotes(self):
        line = 'door-NEC-1891-barton,,"Pawtucket/Central Falls - Barton St, Pick-up/Drop-off","Pawtucket/Central Falls - Barton St, Pick-up/Drop-off",,,41.878490,-71.392761,,,,level_ground,2,place-NEC-1891,1,Pawtucket,,,'
        assert recursive_split(line) == ['door-NEC-1891-barton', '', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', '', '', '41.878490', '-71.392761', '', '', '', 'level_ground', '2', 'place-NEC-1891', '1', 'Pawtucket', '', '', '']
    def test_double_quote_second_to_last_idx(self):
        line = 'door-NEC-1891-barton,,"Pawtucket/Central Falls - Barton St, Pick-up/Drop-off","Pawtucket/Central Falls - Barton St, Pick-up/Drop-off",,,41.878490,-71.392761,,,,level_ground,2,place-NEC-1891,1,Pawtucket,,"hello, this is a sentence",'
        assert recursive_split(line) == ['door-NEC-1891-barton', '', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', '', '', '41.878490', '-71.392761', '', '', '', 'level_ground', '2', 'place-NEC-1891', '1', 'Pawtucket', '', 'hello, this is a sentence', '']
    def test_double_quote_last_idx(self):
        line = 'door-NEC-1891-barton,,"Pawtucket/Central Falls - Barton St, Pick-up/Drop-off","Pawtucket/Central Falls - Barton St, Pick-up/Drop-off",,,41.878490,-71.392761,,,,level_ground,2,place-NEC-1891,1,Pawtucket,,,"hello, how are you"'
        assert recursive_split(line) == ['door-NEC-1891-barton', '', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', '', '', '41.878490', '-71.392761', '', '', '', 'level_ground', '2', 'place-NEC-1891', '1', 'Pawtucket', '', '', 'hello, how are you']
    def test_no_quotes(self):
        line = '351,BUS12025-hbt15ns1-Weekday-02,67018534,Bedford Woods Dr via EMD Serono,,0,T351-203,3510110,1,,351-_-0,1'
        assert recursive_split(line) == line.strip().split(',')
    def test_single_double_quote(self):
        line = 'door-NEC-1891-barton,,"Pawtucket/Central Falls - Barton St, Pick-up/Drop-off",Pawtucket/Central Falls - Barton St,,,41.878490,-71.392761,,,,level_ground,2,place-NEC-1891,1,Pawtucket,,,'
        assert recursive_split(line) == ['door-NEC-1891-barton', '', 'Pawtucket/Central Falls - Barton St, Pick-up/Drop-off', 'Pawtucket/Central Falls - Barton St', '', '', '41.878490', '-71.392761', '', '', '', 'level_ground', '2', 'place-NEC-1891', '1', 'Pawtucket', '', '', '']
