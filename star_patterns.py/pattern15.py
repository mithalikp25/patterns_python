#Method 1

n=9

for rows in range(1,n+1):
    if rows<=5:
        for spaces in range(1,n-rows+1):
            print(" ",end=" ")
        for cols in range(1,2*rows):
            if cols==1 or cols==2*rows-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        for spaces in range(1,rows):
            print(" ",end=" ")
        for cols in range(1,(2*n)-(2*rows)+2):
            if cols==1 or cols==((2*n)-(2*rows)+1):
                print("*",end = " ")
            else:
                print(" ",end=" ")
        print()

#Method 2

n = 5

for rows in range(1, n+1):
    for spaces in range(1, n-rows+1):
        print(" ", end=" ")
    for cols in range(1, 2*rows):
        if cols == 1 or cols == 2*rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for rows in range(n-1, 0, -1):
    for spaces in range(1, n-rows+1):
        print(" ", end=" ")
    for cols in range(1, 2*rows):
        if cols == 1 or cols == 2*rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Method 3 

n=5
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*rows)):
        if cols==1 or cols==2*rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*n)-(2*rows)):
        if cols==1 or cols==((2*n)-(2*rows)-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Method 4

n=5

for rows in range(1,n*2):
    if rows<=5:
        for spaces in range(1,n-rows+1):
            print(" ",end=" ")
        for cols in range(1,2*rows):
            if cols==1 or cols==(2*rows-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    else:
        for spaces in range(1,rows-n+1):
            print(" ",end=" ")
        for cols in range(1,(4*n)-(2*rows)):
            if cols==1 or cols==((4*n)-(2*rows)-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

"""
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
"""

