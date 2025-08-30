#Method 1

for rows in range(1,5):
    for cols in range(1,8):
        if cols >= rows+1 and cols <= 7-rows:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

#Method 2

for rows in range(1,5):
    for cols in range(1,8):
        if cols<=rows or cols>=(5-rows)+3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
*           * 
* *       * * 
* * *   * * *
* * * * * * *
"""