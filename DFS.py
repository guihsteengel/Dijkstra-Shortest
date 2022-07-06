import sys

def dijkstra_algorithm(graph, starting_city):
    unvisited_knots = list(graph.get_knots())
 
    # Usa este dict para economizar o custo de visitar cada nó e atualizá-lo à medida que avançamos no gráfico
    road_short = {}
 
    # Usa este dict para salvar o caminho mais curto conhecido para um nó encontrado até agora
    preceding_knot = {}
 
    # Usa max_valuation para inicializar o valor "infinity" dos nós não visitados   
    max_valuation = sys.maxsize
    for knot in unvisited_knots:
        road_short[knot] = max_valuation
    # No entanto, inicia o valor do nó inicial com 0   
    road_short[starting_city] = 0
    
# O algoritmo é executado até visitar todos os nós
    while unvisited_knots:
      # O bloco de código abaixo encontra o nó com a pontuação mais baixa
        current_min_knot = None
        for knot in unvisited_knots: # Iterar sobre os nós
            if current_min_knot == None:
                current_min_knot = knot
            elif road_short[knot] < road_short[current_min_knot]:
                current_min_knot = knot
                
        # O bloco de código abaixo recupera os vizinhos do nó atual e atualiza suas distâncias
        neighbors = graph.get_outgoing_edges(current_min_knot)
        for neighbor in neighbors:
            tentative_valuation= road_short[current_min_knot] + graph.valuation(current_min_knot, neighbor)
            if tentative_valuation< road_short[neighbor]:
                road_short[neighbor] = tentative_valuation
                # Também atualiza o melhor caminho para o nó atual
                preceding_knot[neighbor] = current_min_knot
 
        # Após visitar seus vizinhos, marca o nó como "visitado"

        unvisited_knots.remove(current_min_knot)
    
    return preceding_knot, road_short

class Graph(object):
    def __init__(self, knots, early_graph):
        self.knots = knots
        self.graph = self.construct_graph(knots, early_graph)
        
    def construct_graph(self, knots, early_graph):
        '''
        Este método garante que o gráfico seja simétrico. Em outras palavras, se houver um caminho do nó A para o B com uma avaliação V, precisa haver um caminho do nó B para o nó A com uma avaliação V.
        '''
        graph = {}
        for knot in knots:
            graph[knot] = {}
        
        graph.update(early_graph)
        
        for knot, edges in graph.items():
            for adjacent_knot, valuation in edges.items():
                if graph[adjacent_knot].get(knot, False) == False:
                    graph[adjacent_knot][knot] = valuation
                    
        return graph
    
    def get_knots(self):
        "Retorna os nós do gráfico."
        return self.knots
    
    def get_outgoing_edges(self, knot):
        "Retorna os vizinhos de um nó."
        connections = []
        for out_knot in self.knots:
            if self.graph[knot].get(out_knot, False) != False:
                connections.append(out_knot)
        return connections
    
    def valuation(self, knot1, knot2):
        "Retorna a avaliação de uma aresta entre dois nós."
        return self.graph[knot1][knot2]


def print_result(preceding_knot, road_short, starting_city, target_knot):
    road = []
    knot = target_knot
    
    while knot != starting_city:
        road.append(knot)
        knot = preceding_knot[knot]
 
    # Adiciona o nó inicial manualmente
    road.append(starting_city)
    
    print("O Mínimo caminho é {}.".format(road_short[target_knot]))
    print(" -> ".join(reversed(road)))

knots = ["Oradea","Zerind","Arad","Sibiu","Fagaras","Timisoara","Lugoj","Mehadia","Dobreta","Craiova","Rimnicu Vilcea","Pitesti","Bucharest","Girgiu","Urziceni","Hirsova","Vaslui","Eforie","Iasi","Neamt",]
 
early_graph = {}
for knot in knots:
    early_graph[knot] = {}
    
early_graph["Oradea"]["Zerind"] = 71
early_graph["Oradea"]["Sibiu"] = 151

early_graph["Zerind"]["Arad"] = 75
early_graph["Zerind"]["Oradea"] = 71

early_graph["Sibiu"]["Oradea"] = 151
early_graph["Sibiu"]["Arad"] = 140
early_graph["Sibiu"]["Fagaras"] = 99
early_graph["Sibiu"]["Rimnicu Vilcea"] = 80

early_graph["Arad"]["Timisoara"] = 118
early_graph["Arad"]["Zerind"] = 175
early_graph["Arad"]["Sibiu"] = 140

early_graph["Timisoara"]["Lugoj"] = 111
early_graph["Timisoara"]["Arad"] = 118

early_graph["Lugoj"]["Mehadia"] = 70
early_graph["Lugoj"]["Timisoara"] = 111

early_graph["Mehadia"]["Dobreta"] = 75
early_graph["Mehadia"]["Lugoj"] = 70

early_graph["Dobreta"]["Craiova"] = 120
early_graph["Dobreta"]["Mehadia"] =75

early_graph["Craiova"]["Dobreta"] = 120
early_graph["Craiova"]["Rimnicu Vilcea"] = 146
early_graph["Craiova"]["Pitesti"] = 138

early_graph["Rimnicu Vilcea"]["Pitesti"] = 97
early_graph["Rimnicu Vilcea"]["Sibiu"] = 80
early_graph["Rimnicu Vilcea"]["Craiova"] = 146

early_graph["Pitesti"]["Bucharest"] = 101
early_graph["Pitesti"]["Rimnicu Vilcea"] = 97
early_graph["Pitesti"]["Craiova"] = 138

early_graph["Fagaras"]["Bucharest"] = 211
early_graph["Fagaras"]["Sibiu"] = 99

early_graph["Bucharest"]["Girgiu"] = 90
early_graph["Bucharest"]["Pitesti"] = 101
early_graph["Bucharest"]["Fagaras"] = 211
early_graph["Bucharest"]["Urziceni"] = 85

early_graph["Girgiu"]["Bucharest"] = 90

early_graph["Urziceni"]["Bucharest"] = 85
early_graph["Urziceni"]["Vaslui"] = 142
early_graph["Urziceni"]["Hirsova"] = 98

early_graph["Hirsova"]["Eforie"] = 86
early_graph["Hirsova"]["Urziceni"] = 98

early_graph["Eforie"]["Hirsova"] = 86

early_graph["Vaslui"]["Iasi"] = 92
early_graph["Vaslui"]["Urziceni"] = 142

early_graph["Iasi"]["Neamt"] = 87
early_graph["Iasi"]["Vaslui"] = 92

early_graph["Neamt"]["Iasi"] = 87


graph = Graph(knots, early_graph)
preceding_knot, road_short = dijkstra_algorithm(graph=graph, starting_city="Urziceni")
print_result(preceding_knot, road_short, starting_city="Urziceni", target_knot="Iasi")
