import unittest


class CompactDisc(object):
    def __init__(self, initial_stock):
        pass

    def get_stock_count(self):
        return 5

    def buy(self, quantity):
        pass


class BuyCdTest(unittest.TestCase):
    def test_buy_cd_in_stock(self):
        cd = CompactDisc(10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == '__main__':
    unittest.main()
