n=5

for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
        * 
      * * 
    *   *
  *     *
* * * * *
"""

n = 5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
*
* *
*   *
*     *
* * * * *
"""