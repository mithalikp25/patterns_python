n=5

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,2*rows):
        if rows==n or cols==1 or cols==2*rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
        * 
      *   * 
    *       *
  *           *
* * * * * * * * *
"""