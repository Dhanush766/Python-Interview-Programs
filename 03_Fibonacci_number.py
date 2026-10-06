#Write the values of Fibonacci N terms
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
n=int(input("Enter the numbers of terms: "))
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
