import networkx as nx
import matplotlib.pyplot as plt

def f(n):
    return (3*n + 2)//2 if n % 2 == 0 else (n + 1)//2

def forward_orbit(n, max_steps=200):
    orbit = [n]
    seen = {n}
    x = n
    for _ in range(max_steps):
        x = f(x)
        orbit.append(x)
        if x in seen or x in (1,4,7):
            break
        seen.add(x)
    return orbit

def plot_multiple_orbits(start_values):
    G = nx.DiGraph()
    colors = {}
    
    for s in start_values:
        orbit = forward_orbit(s)
        for i in range(len(orbit)-1):
            G.add_edge(orbit[i], orbit[i+1])
            colors[orbit[i]] = s
        colors[orbit[-1]] = s

    # assign positions left-to-right by sorted value
    pos = {node:(i,0) for i,node in enumerate(sorted(G.nodes()))}

    plt.figure(figsize=(18,4))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=[colors[n] for n in G.nodes()],
        cmap=plt.cm.tab20,
        node_size=900,
        arrows=True
    )
    plt.title("Multiple Forward Orbits")
    plt.axis("off")
    plt.show()


# Example
plot_multiple_orbits([10, 25, 50, 100, 200])

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_orbit(n):
    orbit = forward_orbit(n)
    fig, ax = plt.subplots(figsize=(10,2))
    ax.set_xlim(0, len(orbit))
    ax.set_ylim(0, 1)
    text = ax.text(0.5, 0.5, "", ha="center", va="center", fontsize=20)

    def update(i):
        text.set_text(" → ".join(map(str, orbit[:i+1])))

    ani = FuncAnimation(fig, update, frames=len(orbit), interval=600)
    plt.show()


# Example
animate_orbit(100)

def forward_orbit_tree(start_values):
    G = nx.DiGraph()

    for s in start_values:
        orbit = forward_orbit(s)
        for i in range(len(orbit)-1):
            G.add_edge(orbit[i], orbit[i+1])

    pos = nx.spring_layout(G, k=0.5, iterations=200)

    plt.figure(figsize=(14,10))
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=900,
        node_color="skyblue",
        arrows=True
    )
    plt.title("Forward-Orbit Tree for Many Starting Values")
    plt.show()


# Example
forward_orbit_tree(range(10, 200, 10))

def distance_to_cycle(n):
    x = n
    d = 0
    seen = set()
    while x not in (4,7) and x not in seen:
        seen.add(x)
        x = f(x)
        d += 1
    return d

def color_by_distance(start_values):
    G = nx.DiGraph()
    dist = {}

    for s in start_values:
        orbit = forward_orbit(s)
        for i in range(len(orbit)-1):
            G.add_edge(orbit[i], orbit[i+1])
            dist[orbit[i]] = distance_to_cycle(orbit[i])
        dist[orbit[-1]] = distance_to_cycle(orbit[-1])

    pos = nx.spring_layout(G, k=0.5)

    plt.figure(figsize=(14,10))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=[dist[n] for n in G.nodes()],
        cmap=plt.cm.plasma,
        node_size=900,
        arrows=True
    )
    plt.title("Nodes Colored by Distance to 4↔7 Cycle")
    plt.show()


# Example
color_by_distance(range(10, 200, 10))

def detect_cycles(limit=5000):
    cycles = []
    visited = {}

    for n in range(1, limit+1):
        x = n
        seen = []
        while x not in visited:
            visited[x] = True
            seen.append(x)
            x = f(x)
            if x in seen:
                cycle_start = seen.index(x)
                cycle = tuple(seen[cycle_start:])
                if cycle not in cycles:
                    cycles.append(cycle)
                break

    return cycles


# Example
print(detect_cycles(2000))
