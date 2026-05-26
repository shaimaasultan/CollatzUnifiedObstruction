import networkx as nx
import matplotlib.pyplot as plt

def f(n):
    """Your modified Collatz-like function."""
    if n % 2 == 0:
        return (3*n + 2) // 2
    else:
        return (n + 1) // 2


def forward_orbit(n, max_steps=200):
    """Generate the forward orbit starting from n."""
    orbit = [n]
    seen = set([n])

    x = n
    for _ in range(max_steps):
        x = f(x)
        orbit.append(x)

        if x in seen:
            break
        seen.add(x)

        if x in (1, 4, 7):
            break

    return orbit


def draw_forward_orbit(n):
    """Draw the forward orbit as a directed path."""
    orbit = forward_orbit(n)

    G = nx.DiGraph()
    for i in range(len(orbit) - 1):
        G.add_edge(orbit[i], orbit[i+1])

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

    plt.figure(figsize=(14, 3))
    pos = {node: (i, 0) for i, node in enumerate(orbit)}

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=colors,
        node_size=1200,
        font_size=10,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=15,
        edgecolors="black"
    )

    plt.title(f"Forward Orbit Starting at {n}")
    plt.axis("off")
    plt.show()


# Example: forward orbit from 100
draw_forward_orbit(100)
