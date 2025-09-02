#string pattern programs

#pattern 1

s="CODER"
n=len(s)
p=0

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(s[p],end=" ")
    p+=1
    print()

"""
C 
O O 
D D D
E E E E
R R R R R
"""

# Pattern 2

s="CODER"
n=len(s)
p=n-1

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(s[p],end=" ")
    p-=1
    print()

"""
R
E E
D D D
O O O O
C C C C C
"""

# Pattern 3

s="CODER"
n=len(s)

for rows in range(1,n+1):
    p=0
    for cols in range(1,rows+1):
        print(s[p],end=" ")
        p+=1
    print()

"""
C
C O
C O D
C O D E
C O D E R
"""

# Pattern 4

s="CODER"
n=len(s)

for rows in range(1,n+1):
    p=n-1
    for cols in range(1,rows+1):
        print(s[p],end=" ")
        p-=1
    print()

"""
R
R E
R E D
R E D O
R E D O C
"""