def is_prime(func):
    def wrapper(*num):
        i = True
        res = func(*num)
        for j in range(2, res):
            if res % j == 0:
                i = False
        if i:
            print("Простое")
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)