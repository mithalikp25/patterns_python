n = 7
for rows in range(1, n+1):
    for cols in range(1, n+1):
        if cols == rows or cols == n - rows + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


"""
*           * 
  *       *   
    *   *
      *
    *   *
  *       *
*           *
"""


n=4
num=1
for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(num,end="   ")
        num+=1
    print()