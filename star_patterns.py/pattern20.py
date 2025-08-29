n=8

for rows in range(1,n+1):
    if rows<5:
        for spaces in range(1,rows+1):
            print(" ",end=" ")
        for cols in range(1,n-(2*rows)+2):
            if rows==1 or cols==1 or cols==n-(2*rows)+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    else:
        for spaces in range(1,n-rows+2):
            print(" ",end=" ")
        for cols in range(1,(2*rows)-n):
            if rows==n or cols==1 or cols==(2*rows)-n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

"""
  * * * * * * * 
    *       * 
      *   *
        *
        *
      *   *
    *       *
  * * * * * * *
"""