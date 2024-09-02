n = int(input("Enter a Number: "))
noc = 1  # Start column for printing "*"
nor = n * 2 - 1  # End column for printing "*"

for i in range(1, n * 2):
    for j in range(1, n * 2):
        # Print "*" for the first and last row or the first and last columns
        if i == 1 or i == n * 2 - 1 or j == 1 or j == n * 2 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
