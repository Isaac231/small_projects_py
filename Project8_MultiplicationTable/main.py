# Multiplication Table | Rating(9/10)

def set_value(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                break
            print("Invalid Input! Please input a positive value!")
        except ValueError:
            print("Invalid Value! Please input a numerical value!")
    return value

def main():
    rows = set_value("Set row size: ")
    cols = set_value("Set column size: ")

    with open(f'files/Multiplication Table ({rows}x{cols}).txt', 'w') as file:
        print(f'\nMultiplication Table ({rows}x{cols})')
        print('===========================')
        for i in range(1, rows + 1):
            for j in range(1, cols+1):
                result = i * j
                file.write(f'{result}\t')
                print(result, end='\t')

            file.write('\n')
            print()
        print('===========================\n')

if __name__ == '__main__':
    main()
