n=8

for rows in range(1,n+1):
    if rows<5:
        for spaces in range(1,rows):
            print(" ",end=" ")
        for cols in range(1,n-(2*rows)+2):
            print("*",end=" ")
    else:
        for spaces in range(1,n-rows+1):
            print(" ",end=" ")
        for cols in range(1,(2*rows)-n):
            print("*",end=" ")
    print()

"""
  * * * * * * * 
    * * * * * 
      * * *
        *
        *
      * * *
    * * * * *
  * * * * * * *
"""