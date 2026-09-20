import sys

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

for i in range(1, n):
    chave = v[i]
    j = i - 1
    while j >= 0 and chave < v[j]:
        v[j + 1] = v[j]
        j -= 1
    v[j + 1] = chave
