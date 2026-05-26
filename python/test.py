import networkx as nx
import matplotlib.pyplot as plt
from collections import deque, defaultdict

def f(n , a =2, b=1 ):
    if n % 2 == 0:
        return (3*n + a) // 2
    else:
        return (n + b) // 2

def mod6_color(n):
    r = n % 6
    if r == 0:
        return "#0000FF"   # blue
    elif r == 1:
        return "#FF0000"   # red
    elif r == 2:
        return "#00AA00"   # green
    elif r == 3:
        return "#AA00AA"   # purple
    elif r == 4:
        return "#FF8800"   # orange
    elif r == 5:
        return "#008888"   # teal



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


def hierarchical_layout(G, roots):
    """Produce a clean layered layout."""
    pos = {}
    layers = defaultdict(list)
    visited = set()
    q = deque()

    # Initialize roots at depth 0
    for i, r in enumerate(roots):
        pos[r] = (i * 3, 0)
        q.append((r, 0))
        visited.add(r)
        layers[0].append(r)

    # BFS to assign layers
    while q:
        node, depth = q.popleft()
        for child in G.predecessors(node):
            if child not in visited:
                visited.add(child)
                layers[depth + 1].append(child)
                q.append((child, depth + 1))

    # Assign x positions inside each layer
    for depth, nodes in layers.items():
        width = len(nodes)
        start_x = -1.5 * (width - 1)
        for i, node in enumerate(nodes):
            pos[node] = (start_x + i * 3, -depth)

    return pos


def draw_preimage_tree(max_depth=10):
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

    pos = hierarchical_layout(G, roots)

    # Color coding
    colors = []
    for node in G.nodes():
        if node == 1:
            colors.append("gold")        # fixed point
        elif node in (4, 7):
            colors.append("tomato")      # 2-cycle
        elif node % 2 == 0:
            colors.append("skyblue")     # even
        else:
            colors.append("lightgreen")  # odd

    # inside draw_preimage_tree(), replace your color loop with this:

    colors = [mod6_color(node) for node in G.nodes()]
    plt.figure(figsize=(18, 14))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=1200,
        font_size=10,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=15,
        linewidths=1.2,
        edgecolors="black"
    )
    plt.title(f"Preimage Tree for Modified Collatz Map (Depth {max_depth})", fontsize=16)
    plt.show()


# Run it
draw_preimage_tree(max_depth=10)
