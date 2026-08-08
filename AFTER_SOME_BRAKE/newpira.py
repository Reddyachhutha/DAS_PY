for j in range(5):
    for k in range(4-j):
        print(" ",end="")
    for m in range(2*j+1):
        print("*",end="")
    print()
for m in range(5):
    for n in range(m):
        print(" ",end="")
    for p in range(5*2-m*2-1):
        print("*",end="")
    print()