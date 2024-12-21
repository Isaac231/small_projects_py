#Number Sorter  |   Rating (8/10)

print("Welcome to number sorter!")
def append_nums():
    num_list = []
    while True:
        user_input = input('Enter a Number or "done": ')

        try:
            if isinstance(user_input, str) and user_input.lower() == 'done':
                if not num_list:
                    print('\nThe list is still empty!\n')
                    continue

                if len(num_list) > 1 and not all(x == num_list[0] for x in num_list):
                    return num_list
                else:
                    print("\nThe list size should at least be higher than 1 and have different values!\n")
                    continue

            if int(user_input):
                num_list.append(int(user_input))
        except ValueError:
            print("\nInvalid Input! Enter a number or 'done only!\n")

def sort_nums():
    finalized_list = append_nums()
    print("Your current list:")
    print(finalized_list)
    while True:
        print('\nWould you like to sort it Ascending or Descending?')
        user_input = input("Input(ascend | descend): ").lower()
        if user_input == 'ascend':
            sorted_list = sorted(finalized_list)
        elif user_input == 'descend':
            sorted_list = sorted(finalized_list, reverse=True)
        else:
            print('\nInput should be "ascend" or "descend" only!')
            continue

        print("\nList successfully sorted!")
        print('Previous List:')
        print(finalized_list)

        print('\nSorted List:')
        print(sorted_list)
        break

if __name__ == '__main__':
    sort_nums()



