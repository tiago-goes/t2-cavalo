from graph import Graph
from stack import Stack

class Cycle:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.has_cycle = False
        self.edge_to = [-1 for _ in range(G.V)]  # Adicionar edge_to para rastrear o caminho
        self.cycle = None  # Armazenar o ciclo para recuperação posterior
        for s in range(G.V):
            if not self.marked[s] and not self.has_cycle:
                self.dfs(G, s, s)

    def dfs(self, G, v, u): #possui complexidade O(V + E) onde V é o número de vértices e E é o número de arestas no grafo.
        if self.has_cycle:
            return
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w, v)
            elif w != u and not self.has_cycle:
                self.has_cycle = True
                self.cycle = Stack()
                x = v
                while x != w:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(w)
                self.cycle.push(v)
                return

    def get_cycle(self):
        if self.has_cycle and self.cycle is not None:
            cycle_list = []
            for v in self.cycle:
                cycle_list.append(v)
            return cycle_list[::-1]  
        return None
    
    