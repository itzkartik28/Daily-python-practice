student={
101:"rahul",
102:"amit",
103:"neha"
}

roll=int(input("enter a roll number:"))

if roll in student:
    print("student name:",student[roll])
else:
    print("student is not found")