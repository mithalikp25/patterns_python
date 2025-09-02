#character patterns

#pattern 1

n=5
ch=65
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    ch+=1
    print()

"""
A 
B B 
C C C
D D D D
E E E E E
"""
#pattern 2

n=5
ch=69

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    ch-=1
    print()

"""
E
D D
C C C
B B B B
A A A A A
"""

#pattern 3

n=5
ch=65

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    for cols in range(1,rows):
        print(chr(ch),end=" ")
    ch+=1
    print()

"""
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E
"""

#pattern 4

n=5
ch=65

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    ch+=2
    print()

"""
A
C C
E E E
G G G G
I I I I I
"""

#pattern 5

n=5
ch=65

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    for cols in range(1,rows):
        print(chr(ch),end=" ")
    ch+=1
    print()
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+1):
        print(chr(ch),end=" ")
    for cols in range(1,n-rows):
        print(chr(ch),end=" ")
    ch+=1
    print()

"""
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E
  F F F F F F F
    G G G G G
      H H H
        I
"""
#pattern 6

n=5
ch=65

for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
    for cols in range(1,rows):
        print(chr(ch),end=" ")
    ch+=1
    print()
for rows in range(1,n):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+1):
        print(chr(ch-2),end=" ")
    for cols in range(1,n-rows):
        print(chr(ch-2),end=" ")
    ch-=1
    print()

"""
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E
  D D D D D D D
    C C C C C
      B B B
        A
"""