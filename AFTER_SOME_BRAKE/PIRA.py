for i in range(5):
    for j in range(5-1-i):
        print(" ", end="")
    for k in range (2*i+1):
        print("*", end="")
    
    print()
for m in range(5):
    for n in range(m):
        print(" ", end="")
    for o in range(2*(5-m)-1):
        print("*", end="")
    
    print()

