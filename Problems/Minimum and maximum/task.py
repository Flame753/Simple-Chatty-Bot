num1 = int(input())
num2 = int(input())


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


def minimum(a, b):
    return a if a < b else b


print(maximum(num1, num2))
print(minimum(num1, num2))
