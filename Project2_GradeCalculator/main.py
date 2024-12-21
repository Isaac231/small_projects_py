#Grade Calculator Program | Rating (8/10)

while True:
    try:
        student_score = int(input('Enter your score: '))

        if student_score < 0 or student_score > 100:
            print("\n--------------------------------\n")
            print('Invalid Score!')
            print("\n--------------------------------\n")
            continue

        remark: str
        if 0 >= student_score <= 20:
            remark = 'E'
        elif 21 >= student_score <= 40:
            remark = 'D'
        elif 41 >= student_score <= 60:
            remark = 'C'
        elif 61 >= student_score <= 80:
            remark = 'B'
        else:
            remark = 'A'
        print(f"Your grade: {remark}\n{'You Passed!' if student_score > 40 else 'You fail'}")
        break
    except ValueError as e:
        print("\n--------------------------------\n")
        print('Invalid Input! Please Try Again')
        print("\n--------------------------------\n")
        continue
