n=5

for rows in range(1,n+1):
    for cols in range(1,n*2):
        if cols<=rows or cols>=(n-rows)+5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for rows in range(1,n):
    for cols in range(1,n*2):
        if cols<=n-rows or cols>=n+rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()

"""
*               * 
* *           * * 
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
"""
        

