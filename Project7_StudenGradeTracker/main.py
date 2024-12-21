# Student Grade Tracker | Rating(9/10)

from sys import exit

def add_students():
    student_list = {}
    while True:
        std_name = str(input('Enter student name: '))

        if std_name in student_list.keys():
            print(f"{std_name} is already in the list!")
            continue

        try:
            std_grade = int(input('Enter student grade: '))
        except ValueError:
            print("Invalid Input! Please enter an integer value!")
            continue

        if not 75 <= std_grade <= 100:
            print("Invalid Grade! Valid Grade value only ranges from 75-100!")
            continue
        student_list[std_name] = std_grade

        while True:
            user_input = input("Would you like to add another student again?(yes/no): ").strip().lower()
            if not (user_input == 'yes' or user_input == 'no'):
                print('Invalid Input! Input should only be "yes" or "no"!')
                continue
            else:
                break

        if user_input == 'yes':
            continue
        else:
            break

    return student_list


def display_student_data(std_list):
    # Display students data
    print('\n====================================================')
    print('Student List:')
    for index, (student, grade) in enumerate(std_list.items(), start=1):
        print(f'{index}. {student}\t\t\tGrade: {grade}')
    print('====================================================\n')

    return std_list


def update_data(std_list):
    while True:
        user_input = input('What would you like to do? (edit/delete/calculate): ').strip().lower()

        if user_input == 'edit':
            std_list = edit_data(std_list)
            display_student_data(std_list)
        elif user_input == 'delete':
            std_list = delete_data(std_list)
            display_student_data(std_list)
        elif user_input == 'calculate':
            calculate_data(std_list)
            display_student_data(std_list)
        else:
            print("Invalid Input! Please try again!")


def edit_data(std_list):
    while True:
        print("\nEDIT STUDENT'S GRADE")
        std_list = display_student_data(std_list)

        user_input = input("Select student's name or Enter \"back\": ")
        if user_input.strip().lower() == 'back':
            break

        if not user_input in std_list.keys():
            print("Invalid Student Name! Please Try Again!")
            continue

        print(f"\nEditing {user_input}'s Grade:")

        try:
            new_std_grade = int(input('Enter student grade: '))
        except ValueError:
            print("Invalid Input! Please enter an integer value!")
            continue

        if not 75 <= new_std_grade <= 100:
            print("Invalid Grade! Valid Grade value only ranges from 75-100!")
            continue
        std_list[user_input] = new_std_grade

        print(f"Successfully edited {user_input}'s grade!")
        display_student_data(std_list)

        while True:
            user_input = input("Would you like to edit student's grade again?(yes/no): ").strip().lower()
            if not (user_input == 'yes' or user_input == 'no'):
                print('Invalid Input! Input should only be "yes" or "no"!')
                continue
            else:
                break

        if user_input == 'yes':
            continue
        else:
            break
    return std_list


def delete_data(std_list):
    while True:
        if not len(std_list):
            print("\n----------------------------------------------------------\n")
            print("No student records longer exists! going back from start.")
            print("\n----------------------------------------------------------\n")
            main()

        print("\nDELETE STUDENT RECORD")
        std_list = display_student_data(std_list)

        user_promt = input("Select student's name or Enter \"back\": ")
        if user_promt.strip().lower() == 'back':
            break

        if not user_promt in std_list.keys():
            print("Invalid Student Name! Please Try Again!")
            continue

        while True:
            user_input = input(f"Are you sure you want to delete {user_promt}'s record? (yes/no): ").strip().lower()
            if not (user_input == 'yes' or user_input == 'no'):
                print('Invalid Input! Input should only be "yes" or "no"!')
                continue
            else:
                break

        if user_input == 'yes':
            del std_list[user_promt]
            print(f"\nSuccessfully deleted {user_promt}'s record from the list!")

    return std_list


def calculate_data(std_list):
    total_grade = 0
    for index, grades in enumerate(std_list.values(), start=1):
        total_grade += grades

    total_average = (total_grade / index)

    highest_grades = max(std_list.values())
    highest_students = (name for name, grade in std_list.items() if grade == highest_grades)

    lowest_grades = min(std_list.values())
    lowest_students = (name for name, grade in std_list.items() if grade == lowest_grades)

    print('\n====================================================')
    print(f"Average Grade of all students: {round(total_average, 2)}")
    print(f'Student/s with highest grade: {', '.join(highest_students)} with {highest_grades}')
    print(f'Student/s with lowest grade: {', '.join(lowest_students)} with {lowest_grades}')
    print('====================================================\n')

    while True:
        user_input = input("Finalize record? (yes/no): ").strip().lower()

        if user_input == 'yes':
            print("Students record has successfully been finalized!")
            print("Thank you for using our system!")
            print("Goodbye!")
            break
        elif user_input == 'no':
            return
        else:
            print('Invalid Input! Input should only be "yes" or "no"!')
            continue

    exit()


def main():
    student_list = add_students()
    while True:
        student_list = display_student_data(student_list)
        update_data(student_list)


if __name__ == '__main__':
    main()
