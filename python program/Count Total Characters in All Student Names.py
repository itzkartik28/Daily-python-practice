student={
    101:"neha",
    102:"amit",
    103:"rahul"
}

total=0
for name in student.values():
    total+=len(name)

print("total characters:",total)