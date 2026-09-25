import sys 

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

for i in range(n):
    for j in range(0, n-1):
        if v[j] > v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]

#print(v)