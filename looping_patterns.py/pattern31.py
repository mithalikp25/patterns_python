n=5
p=1

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,2*rows):
        print(p,end=" ")
    p+=1
    print()
p=6
for rows in range(1,n):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*n)-(2*rows)):
        print(p,end=" ")
    p+=1
    print()
         
"""
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  6 6 6 6 6 6 6
    7 7 7 7 7
      8 8 8
        9
"""

#pattern 4


n=5
p=1

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,2*rows):
        print(p,end=" ")
    p+=1
    print()
p=4
for rows in range(1,n):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,(2*n)-(2*rows)):
        print(p,end=" ")
    p-=1
    print()
        
"""
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
"""