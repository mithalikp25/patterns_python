n=5
for rows in range(1,n+1):
    p=5
    for cols in range(1,n-rows+2):
        print(p,end=" ")
        p-=1
    print()

"""
5 4 3 2 1 
5 4 3 2 
5 4 3
5 4
5
"""


n=5
for rows in range(1,n+1):
    p=5
    for spaces in range(1,rows):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print(p,end=" ")
        p-=1
    print()

"""
5 4 3 2 1
  5 4 3 2
    5 4 3
      5 4
        5
"""