#Method 1

n=9

for rows in range(1,n+1):
    if rows<=5:
        for cols in range(1,rows+1):
            print("*",end=" ")
    else:
        for cols in range(1,n-rows+2):
            print("*",end=" ")
    print()


#Method 2
    
n=5

for rows in range(1,n+1):
    for cols in range(1,rows+1):
            print("*",end=" ")
    print()
for rows in range(1,n):
    for cols in range(1,n-rows+1):
          print("*",end=" ")
    print()
    

"""
* 
* * 
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""