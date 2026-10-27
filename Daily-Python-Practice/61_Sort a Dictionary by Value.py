student_names={
    "rahul":75,
    "priya":90,
    "neha":60,
    "amit":55
}

print("orignal distionary")
print(student_names)

acending=dict(sorted(student_names.items(),key=lambda item:item[1]))

print("acending order:")
print(acending)

decending=dict(sorted(student_names.items(),key=lambda item:item[1] reverse=true))

print("decending order:")
print(decending)