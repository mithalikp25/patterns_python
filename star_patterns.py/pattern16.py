n=5

for rows in range(1,n+1):
    for spaces in range(1,rows):
        print(" ",end = " ")
    for cols in range(1,n-rows+2):
        if rows==1 or cols==n-rows+1 or cols==1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()


"""
* * * * * 
  *     * 
    *   *
      * *
        *
"""

n = 5

for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        if cols==1 or rows==1 or cols==n-rows+1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()

"""
* * * * *
*     *
*   *
* *
*
"""


