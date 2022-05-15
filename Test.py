import unittest
import core
import pandas as pd
from pandas.testing import assert_frame_equal


class MyTestCase(unittest.TestCase):
    def test_elements(self):
        base_test = 'store_base_2.json'
        b = core.Shop(base_test)
        self.assertEqual(b.check_number_of_product('apple'), 20)
        self.assertEqual(b.check_price_of_product('orange'), 3)

    def test_load_to_pandas(self):
        base_test = 'store_base_2.json'
        b = core.Shop(base_test)
        d = [{"name":"apple","number":20,"price":2},
             {"name":"orange","number":10,"price":3},
             {"name":"pear","number":15,"price":4},
             {"name":"melon","number":4,"price":3}]
        df = pd.DataFrame(data=d)
        testd = df.set_index("name")
        assert_frame_equal(testd, b.check_status())

    def test_write_to_json(self):
        base_test = 'store_base_2.json'
        b = core.Shop(base_test)
        self.assertEqual(b.buy_product('apple',2),'/apple/20/2/18/')
        b.add_number_of_product(2,'apple')



if __name__ == '__main__':
    unittest.main()
