# #Calculator | Rating (9/10)

operators = ['+', '-', '*', '/']

def prompt_restart():
    while True:
        user_input = input('\nWould you like to calculate again? (yes | no): ').lower()
        if user_input == 'yes':
            return True
        elif user_input == 'no':
            print('Thank you for using the program!')
            return False
        else:
            print('\n------------------------------\nInvalid Input!\n------------------------------\n')


def calculate():
    while True:
        try:
            first_num = float(input('Enter first number: '))
            operator = input('Enter an operator (+ | - | * | /): ')
            
            if operator not in operators:
                print('\n------------------------------\nInvalid Operator!\n------------------------------\n')
                continue
            
            second_num = float(input('Enter second number: '))
            
            if operator == '+':
                output = first_num + second_num
            elif operator == '-':
                output = first_num - second_num
            elif operator == '*':
                output = first_num * second_num
            else:
                output = first_num / second_num
            
            print(f'\n{int(first_num) if first_num == int(first_num) else first_num} {operator} '
                  f'{int(second_num) if second_num == int(second_num) else second_num} = '
                  f'{int(output) if output == int(output) else output}')
            
            if not prompt_restart():
                break
        except ValueError:
            print('\n------------------------------\nInvalid Input!\n------------------------------\n')

calculate()
