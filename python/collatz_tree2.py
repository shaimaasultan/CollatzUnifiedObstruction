import networkx as nx
import matplotlib.pyplot as plt
from collections import deque, defaultdict

def f(n):
    if n % 2 == 0:
        return (3*n + 2) // 2
    else:
        return (n + 1) // 2

def preimages(y):
    res = []

    # odd preimage
    x1 = 2*y - 1
    if x1 > 0:
        res.append(x1)

    # even preimage
    num = 2*y - 2
    if num % 3 == 0:
        x2 = num // 3
        if x2 > 0 and x2 % 2 == 0:
            res.append(x2)

    return res


def deep_hierarchical_layout(G, roots):
    """A layout that stays readable even at depth 15–20."""
    pos = {}
    layers = defaultdict(list)
    visited = set()
    q = deque()

    # Roots at depth 0
    for i, r in enumerate(roots):
        pos[r] = (i * 4, 0)
        q.append((r, 0))
        visited.add(r)
        layers[0].append(r)

    # BFS layering
    while q:
        node, depth = q.popleft()
        for child in G.predecessors(node):
            if child not in visited:
                visited.add(child)
                layers[depth + 1].append(child)
                q.append((child, depth + 1))

    # Assign positions with widening spacing
    for depth, nodes in layers.items():
        width = len(nodes)
        spacing = max(3, depth * 0.8)   # widen deeper layers
        start_x = -spacing * (width - 1) / 2

        for i, node in enumerate(nodes):
            pos[node] = (start_x + i * spacing, -depth)

    return pos


def draw_preimage_tree(max_depth=12):
    roots = (1, 4, 7)
    G = nx.DiGraph()
    q = deque()

    for r in roots:
        q.append((r, 0))
        G.add_node(r)

    while q:
        y, depth = q.popleft()
        if depth >= max_depth:
            continue

        for x in preimages(y):
            G.add_edge(x, y)
            q.append((x, depth + 1))

    pos = deep_hierarchical_layout(G, roots)

    # Color coding
    colors = []
    for node in G.nodes():
        if node == 1:
            colors.append("gold")
        elif node in (4, 7):
            colors.append("tomato")
        elif node % 2 == 0:
            colors.append("skyblue")
        else:
            colors.append("lightgreen")

    plt.figure(figsize=(20, 16))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=1300,
        font_size=10,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=14,
        linewidths=1.2,
        edgecolors="black"
    )
    plt.title(f"Preimage Tree (Depth {max_depth})", fontsize=18)
    plt.show()


# Run deeper
draw_preimage_tree(max_depth=9)
