student={
    101:"rahul",
    102:"amit",
    103:"neha"
}
even=0
odd=0

for roll in student.keys():
    if roll%2==0:
      even+=1
    else:
      odd+=1

print("even:",even)

print("odd:",odd)
