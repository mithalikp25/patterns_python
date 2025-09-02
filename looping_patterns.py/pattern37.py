n=5

for rows in range(1,n+1):
    p=rows
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1, rows+1):
        print(p,end=" ")
        p-=1
    print()

"""
        1 
      2 1 
    3 2 1
  4 3 2 1
5 4 3 2 1
"""
