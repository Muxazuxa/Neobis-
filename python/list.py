n=int(input())
arr=[]
for _ in range(n):
    command=input().split()
    func=command[0]
    if func=='print':
        print(arr)
    elif func=='pop':
        arr.pop()
    elif func=='reverse':
        arr.reverse()
    elif func=='sort':
        arr.sort()
    elif func=='remove':
        arr.remove(int(command[1]))
    elif func=='append':
        arr.append(int(command[1]))
    elif func=='insert':
        arr.insert(int(command[1]),int(command[2]))
