import sys 

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

for i in range(n-1):
    menor_valor_indice = i
    for j in range(i+1, n):
        if v[j] < v[menor_valor_indice]:
            menor_valor_indice = j
    menor_valor = v[menor_valor_indice]
    v[menor_valor_indice] = v[i]
    v[i] = menor_valor

#print(v)