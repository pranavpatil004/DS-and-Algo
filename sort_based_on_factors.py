def print_factors(x):
    print("The factors of",x,"are:")
    factors = 0
    for i in range(1, x + 1):
        if x % i == 0:
            factors += 1
            print(i)
    return factors


print(sorted([1,3,5,6,9,4,8], key=lambda x: print_factors(x)))