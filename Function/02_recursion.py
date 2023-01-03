
# factorial(n) = n *(n-1)!

# find factorial
n = 4
p = 1
for j in range(n):
    p = p * (j+1)
    print(p)

# factorial iterative using function


def factorial_iterative(n):
    fact = 1
    for f in range(n):
        fact = fact * (f+1)
    return fact


print(factorial_iterative(5))


# factorial recursion using function
def fatorial_recursion(m):
    if m == 1 or m == 0:
        return 1
    return m * fatorial_recursion(m-1)


print(fatorial_recursion(6))

# recusion function khud ko call karta hai