#Simple Student Database Manager | Rating (8.5/10)
from sys import exit
import csv
import os
from math import floor


def get_student_age(message):
    age = int(input(message))
    if age < 18:
        raise ValueError('Invalid Age! Valid age is 18 and above!')
    return age

def get_student_grade(message):
    grade = int(input(message))
    if not (75 <= grade <= 100):
        raise ValueError('Invalid Grade! Valid grade is 75-100!')
    return grade

def select_student_name(std_database):
    while True:
        get_std_name = input('Select student name or "back" to return: ').capitalize()
        if get_std_name.lower() == 'back':
            return False
        
        if get_std_name not in std_database.keys():
            print_result("Student name not found.")
            continue
        else:
            return get_std_name

def print_result(message):
    print('\n' + '=' * 50)
    print(message)
    print('=' * 50, '\n')
            
def get_yes_or_no(message):
    while True:
        user_input = input(message + ' (yes/no): ').strip().lower()
        
        if user_input in ['yes', 'no']:
            return user_input
    
def add_student_data():
    student_database = {}
    while True:
        name = input("\nAdd student Name: ").capitalize()
        
        try:
            age = get_student_age("Add student age: ")
            grade = get_student_grade("Add student grade: ")
            
            student_database[name] = [age, grade]
            user_input = get_yes_or_no('Would you like to add student data again?')
            
            if user_input == 'no':
                break
                
        except ValueError as e:
            print(f'Error: {e}')
            
    return student_database

def view_student_data(std_database):
    if not std_database:
        print_result("\n\t\t\tThe Database is empty!\n")
        return
    
    longest_name = max(std_database.keys(), key=len)
    
    print('=' * (len(longest_name) + 22))
    print(" " * floor(len(longest_name)/2), "Name", " " * floor(len(longest_name)/2), " Age", " " * 4, "Grade")
        
    for index, (key, value) in enumerate(std_database.items(), start=1):
        print(f'{index}. {key} ', end=' ' * ((len(longest_name) - len(key)) if len(key) < len(longest_name) else 0))
        
        for data in value:
            print(' ' * 3, data, end=' ' * 3)
        print()
        
    print('=' * (len(longest_name) + 22), '')

def edit_student_data(std_database):
   while True:
        if check_database_items(std_database):
            return
        
        print("\nEdit Student's Data")
        view_student_data(std_database)
        
        get_std_name = select_student_name(std_database)
        if not get_std_name:
            return std_database
            
        while True:
            user_input = input(f"Edit {get_std_name} (Name/Age/Grade/Cancel): ").strip().lower()
            if user_input == 'cancel':
                break
                
            if user_input == 'name':
                new_name = input("Enter new name: ").capitalize()
                if new_name in std_database.keys():
                    print_result(f'The name of {new_name} already exists in the database!')
                    continue
                
                print_result(f"Successfully changed {get_std_name}'s name to {new_name}!")
                student_values = std_database[get_std_name]
                std_database.pop(get_std_name)
                std_database[new_name] = student_values
                get_std_name = new_name

            elif user_input == 'age':
                new_age = get_student_age("Enter new age: ")
                std_database[get_std_name][0] = new_age
                
                print_result(f"Successfully changed {get_std_name}'s age to {new_age}!")
            elif user_input == 'grade':
                new_grade = get_student_grade("Enter new grade: ")
                std_database[get_std_name][1] = new_grade
                
                print_result(f"Successfully changed {get_std_name}'s grade to {new_grade}!")

def delete_student_data(std_database):
    while True:
        if check_database_items(std_database):
            return
        
        print("\nDelete Student's Data")
        view_student_data(std_database)
        
        get_std_name = select_student_name(std_database)
        if get_std_name.lower() == 'back':
            return std_database
        
        while True:
            user_input = input(f"Are you sure you want to delete {get_std_name}'s data? (Delete/Cancel): ").strip().lower()
            if user_input == 'cancel':
                break
                
            if not user_input == 'delete':
                continue
            
            del std_database[get_std_name]
            print_result(f"Successfully removed {get_std_name} from the database!")
            
            if not std_database:
                return std_database
            break
            
def load_record(file_path):
    load_db = {}
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            
            print_result("A database record has been detected. Loading datas..")
            for row in reader:
                key = row[0]
                value = [int(row[1]), int(row[2])]
                load_db[key] = value
            
    except FileNotFoundError:
        print_result("No record found.")
        return
    
    return load_db
        
def save_record(file_path, std_database):
    if check_database_items(std_database):
        return
    
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Age', 'Grade'])
        
        for key, value in std_database.items():
            csv_writer.writerow([key] + value)
            
        print_result(f'Successfully saved student records to: {file_path}!')
    
    while True:
        user_input = get_yes_or_no('Would you like to exit the system?')
        
        if user_input == 'yes':
            exit()
        else:
            return
        
def check_student_exist(new_std_rd, std_database):
    print('\n' + '=' * 65)
    for key, value in new_std_rd.items():
        if key not in std_database:
            std_database[key] = value
            print(f'Successfully added {key} to the database!')
        else:
            print(f'Update Failure: {key}\'s data already exists in the database!')
    print('=' * 65)
    return std_database

def check_database_items(std_database):
    if not std_database:
        print_result('\nUnable to take action! The database is empty!\n')
        return True
        
def main():
    folder_path = 'database'
    file_name = '/College Student Database.csv'
    os.makedirs(folder_path, exist_ok=True)
    filepath = folder_path + file_name
    
    print("Checking for student records..")
    student_database = load_record(filepath)
    
    print('Welcome to College Student Database Manager.')
    if not student_database:
        student_database = add_student_data()
    
    #Navigation Selector
    while True:
        user_input = input("\nActions (View/Add/Edit/Delete/Save): ").strip().lower()
        if user_input == 'view':
            print("\nViewing Student Database:")
            view_student_data(student_database)
        elif user_input == 'add':
            new_std_record = add_student_data()
            student_database = check_student_exist(new_std_record, student_database)
        elif user_input == 'edit':
            student_database = edit_student_data(student_database)
        elif user_input == 'delete':
            student_database = delete_student_data(student_database)
        elif user_input == 'save':
            save_record(filepath, student_database)
            
            
if __name__ == '__main__':
    main()