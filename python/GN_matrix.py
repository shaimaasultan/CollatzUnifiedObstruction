import numpy as np

def v2(n):
    """Return the exponent of 2 dividing n."""
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_next_odd(x):
    """Return the next odd number after applying the Collatz odd step."""
    y = 3*x + 1
    return y >> v2(y)   # divide by 2^v2(y)

def build_collatz_matrix(N):
    """
    Build the odd-to-odd Collatz transition matrix modulo N.
    
    Returns:
        states: list of odd residues modulo N
        A: adjacency matrix (0/1)
        P: Markov matrix (each row sums to 1)
    """
    # All odd residues mod N
    states = [r for r in range(N) if r % 2 == 1]
    k = len(states)

    # Map residue -> index
    index = {s: i for i, s in enumerate(states)}

    # Initialize adjacency matrix
    A = np.zeros((k, k), dtype=int)

    # Build transitions
    for r in states:
        nxt = collatz_next_odd(r) % N
        if nxt % 2 == 1:  # ensure odd
            i = index[r]
            j = index[nxt]
            A[i, j] = 1

    # Markov matrix (deterministic: each row has exactly one 1)
    P = A.astype(float)

    return states, A, P


# Example usage:
if __name__ == "__main__":
    N = 30
    states, A, P = build_collatz_matrix(N)

    print("Odd states mod", N, ":", states)
    print("\nAdjacency matrix A:")
    print(A)
    print("\nMarkov matrix P:")
    print(P)


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def v2(n):
    """Return exponent of 2 dividing n."""
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_next_odd(x):
    """Return next odd after Collatz odd step."""
    y = 3*x + 1
    return y >> v2(y)

def build_collatz_matrix(N):
    """Return odd states, adjacency matrix A, and Markov matrix P."""
    states = [r for r in range(N) if r % 2 == 1]
    k = len(states)
    index = {s: i for i, s in enumerate(states)}

    A = np.zeros((k, k), dtype=int)

    for r in states:
        nxt = collatz_next_odd(r) % N
        if nxt % 2 == 1:
            A[index[r], index[nxt]] = 1

    P = A.astype(float)
    return states, A, P

def plot_collatz_graph(N):
    """Plot the odd-to-odd Collatz graph modulo N."""
    states, A, _ = build_collatz_matrix(N)

    G = nx.DiGraph()

    # Add nodes
    for s in states:
        G.add_node(s)

    # Add edges
    for i, s in enumerate(states):
        for j, t in enumerate(states):
            if A[i, j] == 1:
                G.add_edge(s, t)

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


# Example:
if __name__ == "__main__":
    plot_collatz_graph(900)
