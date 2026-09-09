student={
    101:"rahul",
    102:"amit",
    103:"kartikkkkkkkkkkkkkkkkkkkkkk",
    104:"neha"
}
longest=""
for name in student.values():
    if len(name) > len(longest):
     longest=name


print("the longest name:",longest)