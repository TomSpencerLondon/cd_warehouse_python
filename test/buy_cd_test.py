import unittest




class BuyCdTest(unittest.TestCase):
    def test_buy_cd_in_stock(self):
        cd = CompactDisc(10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == '__main__':
    unittest.main()
