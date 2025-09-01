#special case patterns

#pattern 1

n=5
p=1

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(p,end=" ")
    p+=1
    print()

"""
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
"""

#pattern 2

n=5
p=1

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(p,end=" ")
        p+=1
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

#pattern 3

n=5
p=1

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        if rows%2==0:
            print(p+1,end=" ")
        else:
            print(p,end=" ")
    print()

"""
1
2 2
1 1 1
2 2 2 2
1 1 1 1 1
"""

