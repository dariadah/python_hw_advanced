def gcd_1(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

gcd_1(20, 45)


def gcd_2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)

gcd_2(10, 20)

