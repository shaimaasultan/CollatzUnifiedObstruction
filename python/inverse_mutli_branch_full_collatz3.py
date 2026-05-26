def odd_parents(n):
    """
    Return all odd parents of n under the Collatz map.
    Solve 3o + 1 = n * 2^k  →  o = (n*2^k - 1)/3
    Only keep integer odd o.
    """
    parents = []
    k = 1
    while True:
        N = n * (2 ** k)
        if (N - 1) % 3 == 0:
            o = (N - 1) // 3
            if o % 2 == 1:
                parents.append(o)
        if N > 10**12:
            break
        k += 1
    return parents


def build_inverse_tree(root, depth_limit=1, recursive=True, prune_empty=True):
    """
    Build inverse Collatz tree for any root.

    Parameters:
        root (int)        : starting node
        depth_limit (int) : recursion depth
        recursive (bool)  : True = full tree, False = only m-branch
        prune_empty (bool): remove nodes with no parents

    Returns:
        dict: node → list of parents
    """
    tree = {}
    frontier = [(root, 0)]
    visited = set([root])

    while frontier:
        n, depth = frontier.pop()

        # compute parents of n
        parents = []

        # even parent always exists
        even_parent = n * 2
        parents.append(even_parent)

        # odd parents
        for o in odd_parents(n):
            parents.append(o)

        # prune nodes with no parents
        if prune_empty and len(parents) == 0:
            continue

        tree[n] = parents

        # stop recursion if disabled
        if not recursive:
            continue

        # stop recursion at depth limit
        if depth >= depth_limit:
            continue

        # expand upward
        for p in parents:
            if p not in visited:
                visited.add(p)
                frontier.append((p, depth + 1))

    return tree


# Example usage:
def print_tree(m,depth,recursive =False,prune_empty=True):
    tree = build_inverse_tree(m, depth_limit=depth, recursive=recursive, prune_empty=prune_empty)
    if recursive:
        print("only m-branch:\n")
    else:   
         print(f"Only m-branch tree from m={m} up to depth {depth}:\n")

    for node, parents in tree.items():
        print(f"{node} <- {parents}")



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
    return "gray"  # even numbers or other endings

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
# Draw m-branch only
# -----------------------------
def visualize_m_branch(m ,depth_limit=1, recursive=False, prune_empty=False):
    odd_parents = odd_parents_with_k(m)
    # Build m-branch only (recursive=False)
    tree = build_inverse_tree(m, depth_limit=depth_limit, recursive=recursive, prune_empty=prune_empty)

    parents = tree[m]

    G = nx.DiGraph()

    # Add root
    G.add_node(m, color=color_for_last_digit(m))

    # Add parents
    for p in parents:
        G.add_node(p, color=color_for_last_digit(p))
        G.add_edge(p, m)

    # Extract colors
    colors = [G.nodes[n]["color"] for n in G.nodes]

    # Layout
    pos = nx.spring_layout(G, seed=42, k=1.2)

    plt.figure(figsize=(14, 10))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=1500,
        font_size=10,
        arrows=True
    )

    plt.title(f"Inverse Collatz m-branch for m={m}\nColor-coded by last digit (1,3,5,7,9)")
    plt.axis("off")
    plt.show()


# -----------------------------
# Example: visualize all m in your list
# -----------------------------
ms = [3,5,7]
m=3
depth=1
recursive=False

for m in ms:
    visualize_m_branch(m, depth_limit=depth, recursive=recursive, prune_empty=False)
