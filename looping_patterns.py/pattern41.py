# Pattern 1

n=5
k=69
for rows in range(1,n+1):
    ch=k
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print(chr(ch),end=" ")
        ch-=1
    k-=1
    print()

"""
  E D C B A
    D C B A
      C B A
        B A
          A
"""
# Pattern 2

n=5
k=65
for rows in range(1,n+1):
    ch=k
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch-=1
    k+=1
    print()

"""
A
B A
C B A
D C B A
E D C B A
"""

# Pattern 3

n=5
k=65
for rows in  range(1,n+1):
    p=65
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows):
        print(chr(p),end=" ")
        p+=1
    p=k
    for cols in range(1,rows+1):
        print(chr(p),end=" ")
        p-=1
    k+=1
    print()

"""
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""