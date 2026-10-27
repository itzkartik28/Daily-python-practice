text=input("enter the text:")

count=0

for ch in text:
    if ch in "aeiouAEIOU":
        count=count+1

print(f"number of charater{count}")