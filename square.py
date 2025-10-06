n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i in (1,n):
            print('*',end='')
        elif j in (1,n): 
            print('*',end='')
        else:
            print(' ',end='')
    print()