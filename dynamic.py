def find_min_coins(amount, coins=[1, 2, 5, 10, 25, 50]):
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and min_coins[a - coin] + 1 < min_coins[a]:
                min_coins[a] = min_coins[a - coin] + 1
                coin_used[a] = coin
    result = {}
    while amount > 0:
        c = coin_used[amount]
        result[c] = result.get(c, 0) + 1
        amount -= c
    return result
