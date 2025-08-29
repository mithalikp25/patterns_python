n=4

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows:
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    for spaces in range(1,n-rows+1):
        print("   ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows:
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
        
    print()
n=7
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        if cols==1 or cols== n-rows+1:
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()

"""
       *               *  
     *   *           *   *  
   *       *       *       *
 *           *   *           *
   *                       *
     *                   *
       *               *
         *           *
           *       *
             *   *
               *
"""