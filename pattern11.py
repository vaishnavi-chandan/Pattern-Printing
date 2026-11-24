# Hollow right-angled triangle pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print an asterisk on the outer border of the triangle.
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()