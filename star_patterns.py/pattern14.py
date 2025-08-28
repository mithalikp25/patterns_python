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

<<<<<<< HEAD
=======

>>>>>>> fb50aa4 (Work in progress before merge)
