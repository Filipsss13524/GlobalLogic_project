import unittest
import core


class MyTestCase(unittest.TestCase):
    def test_list(self):
        base_test = 'store_base_2.json'
        b = core.Shop(base_test)
        self.assertEqual(b.check_number_of_product('apple'), 20)
        self.assertEqual(b.check_price_of_product('orange'), 3)

    def test_write(self):
        base_test = 'store_base_2.json'
        b = core.Shop(base_test)
        self.assertEqual(b.buy_product('apple',2),'/apple/20/2/18/')
        b.add_number_of_product(2,'apple')


if __name__ == '__main__':
    unittest.main()
