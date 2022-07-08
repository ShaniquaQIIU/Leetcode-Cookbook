def deomo(a, b, c=0):
    if a > 0 and b > 0:
        c = c/a
    if a > 1 or c > 1:
        c = c+1
    c = b + c
    return c


if __name__ == '__main__':
    print(deomo(1, 2))
