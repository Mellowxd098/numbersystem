
print("Enter the Hexadecimal Number: ", end="")
hnum = input()

hnum = int(hnum, 16)
bnum = bin(hnum)
print("\nEquivalent Binary Value= ", bnum[2:])
