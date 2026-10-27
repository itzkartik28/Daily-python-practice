list1=[10,20,30,40,50]
list2=[60,70,30,80,90]

common=False

for item in list1:
    if item in list2:
        common=True
        break

print("common number is:",common)