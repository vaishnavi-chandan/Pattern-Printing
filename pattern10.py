# Hollow square pattern
n = 5 

for i in range(n):
    for j in range(n):
        # Print an asterisk on the outer border of the square.
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            # Print a space for positions inside the hollow square.
            print(" ", end=" ")
    # Move to the next line after each row.
    print()