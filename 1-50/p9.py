def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2


if __name__ == '__main__':
    for a in range(1, 999):
        for b in range(1, 1000 - a):
            if is_pythagorean(a, b, 1000 - a - b):
                print(a, b, 1000 - a - b)
