def sum_recursive(n):
    if n == 1:          # Base Case
        return 1
    return n + sum_recursive(n - 1)

print(sum_recursive(5))  # 15