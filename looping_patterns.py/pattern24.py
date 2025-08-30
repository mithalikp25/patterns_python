
n=4
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end = " ")
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print("*",end = " ")
    print()
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print("*",end = " ")
    for spaces in range(1,rows):
        print(" ",end=" ")
    for spaces in range(1,rows):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print("*",end = " ")
    print()

"""
*             * 
* *         * * 
* * *     * * *
* * * * * * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
"""