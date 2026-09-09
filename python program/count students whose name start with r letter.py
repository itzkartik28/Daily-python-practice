student={
    101:"rahul",
    102:"amit",
    103:"riya",
    104:"neha"
}
count=0
for name in student.values():
    if name.startswith("r"):
        count+=1

print("student name starting R:",count)