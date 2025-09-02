def calculate_average(marks):
    total=0
    for mark in marks:
        total=total+mark
    average=total/len(marks)
    return average

def find_grade(average):
    if average>=90:
        return "A"
    elif average>=75:
        return "B"
    elif average>=50:
        return "C"
    else:
        return "F"

def main():
    marks=[85, 70, 90, 60, 75]
    avg=calculate_average(marks)
    grade=find_grade(avg)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)

main()
