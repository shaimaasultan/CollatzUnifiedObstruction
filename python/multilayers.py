import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def build_collatz_automaton(N, K):
    """
    Build the true Collatz automaton with states (r mod N, v2 mod K).
    
    Returns:
        states: list of (r, k)
        edges: list of (state -> next_state)
        G: networkx DiGraph
    """
    # All odd residues mod N
    odd_residues = [r for r in range(N) if r % 2 == 1]

    # Build state space
    states = [(r, k) for r in odd_residues for k in range(K)]

    # Map state -> index
    index = {s: i for i, s in enumerate(states)}

    G = nx.DiGraph()

    for (r, k) in states:
        # Compute 3r+1 in extended modulus
        y = 3*r + 1

        # Compute v2 layer
        v = v2(y) % K

        # Compute next odd residue
        y_reduced = y >> v
        r_next = y_reduced % N

        # Only keep odd residues
        if r_next % 2 == 1:
            next_state = (r_next, v)
            G.add_edge((r, k), next_state)

    return states, G

# Example:
if __name__ == "__main__":
    N= 30
    K =4
    states , G = build_collatz_automaton(N, K)
    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Draw
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)

    plt.title(f"Odd-to-Odd Collatz Graph mod {N}")
    plt.axis("off")
    plt.show()


    import networkx as nx

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def build_collatz_automaton(N, K):
    """
    Build the true Collatz automaton with states (r mod N, v2 mod K).
    Returns a directed graph G.
    """
    odd_residues = [r for r in range(N) if r % 2 == 1]
    states = [(r, k) for r in odd_residues for k in range(K)]

    G = nx.DiGraph()

    for (r, k) in states:
        y = 3*r + 1
        v = v2(y) % K
        y_reduced = y >> v
        r_next = y_reduced % N

        if r_next % 2 == 1:
            G.add_edge((r, k), (r_next, v))

    return G


def find_cycles_and_attractors(G):
    """
    Given a deterministic directed graph G,
    return:
      - list of cycles (each cycle is a list of states)
      - attractors (cycles with no outgoing edges to other cycles)
      - basins (mapping: state -> attractor)
    """
    # 1. Find all simple cycles
    cycles = list(nx.simple_cycles(G))

    # Convert cycles to tuples for hashing
    cycles = [tuple(cycle) for cycle in cycles]

    # 2. Identify attractors
    attractors = []
    for cyc in cycles:
        is_attractor = True
        for node in cyc:
            for _, nxt in G.out_edges(node):
                if nxt not in cyc:
                    is_attractor = False
                    break
        if is_attractor:
            attractors.append(cyc)

    # 3. Compute basins of attraction
    basins = {}
    for node in G.nodes():
        current = node
        visited = set()
        while current not in visited:
            visited.add(current)
            out_edges = list(G.out_edges(current))
            if not out_edges:
                break
            current = out_edges[0][1]

        # current is now in a cycle
        for cyc in attractors:
            if current in cyc:
                basins[node] = cyc
                break

    return cycles, attractors, basins


# Example usage:
if __name__ == "__main__":
    N = 30
    K = 4

    G = build_collatz_automaton(N, K)
    cycles, attractors, basins = find_cycles_and_attractors(G)

    print("Cycles:")
    for c in cycles:
        print(c)

    print("\nAttractors:")
    for a in attractors:
        print(a)

    print("\nExample basin entry:")
    some_state = list(G.nodes())[0]
    print(some_state, "→", basins[some_state])


import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def build_collatz_automaton(N, K):
    """
    Build the true Collatz automaton with states (r mod N, v2 mod K).
    Returns a directed graph G.
    """
    odd_residues = [r for r in range(N) if r % 2 == 1]
    states = [(r, k) for r in odd_residues for k in range(K)]

    G = nx.DiGraph()

    for (r, k) in states:
        y = 3*r + 1
        v = v2(y) % K
        y_reduced = y >> v
        r_next = y_reduced % N

        if r_next % 2 == 1:
            G.add_edge((r, k), (r_next, v))

    return G


def plot_collatz_automaton_layers(N, K):
    """
    Plot the Collatz automaton with nodes arranged in v2 layers.
    """
    G = build_collatz_automaton(N, K)

    # Build layered positions
    pos = {}
    layer_nodes = {k: [] for k in range(K)}

    # Group nodes by v2 layer
    for (r, k) in G.nodes():
        layer_nodes[k].append((r, k))

    # Assign coordinates
    for k in range(K):
        nodes = layer_nodes[k]
        for i, node in enumerate(nodes):
            pos[node] = (i, -k)   # x = index, y = -layer

    # Colors per layer
    colors = []
    for (r, k) in G.nodes():
        colors.append(k)

    plt.figure(figsize=(14, 8))
    nx.draw(
        G, pos,
        with_labels=True,
        labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
        node_color=colors,
        cmap=plt.cm.viridis,
        node_size=600,
        arrowsize=12,
        font_size=8
    )

    plt.title(f"Collatz Automaton (mod {N}) with {K} v₂ Layers")
    plt.axis("off")
    plt.show()


# Example:
if __name__ == "__main__":
    plot_collatz_automaton_layers(N=40, K=5)


import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def build_collatz_automaton(N, K):
    """
    Build the true Collatz automaton with states (r mod N, v2 mod K).
    Returns a directed graph G.
    """
    odd_residues = [r for r in range(N) if r % 2 == 1]
    states = [(r, k) for r in odd_residues for k in range(K)]

    G = nx.DiGraph()

    for (r, k) in states:
        y = 3*r + 1
        v = v2(y) % K
        y_reduced = y >> v
        r_next = y_reduced % N

        if r_next % 2 == 1:
            G.add_edge((r, k), (r_next, v))

    return G


def plot_collatz_automaton_bands(N, K):
    """
    Plot the Collatz automaton with each v2 layer in its own horizontal band.
    """
    G = build_collatz_automaton(N, K)

    # Group nodes by layer
    layers = {k: [] for k in range(K)}
    for (r, k) in G.nodes():
        layers[k].append((r, k))

    # Compute positions: evenly spaced horizontally, fixed y per layer
    pos = {}
    for k in range(K):
        nodes = layers[k]
        count = len(nodes)
        for i, node in enumerate(nodes):
            x = i  # horizontal spacing
            y = -k  # vertical band
            pos[node] = (x, y)

    # Color nodes by layer
    colors = [k for (_, k) in G.nodes()]

    plt.figure(figsize=(18, 10))
    nx.draw(
        G, pos,
        with_labels=True,
        labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
        node_color=colors,
        cmap=plt.cm.plasma,
        node_size=700,
        arrowsize=12,
        font_size=8
    )

    plt.title(f"Collatz Automaton (mod {N}) with {K} v₂ Layers — Horizontal Bands")
    plt.axis("off")
    plt.show()


# Example:
if __name__ == "__main__":
    plot_collatz_automaton_bands(N=30, K=5)


import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def build_collatz_automaton(N, K):
    """
    Build the true Collatz automaton with states (r mod N, v2 mod K).
    Returns a directed graph G.
    """
    odd_residues = [r for r in range(N) if r % 2 == 1]
    states = [(r, k) for r in odd_residues for k in range(K)]

    G = nx.DiGraph()

    for (r, k) in states:
        y = 3*r + 1
        v = v2(y) % K
        y_reduced = y >> v
        r_next = y_reduced % N

        if r_next % 2 == 1:
            G.add_edge((r, k), (r_next, v))

    return G


def find_cycles_and_attractors(G):
    """
    Return:
      - cycles: list of cycles (each cycle is a tuple of states)
      - attractors: cycles with no outgoing edges to outside nodes
    """
    cycles = [tuple(c) for c in nx.simple_cycles(G)]

    attractors = []
    for cyc in cycles:
        is_attractor = True
        for node in cyc:
            for _, nxt in G.out_edges(node):
                if nxt not in cyc:
                    is_attractor = False
                    break
        if is_attractor:
            attractors.append(cyc)

    return cycles, attractors


def plot_collatz_automaton_bands_with_cycles(N, K):
    """
    Plot the Collatz automaton with:
      - horizontal v2 bands
      - attractor cycles highlighted in red
      - cycle edges thickened
    """
    G = build_collatz_automaton(N, K)
    cycles, attractors = find_cycles_and_attractors(G)

    # Flatten attractor nodes
    attractor_nodes = set()
    for cyc in attractors:
        for node in cyc:
            attractor_nodes.add(node)

    # Flatten cycle edges
    cycle_edges = set()
    for cyc in cycles:
        for i in range(len(cyc)):
            a = cyc[i]
            b = cyc[(i+1) % len(cyc)]
            cycle_edges.add((a, b))

    # Group nodes by layer
    layers = {k: [] for k in range(K)}
    for (r, k) in G.nodes():
        layers[k].append((r, k))

    # Compute positions
    pos = {}
    for k in range(K):
        nodes = layers[k]
        for i, node in enumerate(nodes):
            pos[node] = (i, -k)

    # Node colors
    node_colors = []
    for node in G.nodes():
        if node in attractor_nodes:
            node_colors.append("red")
        else:
            node_colors.append("lightgray")

    # Draw base graph
    plt.figure(figsize=(18, 10))

    # Draw non-cycle edges
    normal_edges = [e for e in G.edges() if e not in cycle_edges]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=normal_edges,
        edge_color="black",
        arrowsize=10,
        width=1
    )

    # Draw cycle edges thicker
    nx.draw_networkx_edges(
        G, pos,
        edgelist=list(cycle_edges),
        edge_color="red",
        arrowsize=15,
        width=3
    )

    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=700
    )

    # Labels
    nx.draw_networkx_labels(
        G, pos,
        labels={node: f"{node[0]}|v2={node[1]}" for node in G.nodes()},
        font_size=8
    )

    plt.title(f"Collatz Automaton (mod {N}) with {K} v₂ Layers — Cycles Highlighted")
    plt.axis("off")
    plt.show()


# Example:
if __name__ == "__main__":
    plot_collatz_automaton_bands_with_cycles(N=30, K=5)





