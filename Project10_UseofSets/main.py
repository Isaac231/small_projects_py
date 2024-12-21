#Use of Sets | Rating(10/10)

def validate_sets(message):
    set_values = set()
    while True:
        user_input = input(f'{message} | "back": ').capitalize()
        if user_input.strip().lower() == 'back':
            if not set_values:
                print('Unable to execute action! Set is still empty!')
                continue
            break
        
        if not user_input:
            print("Error: Cannot enter without inserting a value!")
            continue
        
        if user_input in set_values:
            print(f"Error: {user_input} is already in the set!")
            continue
            
        set_values.add(user_input)
        
    return set_values
    
def print_common_difference(set1, set2):
    print(f"Common Elements: {set1 & set2}")

def print_unique_elements(set1, set2):
    if not (set1 - set2):
        print('No unique value to Set 1.')
    else:
        print(f"Unique to Set 1: {set1 - set2}")
    
    if not (set2 - set1):
        print('No unique value to Set 2.')
    else:
        print(f"Unique to Set 2: {set2 - set1}")

def print_combined_set(set1, set2):
    print(f"Combined Set: {set1 | set2}")

def main():
    first_set = validate_sets('Enter value set 1')
    second_set = validate_sets('Enter value set 2')
    
    print('\n' + '=' * 50)
    print_common_difference(first_set, second_set)
    print_unique_elements(first_set, second_set)
    print_combined_set(first_set, second_set)
    print('=' * 50)
    
if __name__ == '__main__':
    main()