#implement a recursive function to calculate the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("Enter a number to find factorial: "))
res= factorial(n)
print("the factorial of the number",n, "is",res );