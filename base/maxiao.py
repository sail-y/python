
def can(b):
    c=1
    for i in range(b):
        c *= i+1
        print(i)
    return c

print(can(5))
