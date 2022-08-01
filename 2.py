# Problem 2
# use dynamic programming
def even_fib_num():
    thresh = 4000000
    total = 0
    dp = [0, 1]
    i = 2
    while True:
        dp.append(dp[i-1] + dp[i-2])
        if dp[i]%2 == 0:
            total += dp[i]
        if dp[i] > thresh:
            break
        i += 1
    return total

print(even_fib_num())