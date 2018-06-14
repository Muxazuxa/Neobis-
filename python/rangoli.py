n = int(input())
s = []
for i in list(range(n-1,0,-1))+list(range(n)):
    line = ('-'.join([chr(ord('a')+i) for i in range(n-1,i-1,-1)] +
        [chr(ord('a')+i) for i in range(i+1,n)]))
    print(line.center(4*n-3,'-'))
