import unittest


def count_endzeros(bignumber):
    count = 0
    num = bignumber
    while num % 10 == 0:
        count += 1
        num = num // 10
    return count


class TrailingZeroTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_nozero(self):
        self.assertEqual(count_endzeros(1324324), 0)

    def test_onezero(self):
        self.assertEqual(count_endzeros(232140), 1)

    def test_fivezero(self):
        self.assertEqual(count_endzeros(12000200000), 5)

    def test_lotsozero(self):
        self.assertEqual(
            count_endzeros(100000000000000000000000000), 26)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
