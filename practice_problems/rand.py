def rand5():
    return 1

def rand7():
    sum = 0
    for _ in range(7):
        sum += rand5()
    return sum % 7