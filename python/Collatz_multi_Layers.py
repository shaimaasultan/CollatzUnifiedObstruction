import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_next(x):
    if x % 2 == 0:
        return x // 2
    y = 3*x + 1
    return y >> v2(y)

def build_true_collatz_automaton(max_value, K):
    """
    Build the TRUE Collatz automaton (no mod N).
    States are (x, v2(x)%K).
    """
    G = nx.DiGraph()

    for x in range(1, max_value+1):
        nxt = collatz_next(x)
        G.add_edge((x, v2(x) % K), (nxt, v2(nxt) % K))

    return G


def plot_true_collatz_with_cycle(max_value=50, K=6):
    """
    Plot the TRUE Collatz automaton with the real 1→4→2→1 cycle highlighted.
    """
    G = build_true_collatz_automaton(max_value, K)

    # True Collatz cycle
    cycle_nodes = {(1, v2(1)%K), (2, v2(2)%K), (4, v2(4)%K)}
    cycle_edges = {
        ((1, v2(1)%K), (4, v2(4)%K)),
        ((4, v2(4)%K), (2, v2(2)%K)),
        ((2, v2(2)%K), (1, v2(1)%K)),
    }

    # Group nodes by v2 layer
    layers = {k: [] for k in range(K)}
    for node in G.nodes():
        layers[node[1]].append(node)

    # Compute positions
    pos = {}
    for k in range(K):
        for i, node in enumerate(layers[k]):
            pos[node] = (i, -k)

    # Node colors
    node_colors = ["red" if node in cycle_nodes else "lightgray"
                   for node in G.nodes()]

    plt.figure(figsize=(20, 12))

    # Draw normal edges
    normal_edges = [e for e in G.edges() if e not in cycle_edges]
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges,
                           edge_color="black", width=1, arrowsize=10)

    # Draw cycle edges
    nx.draw_networkx_edges(G, pos, edgelist=list(cycle_edges),
                           edge_color="red", width=4, arrowsize=20)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

    # Labels
    nx.draw_networkx_labels(
        G, pos,
        labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
        font_size=8
    )

    plt.title("TRUE Collatz Automaton with Explicit 1→4→2→1 Cycle")
    plt.axis("off")
    plt.show()

    return G, cycle_nodes, cycle_edges, pos

plot_true_collatz_with_cycle(max_value=30, K=4)

# import networkx as nx
# import matplotlib.pyplot as plt

# def v2(n):
#     c = 0
#     while n % 2 == 0:
#         n //= 2
#         c += 1
#     return c

# def build_full_collatz_automaton(N, K):
#     """
#     Build full Collatz automaton (odd + even) with states (r mod N, v2(r)).
#     v2 is truncated mod K for visualization.
#     """
#     residues = list(range(N))
#     states = [(r, v2(r) % K) for r in residues]

#     G = nx.DiGraph()

#     for (r, k) in states:
#         if r % 2 == 0:
#             # Even step: x -> x/2
#             nxt = (r // 2) % N
#             G.add_edge((r, k), (nxt, v2(nxt) % K))
#         else:
#             # Odd step: x -> (3x+1)/2^v2
#             y = 3*r + 1
#             v = v2(y)
#             nxt = (y >> v) % N
#             G.add_edge((r, k), (nxt, v2(nxt) % K))

#     return G


# def plot_full_collatz_with_cycle(N, K):
#     """
#     Plot the full Collatz automaton (odd + even) with the true 1→4→2→1 cycle highlighted.
#     Returns a dict containing the graph, cycle nodes, cycle edges, and layout positions.
#     """
#     G = build_full_collatz_automaton(N, K)

#     # True Collatz cycle
#     cycle_nodes = {
#         (1 % N, v2(1) % K),
#         (4 % N, v2(4) % K),
#         (2 % N, v2(2) % K)
#     }

#     cycle_edges = {
#         ((1 % N, v2(1) % K), (4 % N, v2(4) % K)),
#         ((4 % N, v2(4) % K), (2 % N, v2(2) % K)),
#         ((2 % N, v2(2) % K), (1 % N, v2(1) % K)),
#     }

#     # Group nodes by v2 layer
#     layers = {k: [] for k in range(K)}
#     for node in G.nodes():
#         layers[node[1]].append(node)

#     # Compute positions
#     pos = {}
#     for k in range(K):
#         nodes = layers[k]
#         for i, node in enumerate(nodes):
#             pos[node] = (i, -k)

#     # Node colors
#     node_colors = ["red" if node in cycle_nodes else "lightgray"
#                    for node in G.nodes()]

#     plt.figure(figsize=(20, 12))

#     # Draw normal edges
#     normal_edges = [e for e in G.edges() if e not in cycle_edges]
#     nx.draw_networkx_edges(G, pos, edgelist=normal_edges,
#                            edge_color="black", width=1, arrowsize=10)

#     # Draw cycle edges
#     nx.draw_networkx_edges(G, pos, edgelist=list(cycle_edges),
#                            edge_color="red", width=4, arrowsize=20)

#     # Draw nodes
#     nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

#     # Labels
#     nx.draw_networkx_labels(
#         G, pos,
#         labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
#         font_size=8
#     )

#     plt.title(f"Full Collatz Automaton (mod {N}) with Explicit 1→4→2→1 Cycle")
#     plt.axis("off")
#     plt.show()

#     return {
#         "graph": G,
#         "cycle_nodes": cycle_nodes,
#         "cycle_edges": cycle_edges,
#         "positions": pos
#     }



# # --- import your functions ---
# #from collatz_automaton import plot_full_collatz_with_cycle

# # --- choose parameters ---
# N = 10      # modulus
# K = 1       # number of v2 layers

# # --- call the visualizer ---
# result = plot_full_collatz_with_cycle(N, K)

# # --- unpack returned data ---
# G           = result["graph"]
# cycle_nodes = result["cycle_nodes"]
# cycle_edges = result["cycle_edges"]
# positions   = result["positions"]

# print("Cycle nodes:", cycle_nodes)
# print("Cycle edges:", cycle_edges)

# import networkx as nx
# import matplotlib.pyplot as plt

# def v2(n):
#     c = 0
#     while n % 2 == 0:
#         n //= 2
#         c += 1
#     return c

# def build_full_collatz_automaton(N, K):
#     residues = list(range(N))
#     states = [(r, v2(r) % K) for r in residues]

#     G = nx.DiGraph()

#     for (r, k) in states:
#         if r % 2 == 0:
#             nxt = (r // 2) % N
#             G.add_edge((r, k), (nxt, v2(nxt) % K))
#         else:
#             y = 3*r + 1
#             v = v2(y)
#             nxt = (y >> v) % N
#             G.add_edge((r, k), (nxt, v2(nxt) % K))

#     return G


# def plot_full_collatz_with_cycle(N, K):
#     G = build_full_collatz_automaton(N, K)

#     # True Collatz cycle
#     cycle_nodes = {
#         (1 % N, v2(1) % K),
#         (4 % N, v2(4) % K),
#         (2 % N, v2(2) % K)
#     }

#     cycle_edges = {
#         ((1 % N, v2(1) % K), (4 % N, v2(4) % K)),
#         ((4 % N, v2(4) % K), (2 % N, v2(2) % K)),
#         ((2 % N, v2(2) % K), (1 % N, v2(1) % K)),
#     }

#     # Group nodes by v2 layer
#     layers = {k: [] for k in range(K)}
#     for node in G.nodes():
#         layers[node[1]].append(node)

#     # Compute positions
#     pos = {}
#     for k in range(K):
#         nodes = layers[k]
#         for i, node in enumerate(nodes):
#             pos[node] = (i, -k)

#     # Node colors
#     node_colors = ["red" if node in cycle_nodes else "lightgray"
#                    for node in G.nodes()]

#     plt.figure(figsize=(20, 12))

#     # Draw normal edges
#     normal_edges = [e for e in G.edges() if e not in cycle_edges]
#     nx.draw_networkx_edges(G, pos, edgelist=normal_edges,
#                            edge_color="black", width=1, arrowsize=10)

#     # Draw cycle edges
#     nx.draw_networkx_edges(G, pos, edgelist=list(cycle_edges),
#                            edge_color="red", width=4, arrowsize=20)

#     # Draw nodes
#     nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

#     # Labels
#     nx.draw_networkx_labels(
#         G, pos,
#         labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
#         font_size=8
#     )

#     plt.title(f"Full Collatz Automaton (mod {N}) with Explicit 1→4→2→1 Cycle")
#     plt.axis("off")
#     plt.show()

#     # ⭐ Return everything
#     return {
#         "graph": G,
#         "cycle_nodes": cycle_nodes,
#         "cycle_edges": cycle_edges,
#         "positions": pos
#     }


# # Example:
# if __name__ == "__main__":
#     result = plot_full_collatz_with_cycle(N=30, K=6)
#     print(result.keys())
