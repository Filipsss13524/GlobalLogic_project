import pandas as pd
import json


class Shop:

    def __init__(self,data):
        self.date = data
        with open(self.date, 'r') as f:
            data_p = json.loads(f.read())
        df_list = pd.json_normalize(data_p, record_path=['data'])

        self.df_list = df_list.set_index("name")

    def check_status(self):
        return self.df_list

    def check_number_of_product(self, product):
        return self.df_list.loc[product]['number']

    def check_price_of_product(self, product):
        return self.df_list.loc[product]['price']

    def write_new_price(self, price, product):
        self.df_list.loc[product]['price'] = price
        self.df_list.to_json(path_or_buf = self.date,
                             orient="table")

    def write_new_number(self, num, product):
        self.df_list.loc[product]['number'] = num
        self.df_list.to_json(path_or_buf = self.date,
                             orient="table")

    def show_list_if_product(self):
        lst = []
        for i in range(len(self.df_list.index)):
            lst.append(self.df_list.index[i])
        return lst

    def add_number_of_product(self, add_num, product):
        initial_amount = self.check_number_of_product(product)
        final_state = initial_amount + add_num
        self.write_new_number(final_state, product)
        return f"/{product}/{initial_amount}/{add_num}/{final_state}/"

    def buy_product(self, product, buy_amount):
        initial_amount = self.check_number_of_product(product)
        final_state = initial_amount - buy_amount
        self.write_new_number(final_state,product)
        return f"/{product}/{initial_amount}/{buy_amount}/{final_state}/"



