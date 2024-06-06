import networkx as nx
import matplotlib.pyplot as plt
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def search2(start,key):
    stk=[]
    node=start
    stk.append(node)
    used=[]
    bfs_order=[]
    while True:
        if len(stk)==0:
            break
        print ("stack", stk)
        node=stk.pop(0)
        used.append(node)
        print(node) 
        bfs_order.append(node)   
        if node == key:
            print("found",used)
            break
        nbs=graph[node]
        for nb in reversed(nbs):
            if nb not in used:
                stk.insert(0,nb)
                
    print("bfs_order!!!!!!!!!!!!!!!!!!!!!",bfs_order)
    return bfs_order
                
def visualize_bfs(graph, bfs_order):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
    
    edges = [(bfs_order[i], bfs_order[i + 1]) for i in range(len(bfs_order) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=bfs_order, node_color='lightgreen', node_size=2000)

    plt.title('Graph BFS Traversal')
    plt.show()   
    
    
    
bfs_order=search2("A","E")
print("BFS Order:", bfs_order)
visualize_bfs(graph, bfs_order)