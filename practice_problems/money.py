# This problem was asked by Google.

# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

# order from largest to smallest to check largest coins first
coins = [25, 10, 5, 1]

def minimum_number_of_coins(cents: int):
    if cents < 0:
        return -1
    
    num_coins = 0

    coins_idx = 0 # current index of coins
    while cents > 0:
        if cents >= coins[coins_idx]:
            cents -= coins[coins_idx]
            num_coins += 1
        else:
            coins_idx += 1

    return num_coins

assert minimum_number_of_coins(16) == 3 # 10 5 1
assert minimum_number_of_coins(17) == 4 # 10 5 1 1
assert minimum_number_of_coins(26) == 2 # 25 1
assert minimum_number_of_coins(30) == 2 # 25 5
assert minimum_number_of_coins(79) == 7 # 25 25 25 1 1 1 1
assert minimum_number_of_coins(-1) == -1 # invalid
