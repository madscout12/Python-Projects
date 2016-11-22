from unittest import TestCase
from Numbers.pi import piN
import math
import random


class TestPi_N(TestCase):
    def test_digits(self):
        n = random.randrange(1, 10)
        self.assertEquals('{0:.{1}f}'.format(math.pi, n), '{0:.{1}f}'.format(piN(n), n))

if __name__=='__main__':
    TestCase.main()
