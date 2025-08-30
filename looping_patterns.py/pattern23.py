for rows in range(1,5):
    for cols in range(1,8):
        if cols<=5-rows or cols>=3+rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
* * * * * * * 
* * *   * * * 
* *       * *
*           *
"""