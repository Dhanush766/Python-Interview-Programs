s=int(input("Enter a number: "))
total=0
while s>0:
    digit=s%10
    total=total+digit
    s=s//10
print(total)