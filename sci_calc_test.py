from sci_calc import *

class sci_calc(math):

    def test_find_sqrt(self):
        math.find_sqrt(100) == 10

    def test_find_ceil(self):
        math.find_ceil(12.2) == 13