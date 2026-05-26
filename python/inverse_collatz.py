import networkx as nx
import matplotlib.pyplot as plt

def branching_ks(m, depth_limit):
    """Return all valid k values (branching levels) up to depth_limit."""
    if m % 3 == 0:
        return []  # pure even spine, no odd ancestors

    ks = []
    start = 0 if (m % 3 == 1) else 1  # even k for m≡1, odd k for m≡2

    for k in range(start, depth_limit + 1, 2):
        ks.append(k)

    return ks


def build_inverse_tree(m, depth_limit):
    """
    Build the inverse Collatz tree from odd root m up to depth_limit.
    Returns a list of (parent_odd, child_odd, k).
    """
    edges = []
    ks = branching_ks(m, depth_limit)

    for k in ks:
        N = m * (2 ** k)
        odd_parent = (N - 1) // 3
        edges.append((odd_parent, m, k))

    return edges


def draw_tree(m, depth_limit):
    edges = build_inverse_tree(m, depth_limit)

    G = nx.DiGraph()
    for parent, child, k in edges:
        G.add_edge(parent, child, label=f"k={k}")

    pos = nx.spring_layout(G, seed=42, k=1.2)

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=1500,
            node_color="lightblue", font_size=10, arrows=True)

    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    plt.title(f"Inverse Collatz Tree from m={m} (depth={depth_limit})")
    plt.axis("off")
    plt.show()


# Example usage:
draw_tree(m=17, depth_limit=15)
