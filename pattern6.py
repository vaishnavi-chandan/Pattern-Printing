# Right aligned triangle pattern
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + " ".join("*" * i))       # Printing spaces and stars for right-aligned triangle