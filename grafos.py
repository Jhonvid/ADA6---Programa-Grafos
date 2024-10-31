import networkx as nx
import matplotlib.pyplot as plt

estados = ["Oaxaca", "Chiapas", "Guerrero", "Tabasco", "Campeche", "Yucatán", "Quintana Roo"]
conexiones = [
    ("Oaxaca", "Chiapas", 250),
    ("Oaxaca", "Guerrero", 300),
    ("Chiapas", "Tabasco", 150),
    ("Tabasco", "Campeche", 200),
    ("Campeche", "Yucatán", 180),
    ("Yucatán", "Quintana Roo", 120),
    ("Guerrero", "Campeche", 310),
    ("Oaxaca", "Yucatán", 500),
    ("Chiapas", "Quintana Roo", 350),
    ("Guerrero", "Quintana Roo", 400)
]

# Crear el grafo
G = nx.Graph()

#nodos y aristas con los pesos
for estado in estados:
    G.add_node(estado)

for (origen, destino, costo) in conexiones:
    G.add_edge(origen, destino, weight=costo)

# encontrar un recorrido por todos los estados sin repetir 
def recorrido_sin_repetir(grafo, inicio):
    try:
        camino = list(nx.dfs_edges(grafo, inicio))  # Usar DFS para crear el camino
        recorrido = [inicio] + [destino for _, destino in camino]
        costo_total = sum(grafo[origen][destino]["weight"] for origen, destino in camino)
        return recorrido, costo_total
    except nx.NetworkXNoPath:
        return None, float('inf')

# un recorrido por todos los estados permitiendo repeticiones
def recorrido_con_repeticion(grafo, inicio):
    try:
        camino = list(nx.dfs_edges(grafo, inicio))
        recorrido = [inicio] + [destino for _, destino in camino] + [inicio]  # Volver al inicio para repetir uno
        costo_total = sum(grafo[origen][destino]["weight"] for origen, destino in camino) * 2
        return recorrido, costo_total
    except nx.NetworkXNoPath:
        return None, float('inf')

#grafica el grafo
def dibujar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(grafo, "weight")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()

inicio = "Oaxaca"
recorrido_a, costo_a = recorrido_sin_repetir(G, inicio)
recorrido_b, costo_b = recorrido_con_repeticion(G, inicio)

print("Recorrido sin repetir:", recorrido_a)
print("Costo total (sin repetir):", costo_a)
print("\nRecorrido con repetición:", recorrido_b)
print("Costo total (con repetición):", costo_b)

# Dibujar el grafo
dibujar_grafo(G)
