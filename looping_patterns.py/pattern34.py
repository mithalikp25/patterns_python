n=5

for rows in range(1,n+1):
    p=1
    for cols in range(1,rows+1):
        print(p,end=" ")
        p+=1
    for spaces in range(n-rows):
        print(" ",end=" ")
    q=1
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(q,end=" ")
        q+=1
    print()

"""
1                 1 
1 2             1 2 
1 2 3         1 2 3
1 2 3 4     1 2 3 4
1 2 3 4 5 1 2 3 4 5
"""

