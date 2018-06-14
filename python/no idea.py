n, m = (int(x) for x in input().split())
ar = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
print(len([x for x in ar if x in A])-len([x for x in ar if x in B]))
