numbers=[10,50,30,45,80]

largest=numbers[0]

for i in numbers:
    if i>largest:
        largest=i

print(f"largest number is{largest}")