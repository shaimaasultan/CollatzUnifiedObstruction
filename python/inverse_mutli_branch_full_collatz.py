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
        if N > 10**12:  # safety cutoff
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
def print_tree(m, depth_limit,recursive =False):
    tree = build_inverse_tree(m , depth_limit, recursive=recursive  )
    if recursive:
        print(f"Full recursive tree from m={m} up to depth {depth_limit}:")
    else:
        print(f"m-branch only from m={m}:") 
    for node, parents in tree.items():
        print(f"{node} <- {parents}")
        
print_tree(m=15, depth_limit=1, recursive=True)
