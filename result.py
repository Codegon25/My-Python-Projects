results = {}

def display_results():
    print("Student \t Score \t Grade")
    for key in results:
        print("{}\t{}\t{}".format(key,results.get(key)))

while True:
    options = int(input("1. Add result \n 2. Change result \n 3. Clear result \n 4. View result \n 5. Exit page \n Enter your choice "))
    if options == 1:
        name = str(input("Enter student's name: "))
        score = int(input("Enter student's score: "))
        grade = str(input("Enter student's grade: "))
        results[name] = score, grade
    elif options == 2:
        student_score_to_edit = str(input("Enter Student's name: "))
        if student_score_to_edit in results:
            score = input("Change score to: ")
            grade = input("Change grade to: ") 
            results[student_score_to_edit] = score, grade
        else:
            print("Student's name not found")
    elif options == 3:
        students_data = str(input("Enter Student's name: "))
        if students_data in results:
            del_data = str(input("Are you sure you want to delete the score? \n y/n"))
            if del_data == 'Y' or del_data == 'y':
                results.pop(students_data[score])
            else:
                print("Student's data is still intact")  
    elif options == 4:
        if not results:
            print("No results found")
        else:
            display_results()       
    elif options == 5:
        break        