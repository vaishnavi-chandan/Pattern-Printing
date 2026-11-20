# Inverted Star pyramid pattern
n = 5
for i in range(n, 0, -1):
    print("  " * (n - i) + " ".join("*" * (2 * i - 1)))  # Printing spaces and stars for inverted pyramid pattern