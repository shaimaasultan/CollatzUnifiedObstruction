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


def hierarchical_layout(G, root_positions):
    """
    Create a clean hierarchical layout for the tree.
    root_positions: dict {node: (x, y)} for depth 0
    """
    pos = {}
    pos.update(root_positions)

    # BFS layering
    layers = defaultdict(list)
    visited = set(root_positions.keys())
    q = deque([(node, 0) for node in root_positions])

    while q:
        node, depth = q.popleft()
        layers[depth].append(node)

        for child in G.predecessors(node):
            if child not in visited:
                visited.add(child)
                q.append((child, depth + 1))

    # Assign positions layer by layer
    for depth, nodes in layers.items():
        x_spacing = 2.0
        start_x = -x_spacing * (len(nodes) - 1) / 2
        for i, node in enumerate(nodes):
            pos[node] = (start_x + i * x_spacing, -depth)

    return pos


def draw_preimage_tree(roots=(1,4,7), max_depth=6):
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

    # Root positions (top row)
    root_positions = {r: (i * 3, 0) for i, r in enumerate(roots)}

    pos = hierarchical_layout(G, root_positions)

    plt.figure(figsize=(16, 12))
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=1200,
        font_size=10,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=15
    )
    plt.title("Hierarchical Preimage Tree for Modified Collatz Map")
    plt.show()


# Run it
draw_preimage_tree(max_depth=10)
