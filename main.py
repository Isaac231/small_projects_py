# Grade Calculator

while True:
    try:
        student_score = int(input('Enter your score: '))
        
        if not 0 <= student_score <= 100:
            print("\n--------------------------------\nInvalid Score!\n--------------------------------\n")
            continue
        
        if student_score <= 20:
            remark = 'E'
        elif student_score <= 40:
            remark = 'D'
        elif student_score <= 60:
            remark = 'C'
        elif student_score <= 80:
            remark = 'B'
        else:
            remark = 'A'
        
        print(f"Your grade: {remark}\n{'You Passed!' if student_score > 40 else 'You fail..'}")
        break
    except ValueError as e:
        print("\n--------------------------------\nInvalid Input! Please Try Again\n--------------------------------\n")
        continue