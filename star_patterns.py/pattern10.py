#Method 1
n=9

for rows in range(1,n+1):
    if rows<=5:
        for spaces in range(1,n-rows+1):
            print(" ",end=" ")
        for cols in range(1,2*rows):
            print("*",end=" ")
        print()
    else:
        for spaces in range(1,rows):
            print(" ",end=" ")
        for cols in range(1,(2*n)-(2*rows)+2):
            print("*",end = " ")
        print()

#Method 2

n=5
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*rows)):
        print("*",end=" ")
    print()
n=4
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*n)-(2*rows)+2):
        print("*",end=" ")
    print()

#Method 3 

n=5
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*rows)):
        print("*",end=" ")
    print()
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*n)-(2*rows)):
        print("*",end=" ")
    print()

"""
                * 
              * * * 
            * * * * *
          * * * * * * *
        * * * * * * * * *
          * * * * * * *
            * * * * *
              * * *
                *
"""