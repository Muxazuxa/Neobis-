sin = input()
sout = ''.join([sin[0].upper()] + [sin[i].upper() if sin[i-1].isspace() else sin[i] for i in range(1,len(sin))])
print(sout)
