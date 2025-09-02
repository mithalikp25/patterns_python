#character patterns (columns)

#pattern 1

n=5

for rows in range(1,n+1):
    ch=65
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch+=1
    print()

"""
A 
A B 
A B C
A B C D
A B C D E
"""

#pattern 2

n=5

for rows in range(1,n+1):
    ch=65
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch+=1
    for cols in range(1,rows):
        print(chr(ch),end=" ")
        ch+=1
    print()

"""
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
"""

#pattern 3

n=5

for rows in range(1,n+1):
    ch=65
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch+=1
    for cols in range(1,rows):
        print(chr(ch),end=" ")
        ch+=1
    print()
for rows in range(1,n):
    ch=65
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for cols in range(1,n-rows+1):
        print(chr(ch),end=" ")
        ch+=1
    for cols in range(1,n-rows):
        print(chr(ch),end=" ")
        ch+=1
    print()

"""
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
  A B C D E F G
    A B C D E
      A B C
        A
"""

#pattern 4

n=5

for rows in range(1,n+1):
    ch=65
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch+=1
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    ch=65
    for spaces in range(1,n-rows+1):
        print(" ",end=" ") 
    for cols in range(1,rows+1):
        print(chr(ch),end=" ")
        ch+=1
    print()
for rows in range(1,n):
    ch=65
    for cols in range(1,n-rows+1):
        print(chr(ch),end=" ")
        ch+=1
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    ch=65
    for spaces in range(1,rows+1):
        print(" ",end=" ")  
    for cols in range(1,n-rows+1):
        print(chr(ch),end=" ")
        ch+=1
    print()

"""
A                 A
A B             A B
A B C         A B C
A B C D     A B C D
A B C D E A B C D E
A B C D     A B C D
A B C         A B C
A B             A B
A                 A
"""