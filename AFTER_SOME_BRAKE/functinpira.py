def piramid(rows):
    for i in range(rows):
        for k in range(rows-1-i):
            print(" ",end="") # this loop for the spaces
        
        for l in range(i*2+1):
            print("*",end="")
        print()
    for m in range(rows):
        for d in range(m):
            print(" ",end="")
        for r in range(2*(rows-m)-1):
            print("*",end="")
        print()
piramid(5)