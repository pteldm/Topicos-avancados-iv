import sys
import heapq

entrada = sys.stdin.read().split()

n = int(entrada[0])
v = [int(x) for x in entrada[1:n+1]]

# cria o max-heap invertendo os sinais dos elementos
max_heap = [-x for x in v]
heapq.heapify(max_heap)

# selection sort extrai o maior elemento (menor negativo) 
# e preenche o vetor original de trás para frente

# começa em n-1, vai até -1, decrementando de 1 em 1
for i in range(n - 1, -1, -1):
    maior_elemento = -heapq.heappop(max_heap)
    v[i] = maior_elemento

print(v)