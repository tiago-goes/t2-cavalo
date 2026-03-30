
import os
from graph import Graph
from breadth_first_paths import BreadthFirstPaths
from cc import CC
from cycle import Cycle


arquivo= os.path.join((os.path.dirname(os.path.dirname(__file__))),"dados","entrada.txt")

f = open(arquivo)
s = 0
V = int(f.readline())
E = int(f.readline())

g = Graph(V)
for i in range(E):
    v, w = f.readline().split()
    g.add_edge(v, w)

lista_adj = g.get_adjacent_list()
print("Lista de adjacências:")
for i in range(len(lista_adj)):
    print(f"{i}: {lista_adj[i]}")

cc = CC(g)
print("\nComponentes conexas:")
components = []
for i in range(cc.count):
    components.append([])

for v in range(g.V):
    components[cc.id[v]].append(v)
for i in range(cc.count):
    print(f"Componente {i}: {components[i]}")

inicial = BreadthFirstPaths(g, 0)
distancia = inicial.distance_to(8)
print(f"\nDistância de (0,0) para (2,2): {distancia}")
cycle = Cycle(g) #comentarios realizados na classe Cycle.py
print(f"\nO grafo tem ciclo? {'Sim' if cycle.has_cycle else 'Não'}")
if cycle.has_cycle:
    cycle_list = cycle.get_cycle()
    print("Ciclo encontrado:", " -> ".join(str(v) for v in cycle_list))