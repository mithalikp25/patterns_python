n=4

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(" * ",end=" ")
    for spaces in range(1,n-rows+1):
        print("   ",end=" ")
    for cols in range(1,rows+1):
        print(" * ",end=" ")
    print()
n=7
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print(" * ",end=" ")
    print()

"""
       *               *
     *   *           *   *
   *   *   *       *   *   *
 *   *   *   *   *   *   *   *
   *   *   *   *   *   *   *
     *   *   *   *   *   *
       *   *   *   *   *
         *   *   *   *
           *   *   *
             *   *
               *
"""