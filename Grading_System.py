def writefile():
    fileobject = open("student.csv","w")

    flag = "y"
    while (flag == "y"):
        student = {}
        studentName = input("Please enter the student Name: ")
        student["name"] = studentName
        subjectFlag = "y"
        subjects = []
        # taking the inputs for marks
    # validation logic
        totalMarks = 0
        while (subjectFlag == "y"):
            subject = {}
            subjectName = (input("Please enter the name of the subject: "))
            marks = int(input("enter the marks for the subject: "))
            subject["name"] = subjectName
            subject["marks"] = marks
            subjects.append(subject)
            totalMarks = totalMarks+marks
            subjectFlag = input("do you have any other subject data y/n")

            student["totalMarks"] = totalMarks
        print(" The total marks of the student would be ", totalMarks)

# percentage of the total marks
        percentageMarks = (totalMarks/300)*100
        student["percentageMarks"] = percentageMarks
        student["subjects"] = subjects
        students = [student]
        
        if (percentageMarks < 30):
            print(" The student have failed")
            print(" grade : F")
        elif (percentageMarks < 60):

            print("Grade D")

        elif (percentageMarks < 80):

            print("grade A")
        else:
            print("grade E")

        flag = input("do you have any other student data y/n")

    print(students)
    
    fileobject.writelines(str(students))
    
writefile()