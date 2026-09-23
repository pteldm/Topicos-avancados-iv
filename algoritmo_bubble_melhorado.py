import sys

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

for i in range(n):
    trocou = False
    for j in range(i, n-1):
        if v[j] > v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]
            trocou = True
    if not trocou:
        break

#print(v)