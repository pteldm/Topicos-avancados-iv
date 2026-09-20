import sys

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

min_idx = 0
for i in range(1, n):
    if v[i] < v[min_idx]:
        min_idx = i
v[min_idx], v[0] = v[0], v[min_idx]    

for i in range(2, n):
    chave = v[i]
    j = i - 1
    
    while chave < v[j]:
        v[j + 1] = v[j]
        j -= 1
    
    v[j + 1] = chave
print(v)