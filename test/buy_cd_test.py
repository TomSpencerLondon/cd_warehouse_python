import unittest


class CompactDisc(object):
    def __init__(self, initial_stock):
        self._stock_count = initial_stock

    def get_stock_count(self):
        return self._stock_count

    def buy(self, quantity):
        self._stock_count -= quantity


class BuyCdTest(unittest.TestCase):
    def test_buy_cd_in_stock(self):
        cd = CompactDisc(10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == '__main__':
    unittest.main()
