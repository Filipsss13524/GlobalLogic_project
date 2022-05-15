from time import sleep
import sys
from os import system
import core


def menu(base):
    while True:
        print('Hello what would you like to do?')
        number = int(input("Choose:"
                           "\n 1 Check shop status "
                           "\n 2 Check number of product"
                           "\n 3 Check price of product"
                           "\n 4 Buy a product"
                           "\n 5 Add number of product"
                           "\n 6 Close the application"))

        shop = core.Shop(base)
        if number == 1:
            sleep(1)
            system("cls")
            print(shop.check_status())
            input("If you want to back click enter")
            sleep(1)
            system("cls")
        elif number == 2:
            sleep(1)
            system("cls")
            product = str(input('Select a product'))
            print(shop.check_number_of_product(product))
            input("If you want to back click enter")
            sleep(1)
            system("cls")
        elif number == 3:
            sleep(1)
            system("cls")
            product = str(input('Select a product'))
            print(shop.check_price_of_product(product))
            input("If you want to back click enter")
            sleep(1)
            system("cls")
        elif number == 4:
            sleep(1)
            system("cls")
            product = str(input('Select a product:'))
            buy_amount = int(input('Choose quantity:'))
            print(shop.buy_product(product, buy_amount))
            input("If you want to back click enter")
            sleep(1)
            system("cls")
        elif number == 5:
            sleep(1)
            system("cls")
            product = str(input('Select a product:'))
            number = int(input('Choose quantity:'))
            print(shop.add_number_of_product(number, product))
            input("If you want to back click enter")
            sleep(1)
            system("cls")
        elif number == 6:
            sys.exit(0)
        else:
            print('Choose other number')


def main(args):
    base = 'store_base.json'
    menu(base)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
