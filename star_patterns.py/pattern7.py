
n = 5

for rows in range(1,n+1):
    for spaces in range(1,rows+1):
            print(" ",end = " ")
    for cols in range(1,(2*n)-(2*rows)+2):
       print("*",end = " ") 
    print()