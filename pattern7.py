# Star pyramid pattern
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + " ".join("*" * (2 * i - 1)))  # Printing spaces and stars for pyramid pattern
