import networkx as nx
import matplotlib.pyplot as plt


# -----------------------------
# Color map by last digit
# -----------------------------
def color_for_last_digit(n):
    last = n % 10
    if last == 1:
        return "gold"
    if last == 3:
        return "red"
    if last == 5:
        return "green"
    if last == 7:
        return "blue"
    if last == 9:
        return "purple"
    return "gray"  # fallback (should not happen for odd nodes)


# -----------------------------
# Compute odd parents WITH k-values
# -----------------------------
def odd_parents_with_k(n):
    parents = []
    k = 1
    while True:
        N = n * (2 ** k)
        if (N - 1) % 3 == 0:
            o = (N - 1) // 3
            if o % 2 == 1:  # odd only
                parents.append((o, k))
        if N > 10**12:
            break
        k += 1
    return parents


# -----------------------------
# Build ONE combined graph
# -----------------------------
def build_combined_graph(m_list):
    G = nx.DiGraph()

    for m in m_list:
        # Add root node
        G.add_node(m, color=color_for_last_digit(m))

        # Add odd parents only
        for o, k in odd_parents_with_k(m):
            G.add_node(o, color=color_for_last_digit(o))
            G.add_edge(o, m, label=f"k={k}")

    return G


# -----------------------------
# Visualize combined graph
# -----------------------------
def visualize_combined_graph(m_list):
    G = build_combined_graph(m_list)

    # Extract colors
    colors = [G.nodes[n]["color"] for n in G.nodes]

    # Layout
    pos = nx.spring_layout(G, seed=42, k=1.2)

    plt.figure(figsize=(18, 14))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=1400,
        font_size=9,
        arrows=True
    )

    # Edge labels (k-values)
    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Combined Odd‑Only Inverse Collatz Graph\n(All m‑branches merged, edges labeled with k)")
    plt.axis("off")
    plt.show()


# -----------------------------
# Run on your full list
# -----------------------------
m_values = [3,5,7,11]

visualize_combined_graph(m_values)
