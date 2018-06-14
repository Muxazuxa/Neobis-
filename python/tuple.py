if __name__ == '__main__':
    n = int(input())
    arr=tuple(int(x) for x in input().split())
    print(hash(arr))
