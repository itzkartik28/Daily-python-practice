from datetime import date

name=input("enter your name:")
age=int(input("enter your age:"))

current_year=date.today().year
year_100=current_year+(100 - age)

print(f"{name},you will turn 100 year old in this year{year_100}")