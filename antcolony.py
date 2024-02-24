import networkx as nx
from pyvis.network import Network

# Step 1: Parse the edges file
edges_file = "insecta-ant-colony5-day27.edges"

edges = []
with open(edges_file, "r") as file:
    for line in file:
        source, target, weight = map(int, line.split())  # Convert to integers
        edges.append((source, target, weight))

# Step 2: Create a networkx graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Step 3: Use pyvis to visualize the network
net = Network(height='800px', width='100%', notebook=True)

# Step 4: Add nodes and edges to the Pyvis network
# Assign vibrant colors to the nodes and edges
vibrant_colors = ['#FF1493', '#00FFFF', '#39FF14', '#FFA500']  # Pink, Neon Blue, Neon Green, Orange

for node in G.nodes():
    color = vibrant_colors[node % len(vibrant_colors)]  # Cycle through the vibrant colors for each node
    net.add_node(node, color=color)

for edge in G.edges(data=True):
    source, target, weight = edge
    color = vibrant_colors[int(weight['weight']) % len(vibrant_colors)]  # Use weight to determine edge color
    net.add_edge(source, target, value=weight['weight'], color=color)

# Step 5: Customize visualization
net.show_buttons(filter_=['nodes', 'edges', 'physics'])

# Step 6: Display the visualization
net.show("ant_colony_network.html")
