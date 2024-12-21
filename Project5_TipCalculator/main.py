#Tip Calculator   |   Rating (9/10)

from sys import exit

total_balance = 5000
product_list = ['Apple', 'Banana', 'Orange']
product_price = {product_list[0] : 20, product_list[1] : 10, product_list[2] : 15}
cart = {}
total_amount = 0

def user_options(tot_amount):
    global total_amount
    total_amount = tot_amount
    while True:
        print(f'\nWhat to do?\t\t\t\tBalance: {total_balance}\tTotal Amount: {tot_amount if tot_amount != 0 else '--'}')
        print('1. Select Item\n2. Open Cart\n3. Proceed Order')

        user_choice = int(input('\nYour Choice: '))
        if user_choice == 1:
            cart_products(tot_amount)
        elif user_choice == 2:
            open_cart(tot_amount)
        elif user_choice == 3:
            proceed_transaction(tot_amount)
        else:
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

def cart_products(tot_amount):
    while True:
        print("\n\t\t\tFruit Store\nPlease select the items that you want to purchase")
        for num, fruit_list in enumerate(product_list, start=1):
            print(f'{num}. {fruit_list}\t\t\t\tPrice: {product_price[fruit_list]}')

        print('\n0. Go Back')
        user_choice = int(input('\nYour Choice: '))

        if user_choice == 0:
            return

        if user_choice not in range(1, (len(product_list) + 1)):
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

        quantity = int(input(f'How many {product_list[user_choice - 1]} do you want: '))
        if product_list[user_choice - 1] in cart:
            cart[product_list[user_choice - 1]] += quantity
        else:
            cart[product_list[user_choice - 1]] = quantity

        tot_amount += (product_price[product_list[user_choice - 1]] * quantity)
        print('\n--------------------\nAdded to the cart!\n--------------------')

        user_options(tot_amount)

def open_cart(tot_amount):
    if len(cart) == 0:
        print('\n--------------------\nThe cart is empty!\n--------------------')
        return

    while True:
        print('\nCart List:')
        for num, (key, value) in enumerate(cart.items(), start=1):
            print(f'{num}. {key}\t\t\tAmount: {value}\t\t\tPrice: {product_price[key] * value}')

        print(f'\t\t\t\t\t\t\t\t\tTotal Amount: {tot_amount}')
        print('\nWhat to do?')
        print('1. Remove an Item\n2. Go back\n3. Proceed Order')
        user_choice = int(input('\nYour Choice: '))

        if user_choice == 1:
            tot_amount = remove_item_cart(tot_amount)
        elif user_choice == 2:
            return tot_amount
        elif user_choice == 3:
            proceed_transaction(tot_amount)
        else:
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

def remove_item_cart(tot_amount):
    while True:
        print("\nSelect an item to remove:")
        for num, (key, value) in enumerate(cart.items(), start=1):
            print(f'{num}. {key}\t\t\tAmount: {value}')

        print(f'\n0. Go back')
        user_choice = int(input('\nYour Choice: '))

        if user_choice == 0:
            return tot_amount

        if user_choice not in range(1, len(cart) + 1):
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

        list_to_remove = list(cart.keys())[user_choice -1]
        while True:
            print(f'\nAre you sure you want to remove {list_to_remove}?')
            print('1. Yes\n2. No')

            user_choice = int(input('\nYour Choice: '))
            if user_choice == 1:
                tot_amount -= product_price[list_to_remove] * cart[list_to_remove]
                cart.pop(list_to_remove)
                print(f'\n---------------------------------------\nRemoved {list_to_remove} from the list.\n---------------------------------------')
                if len(cart) == 0:
                    user_options(tot_amount)

                break
            elif user_choice == 2:
                break
            else:
                print('\n--------------------\nInvalid Input!\n--------------------')
                continue

def proceed_transaction(tot_amount):
    if len(cart) == 0:
        print('\n-----------------------------------------\nYou haven\'t ordered anything yet.\n-----------------------------------------')
        return

    while True:
        print(f"\nYour total amount is {tot_amount}\t\t\t\tBalance: {total_balance}")
        payment = int(input('\nInsert amount of payment: '))

        if total_balance < tot_amount:
            print('\n-------------------------\nGoing back to the selection!\nThe total amount exceeds your balance.\n-------------------------')
            user_options(tot_amount)

        if payment < tot_amount:
            print('\n--------------------\nInsufficient Payment!\n--------------------')
            continue
        elif payment > total_balance:
            print('\n------------------------\nPayment is over the Balance!\n------------------------')

        if payment == total_balance:
            confirm_payment(tot_amount, payment, total_balance)

        print("\nWould you like to tip?")
        print('1. Yes\n2. No')
        user_choice = int(input("\nYour Choice: "))

        if user_choice == 1:
            tip = user_tipping(tot_amount)
        elif user_choice == 2:
            confirm_payment(tot_amount, payment, total_balance)
            break
        else:
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

        confirm_payment(tot_amount, payment, total_balance, tip)

def user_tipping(tot_amount):
    while True:
        print("\nWould you like to tip in certain amount or a percentage based on your order total amount?")
        print('1. Tip certain amount\n2. Tip based on percentage of total amount\n\n0. Cancel')
        user_choice = int(input("\nYour Choice: "))

        if user_choice == 0:
            return 0

        if user_choice == 1:
            tip = int(input('\nInsert amount of tip: '))
        elif user_choice == 2:
            tip = input('\nInsert percentage of tip: ')
        else:
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

        if isinstance(tip, str) and str(tip).endswith('%'):
            if int(tip[:-1]):
                tip = int(tip[:-1])

        if isinstance(tip, str):
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

        if user_choice == 2:
            tip = round(tot_amount * (tip / 100))

        if tot_amount + tip > total_balance:
            print('\n---------------------------------------\nThe total amount and tip exceeds your balance.\n---------------------------------------\n')
            continue

        return tip

def confirm_payment(tot_amount, payment, balance, tip=0):
    total = tot_amount + tip
    balance -= payment + tip
    change = payment - tot_amount
    while True:
        print(f'\nYour Amount: {tot_amount}')
        print(f'Your Payment: {payment}')
        print(f'Your Tip: {tip if tip != 0 else 'Did not tip.'}')
        print(f'Total: {total} {'(+Tip)' if tip > 0 else ''}')

        print('\nConfirm Payment?')
        print('1. Yes\n2. No')
        user_choice = int(input("\nYour Choice: "))

        if user_choice == 2:
            proceed_transaction(tot_amount)

        if user_choice == 1:
            balance += change
            print('\n======================================\n')
            print('Successfully purchased:')
            for num, (key, value) in enumerate(cart.items(), start=1):
                print(f'{num}. {key}\t\t\tAmount: {value}')
            print('\n======================================\n')
            print(f'Change: {change}')
            print(f'Remaining Balance: {balance}')
            print('\n======================================\n')

            print('\nThank you for your purchase!')
            exit()

        else:
            print('\n--------------------\nInvalid Input!\n--------------------')
            continue

def main():
    while True:
        try:
            user_options(total_amount)
        except ValueError:
            print('\n--------------------\nInvalid Value!\n--------------------')

if __name__ == '__main__':
    main()



    
