import unittest
from algopy.mergesort import *

class MergesortTestCase(unittest.TestCase):
    """ Tests for mergesort algorithms """

    def test_mergesort(self):
        # (seed = 183182)
        # Give the array that results after the first 4 exchanges when
        # selection sorting the following array:
        desc = 'MERGESORT'
        a = map(int, "13 16 40 60 19 70 71 47 12 67".split() )
        array_history = []
        sort(a, array_history)
        print desc, "RESULT", a
        # TBD: Implement array history visualization
        # prt_array_history(array_history)
        # show_array_history(desc, array_history)
        print

if __name__ == '__main__':
    unittest.main()
