# Diamond
n = 5

# top half (including the widest row)
for i in range(1, n + 1):
    print("  " * (n - i) + " ".join("*" * (2 * i - 1)))

# bottom half
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + " ".join("*" * (2 * i - 1)))