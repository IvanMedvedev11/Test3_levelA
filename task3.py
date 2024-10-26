def power_two(n):
    if n == 2:
        return "YES"
    elif n % 2 != 0:
        return "NO"
    else:
        return power_two(n // 2)
n = int(input())
print(power_two(n))
