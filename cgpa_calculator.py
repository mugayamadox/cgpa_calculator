"""
    Written by: MUGAYA MADOX 
    Student NO.:24007001

"""
#CGPA CALCULATOR
def cgpaCalc():
    #course units
    course_units = []
    print()
    print("Enter the course units one at a time")
    print("+------------------------------------------------+")
    for i in range(0,4):
        course_units.append(input("enter course unit: "))
    #handle course credits and marks
    course_marks = []
    course_credits = []
    print()
    print("Marks and Credit Units")
    print("+------------------------------------------------+")
    for i in range(0,4):
        course_marks.append(float(input("Enter marks for, "+course_units[i]+": ")))
        course_credits.append(float(input("Enter credit unit for, "+course_units[i]+": ")))
    course_grades = []
    grade_points = []
    #assign grades and equivalent grade points
    for i in range(0,4):
        if course_marks[i] >= 90:
            grade = "A"
            points = 5
        elif course_marks[i] >= 80:
            grade = "B"
            points = 4
        elif course_marks[i] >= 70:
            grade = "C"
            points = 3
        elif course_marks[i] >= 60:
            grade = "D"
            points = 2
        elif course_marks[i] >= 50:
            grade = "E"
            points = 1
        else:
            grade = "F"
            points = 0
        course_grades.append(grade)
        grade_points.append(points)
    #calculate cgpa
    gpa = []
    for i in range(0,4):
        gpa.append(grade_points[i] * course_credits[i])      
    cgpa = (sum(gpa))/sum(course_credits)
    return round(cgpa, 2)
    
#BASIC ARITHMETIC CALCULATOR
def basicCalc(student_n):
    print("Basic Calculator operations")
    print("+------------------------------------------------+")
    print(f"student number is: {student_n}")
    digits = student_n[-2:]
    first = int(digits[0])
    second = int(digits[1])
    print(f"{first} + {second} = {first + second}")
    print(f"{first} - {second} = {first - second}")
    print(f"{first} X {second} = {first * second}")
    if second == 0:
        print(f"{first} / {second}: MathError, Cannot divide by zero")
    else:
        print(f"{first} / {second} = {round(first / second,2)}")


#run program
if __name__ == "__main__":
    #Declare variables to hold student info
    student_name = input("Please enter your name: ")
    student_number = input("Please enter your student number: ")
    #call cgpa calculator
    cgpa = cgpaCalc()
    print("+------------------------------------------------+")
    print(f"CGPA for {student_name} is: {cgpa}")
    print()
    basicCalc(student_number)
    
