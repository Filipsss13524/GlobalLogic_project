from time import sleep
import sys
from os import system
import core


def menu(args):
    while True:
        print('Hello what would you like to do?')
        number =int(input("Choose:"
                        "\n 1 Check shop status "
                        "\n 2 Check number of product"
                        "\n 3 Check price of product"
                        "\n 4 Buy a product"
                        "\n 5 Add number of product"
                        "\n 6 Close the application"))

        n = 'store_base.json'
        shop = core.Shop(n)
        if number == 1:
            sleep(1)
            system("cls")
            print(shop.check_status())
        elif number == 2:
            sleep(1)
            system("cls")
            product = str(input('Select a product'))
            print(shop.check_number_of_product(product))
        elif number == 3:
            sleep(1)
            system("cls")
            product = str(input('Select a product'))
            print(shop.check_price_of_product(product))
        elif number == 4:
            sleep(1)
            system("cls")
            product = str(input('Select a product:'))
            buy_amount = int(input('Choose quantity:'))
            shop.buy_product(product, buy_amount)
        elif number == 5:
            sleep(1)
            system("cls")
            product = str(input('Select a product:'))
            number = int(input('Choose quantity:'))
            shop.add_number_of_product(number, product)
        elif number == 6:
            sys.exit(0)
        else:
            print('Choose other number')

    return 0


def main(args):
    menu(args)

    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))