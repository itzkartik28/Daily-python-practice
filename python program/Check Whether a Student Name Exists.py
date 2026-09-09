student={
    101:"rahul",
    102:"amit",
    103:"neha"
}

name=input("enter name:")
if name in student.values():
    print("name found!!")
else:
    print("name not found")