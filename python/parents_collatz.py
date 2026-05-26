from collections import defaultdict

def odd_child(y):
    # always valid
    return 2*y - 1

def even_child(y):
    # y = (3n + 2)/2  =>  n = (2y - 2)/3, must be even and > 0
    num = 2*y - 2
    if num % 3 != 0:
        return None
    n = num // 3
    return n if n % 2 == 0 and n > 0 else None

def next_level_from_parents(current_level):
    """
    Given a list of nodes at current level (y's),
    return:
      - next_level: list of all children (unique)
      - one_child_nodes: nodes in current_level with exactly 1 child
      - two_child_nodes: nodes in current_level with exactly 2 children
      - children_map: dict[y] = list of its children
    """
    children_map = {}
    all_children = set()

    for y in current_level:
        c1 = odd_child(y)
        c2 = even_child(y)

        children = [c1]
        if c2 is not None:
            children.append(c2)

        children_map[y] = children
        all_children.update(children)

    one_child_nodes = [y for y, ch in children_map.items() if len(ch) == 1]
    two_child_nodes = [y for y, ch in children_map.items() if len(ch) == 2]

    return sorted(all_children), sorted(one_child_nodes), sorted(two_child_nodes), children_map

def explore_tree_by_children(roots, max_depth):
    """
    roots: list of starting nodes (e.g. [4, 7] or [1, 4, 7])
    max_depth: how many levels downward (preimages) to generate
    """
    level = list(roots)
    results = []

    for d in range(1, max_depth + 1):
        next_level, one_child, two_children, children_map = next_level_from_parents(level)

        results.append({
            "depth": d,
            "current_level": sorted(level),
            "next_level": next_level,
            "one_child_count": len(one_child),
            "two_child_count": len(two_children),
            "one_child_nodes": one_child,
            "two_child_nodes": two_children,
        })

        level = next_level

    return results


results = explore_tree_by_children(roots=[4, 7], max_depth=3)

for r in results:
    print(f"Depth {r['depth']}:")
    print("  current level:", r["current_level"])
    print("  next level:", r["next_level"])
    print("  nodes with 1 child:", r["one_child_nodes"])
    print("  nodes with 2 children:", r["two_child_nodes"])
    print()


