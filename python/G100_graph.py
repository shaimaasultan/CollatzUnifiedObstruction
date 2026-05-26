# ---------------------------------------------
# Accelerated Collatz map T(n)
# ---------------------------------------------

def v2(m: int) -> int:
    """Exponent of 2 dividing m."""
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def T(n: int) -> int:
    """Accelerated Collatz map."""
    if n % 2 == 0:
        return n // 2
    m = 3*n + 1
    return m // (2 ** v2(m))


# ---------------------------------------------
# Build the 100-node Collatz graph G_100
# ---------------------------------------------

def build_G100(K: int = 500):
    """
    Build the mod-100 Collatz automaton G_100.

    Vertices: 0..99
    Edge r -> s if ∃ n ≡ r (mod 100) with T(n) ≡ s (mod 100).

    We approximate this by sampling:
        n = r, r+100, r+200, ..., r+100*K
    and collecting all distinct successors s = T(n) mod 100.
    """
    adjacency = {r: set() for r in range(100)}

    for r in range(100):
        for k in range(K + 1):
            n = r + 100*k
            s = T(n) % 100
            adjacency[r].add(s)

    # Convert to sorted lists for readability
    return {r: sorted(list(succs)) for r, succs in adjacency.items()}


G100 = build_G100()

# Optional: print the 100-node layer
for r in range(100):
    print(f"{r:02d} -> {G100[r]}")

print(180 % 100)
# # ------------------------------------------------------------
# #  Accelerated Collatz map
# # ------------------------------------------------------------

# def v2(m: int) -> int:
#     """Return the exponent of 2 dividing m."""
#     k = 0
#     while m % 2 == 0:
#         m //= 2
#         k += 1
#     return k


# def T(n: int) -> int:
#     """Accelerated Collatz map."""
#     if n % 2 == 0:
#         return n // 2
#     m = 3*n + 1
#     return m // (2 ** v2(m))


# # ------------------------------------------------------------
# #  Build G_100
# # ------------------------------------------------------------

# def build_G100(K: int = 500):
#     """
#     Build the mod-100 Collatz automaton G_100.

#     For each residue r in {0,...,99}, sample:
#         n = r, r+100, r+200, ..., r+100*K

#     For each sample, compute T(n) mod 100 and collect all distinct successors.

#     K=500 is usually enough for stabilization.
#     """
#     adjacency = {r: set() for r in range(100)}

#     for r in range(100):
#         for k in range(K + 1):
#             n = r + 100*k
#             s = T(n) % 100
#             adjacency[r].add(s)

#     # Convert sets to sorted lists for readability
#     return {r: sorted(list(succs)) for r, succs in adjacency.items()}


# G100 = build_G100()


# # ------------------------------------------------------------
# #  SCC computation (Kosaraju's algorithm)
# # ------------------------------------------------------------

# def compute_sccs(graph):
#     """
#     Compute strongly connected components of a directed graph
#     given as adjacency dict: node -> list of successors.
#     Returns a list of components, each a set of nodes.
#     """
#     # 1st pass: order by finish time in DFS on original graph
#     visited = set()
#     order = []

#     def dfs1(u):
#         visited.add(u)
#         for v in graph[u]:
#             if v not in visited:
#                 dfs1(v)
#         order.append(u)

#     for node in graph:
#         if node not in visited:
#             dfs1(node)

#     # Build reverse graph
#     rev = {u: [] for u in graph}
#     for u, nbrs in graph.items():
#         for v in nbrs:
#             rev[v].append(u)

#     # 2nd pass: DFS on reversed graph in reverse finish order
#     visited.clear()
#     sccs = []

#     def dfs2(u, comp):
#         visited.add(u)
#         comp.add(u)
#         for v in rev[u]:
#             if v not in visited:
#                 dfs2(v, comp)

#     for u in reversed(order):
#         if u not in visited:
#             comp = set()
#             dfs2(u, comp)
#             sccs.append(comp)

#     return sccs


# sccs = compute_sccs(G100)


# # ------------------------------------------------------------
# #  Classify SCCs: sink SCCs and cycle SCCs
# # ------------------------------------------------------------

# def is_sink_scc(component, graph):
#     """
#     An SCC is a sink if it has no outgoing edges to nodes outside the component.
#     """
#     comp_set = component
#     for u in comp_set:
#         for v in graph[u]:
#             if v not in comp_set:
#                 return False
#     return True


# def is_simple_cycle_scc(component, graph):
#     """
#     Check if an SCC is a simple directed cycle:
#     every node has exactly one successor and one predecessor within the component.
#     """
#     comp_set = component
#     # Count in-degree and out-degree restricted to the component
#     indeg = {u: 0 for u in comp_set}
#     outdeg = {u: 0 for u in comp_set}

#     for u in comp_set:
#         for v in graph[u]:
#             if v in comp_set:
#                 outdeg[u] += 1
#                 indeg[v] += 1

#     # In a simple directed cycle, every node has in-degree=1 and out-degree=1
#     return all(indeg[u] == 1 and outdeg[u] == 1 for u in comp_set)


# # ------------------------------------------------------------
# #  Summarize SCC structure
# # ------------------------------------------------------------

# sink_sccs = []
# cycle_sccs = []

# for comp in sccs:
#     if is_sink_scc(comp, G100):
#         sink_sccs.append(comp)
#     if is_simple_cycle_scc(comp, G100):
#         cycle_sccs.append(comp)

# print("Total number of SCCs:", len(sccs))
# print("Number of sink SCCs:", len(sink_sccs))
# print("Sink SCCs (sorted residues):")
# for comp in sink_sccs:
#     print("  ", sorted(comp))

# print("\nSimple cycle SCCs (sorted residues):")
# for comp in cycle_sccs:
#     print("  ", sorted(comp))

# print("\nNontrivial sink SCCs (size > 1):")
# for comp in sink_sccs:
#     if len(comp) > 1:
#         print("  ", sorted(comp))



# # # ------------------------------------------------------------
# # #  Accelerated Collatz map and full construction of G_100
# # # ------------------------------------------------------------

# # def v2(m: int) -> int:
# #     """Return the exponent of 2 dividing m."""
# #     k = 0
# #     while m % 2 == 0:
# #         m //= 2
# #         k += 1
# #     return k


# # def T(n: int) -> int:
# #     """Accelerated Collatz map."""
# #     if n % 2 == 0:
# #         return n / 2
# #     m = 3*n + 1
# #     return m / (2 ** v2(m))


# # def build_G100(K: int = 500):
# #     """
# #     Build the mod-100 Collatz automaton G_100.

# #     For each residue r in {0,...,99}, we sample:
# #         n = r, r+100, r+200, ..., r+100*K

# #     For each sample, compute T(n) mod 100 and collect all distinct successors.

# #     K=500 is usually enough for stabilization.
# #     """
# #     adjacency = {r: set() for r in range(100)}

# #     for r in range(100):
# #         for k in range(K + 1):
# #             n = r + 100*k
# #             s = T(n) % 100
# #             adjacency[r].add(s)

# #     # Convert sets to sorted lists for readability
# #     return {r: sorted(list(succs)) for r, succs in adjacency.items()}


# # # ------------------------------------------------------------
# # #  Build the graph
# # # ------------------------------------------------------------

# # G100 = build_G100()

# # # If you want to print it:
# # for r in range(100):
# #     print(f"{r:02d} -> {G100[r]}")



