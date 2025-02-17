#3.1

x1 = 1
x1 = x1 + x1 + x1
x1 = x1 + x1
x1 = x1 + x1
print(x1)

#3.2
x2 = 1
x2 = x2 + x2
x2 = x2 + x2
x2 = x2 + x2
x2 = x2 + x2
print(x2)

#3.3
x3 = 1
y = 1
x3 = x3 + x3
x3 = x3 + x3
x3 = x3 + x3
y = y - x3
x3 = x3 - y
print(x3)

#3.4

def f(b, n, a):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    prod = 1
    j = 1
    c = 1
    c1 = 1
    k = 1
    while j <= n:
        while c1 <= b:
            sum1 += ((34 * j + 41)**4 - 93 * (c1 + 79 + c1**3)**5)
            c1 = c1 + 1
        sum2 += sum1
        j = j+1

    while k <= a:
        while c <= b:
            sum3 += (22 * (c - 8)**5 - k**4)
            c = c + 1
        prod = prod * sum3
        k = k + 1

    return sum2 - prod

print(f(2, 2, 6))

#3.5
import math

def f2(x):
    if x < 13:
        return(x**5)
    elif 13 <= x < 87:
        return(x**7 - 1 - (((math.floor(x))**3)/54))
    else:
        return((math.celi(x))**3)

print(f2(14))

#3.6
def f3(x):
    if x == 0:
        return 3
    else:
        return math.sin(f3(x - 1)) - (1 / 16) * (f3(x - 1) ** 3)

print(f3(8))

#3.7
def fast_mul(x: int, y: int):
    result = 0
    while x > 0:
        if x % 2 == 1:
            result += y
        x //= 2
        y *= 2
    return result

print(fast_mul(10, 15))

#3.8
def fast_pow(x: int, y: int):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x *= x
        y //= 2
    return result

print(fast_pow(10, 5))