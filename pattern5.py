# Repeated Number Right-angled Triangle pattern
n = 5
for i in range(1, n + 1):           #for loop to iterate through the rows
    print(" ".join(str(i) * i))     #printing the repeated numbers in each row