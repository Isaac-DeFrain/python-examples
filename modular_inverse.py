# modular arithmetic

# inverse of x modulo n
def inverse(x, n):
    inv = None
    for y in range(1, n):
        if (x * y) % n == 1:
            inv = y
            break
    return inv
