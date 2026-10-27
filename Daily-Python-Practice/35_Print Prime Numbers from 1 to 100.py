for num in range(1,101):

  count=0

  for i in range(1,num+1):
    if num % i ==0:
      count=count+1

if count==0:
  print(f"prime numbers are:{num}")