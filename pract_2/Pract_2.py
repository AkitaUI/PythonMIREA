#1
def f1(n,m,a):
    prod1 = 1
    prod2 = 1
    sum = 0
    c = 1
    j = 1
    i = 1
    while c <= a:
        while j <= m:
            while i <= n:
                sum += ((((28*c**2)**6)/5) + 16*((j**3/44)+i**2)**5)
                i += 1
            prod2 *= sum
            j += 1
        prod1 *= prod2
        c += 1
    return prod1

print("f1:", f1(4,2,8))

#2
import math

def f2(y=[], z=[]):
    sum = 0
    for i in range(len(y)):
        sum += (y[i]-z[i])**2
    sum = math.sqrt(sum)
    return sum

print("f2:", f2([1, 0.5, 1], [0.5, 2, 1]))

#3
def f3(y=[], z=[]):
    sum = 0
    n = 0
    for i in range(len(y)):
        n = (y[i]-z[i])
        if n<0:
            n *= -1
        sum += n
    return sum

print("f3:", f3([1, 0.5, 1], [0.5, 2, 1]))

#4
def f4(y=[], z=[]):
    sum1 = 0
    sum2 = 0
    for i in range(len(y)):
        sum1 = (y[i]-z[i])
        if sum1 < 0:
            sum1 *= -1
        if sum1 > sum2:
            sum2 = sum1
        sum1 = 0
    return sum2

print("f4:", f4([1, 0.5, 1], [0.5, 2, 1]))

#5
import math

def f5(y=[], z=[]):
    sum = 0
    for i in range(len(y)):
        sum += (y[i]-z[i])**2
    return sum

print("f5:", f5([1, 0.5, 1], [0.5, 2, 1]))

#6
def f6(y=[], z=[]):
    sum = 0
    n = 0
    h = 5
    for i in range(len(y)):
        n = (y[i]-z[i])
        if n<0:
            n *= -1
        n**h
        sum += n
    sum**(1/h)
    return sum

print("f6:", f6([1, 0.5, 1], [0.5, 2, 1]))

#7
import matplotlib.pyplot as plt

def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()

    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 2}' for i in x])

    plt.show()

visualize((f2, f3, f4, f5, f6), [1,0.5,1],[0.5,2,1])

#8
def reverse_and_join(words):
    reversed_words = words[-1]
    for i in range(len(words) - 2, -1, -1):
        reversed_words += (' ' + words[i])
    return reversed_words
words = ["language!", "programming", "Python", "the", "love", "I"]
result = reverse_and_join(words)
print("f8:", result)

#9
def f9(s, c):
    count = 0
    for i in c: 
        if s == i:
            count += 1
    return count

def count_characters(text):
    text = text.lower().replace(" ", "")
    char_count = {}

    for i in text:
        char_count[i] = f9(i, text)

    return char_count

print("f9:", count_characters("I love the Python programming language!"))