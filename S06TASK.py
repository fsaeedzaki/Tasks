Rows = int(input("Enter the number of rows: "))

for i in range(1, Rows + 1):
    Spaces = Rows-i
    Stars = 2*i-1
    print(" " * Spaces + "*" * Stars)
