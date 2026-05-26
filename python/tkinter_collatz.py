import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import networkx as nx

# -----------------------------
# Collatz-like function
# -----------------------------
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

def distance_to_cycle(n):
    x = n
    d = 0
    seen = set()
    while x not in (4,7) and x not in seen:
        seen.add(x)
        x = f(x)
        d += 1
    return d

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

# -----------------------------
# GUI + Plotting
# -----------------------------
class CollatzGUI:
    def __init__(self, root):
        self.root = root
        root.title("Modified Collatz Dashboard")

        # Dropdown for starting number
        self.start_var = tk.IntVar(value=100)
        ttk.Label(root, text="Start Value:").grid(row=0, column=0)
        self.start_entry = ttk.Entry(root, textvariable=self.start_var, width=10)
        self.start_entry.grid(row=0, column=1)

        # Buttons
        ttk.Button(root, text="Plot Orbit", command=self.plot_orbit).grid(row=1, column=0)
        ttk.Button(root, text="Animate Orbit", command=self.animate_orbit).grid(row=1, column=1)
        ttk.Button(root, text="Multiple Orbits", command=self.plot_multiple).grid(row=2, column=0)
        ttk.Button(root, text="Orbit Forest", command=self.plot_forest).grid(row=2, column=1)
        ttk.Button(root, text="Distance Coloring", command=self.plot_distance).grid(row=3, column=0)
        ttk.Button(root, text="Detect Cycles", command=self.show_cycles).grid(row=3, column=1)

        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(10,5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

    # -----------------------------
    # Plot single orbit
    # -----------------------------
    def plot_orbit(self):
        n = self.start_var.get()
        orbit = forward_orbit(n)

        self.ax.clear()
        G = nx.DiGraph()
        for i in range(len(orbit)-1):
            G.add_edge(orbit[i], orbit[i+1])

        pos = {node:(i,0) for i,node in enumerate(orbit)}
        nx.draw(G, pos, with_labels=True, node_size=900, arrows=True, ax=self.ax)
        self.ax.set_title(f"Forward Orbit from {n}")
        self.canvas.draw()

    # -----------------------------
    # Animate orbit
    # -----------------------------
    def animate_orbit(self):
        n = self.start_var.get()
        orbit = forward_orbit(n)

        self.ax.clear()
        text = self.ax.text(0.5, 0.5, "", ha="center", va="center", fontsize=20)
        self.ax.axis("off")

        def update(i):
            text.set_text(" → ".join(map(str, orbit[:i+1])))

        ani = FuncAnimation(self.fig, update, frames=len(orbit), interval=600)
        self.canvas.draw()

    # -----------------------------
    # Multiple orbits
    # -----------------------------
    def plot_multiple(self):
        start_values = [10, 25, 50, 100, 200, 300]
        G = nx.DiGraph()
        colors = {}

        for s in start_values:
            orbit = forward_orbit(s)
            for i in range(len(orbit)-1):
                G.add_edge(orbit[i], orbit[i+1])
                colors[orbit[i]] = s
            colors[orbit[-1]] = s

        self.ax.clear()
        pos = nx.spring_layout(G, k=0.5)
        nx.draw(G, pos, with_labels=True, node_color=list(colors.values()),
                cmap=plt.cm.tab20, node_size=900, arrows=True, ax=self.ax)
        self.ax.set_title("Multiple Forward Orbits")
        self.canvas.draw()

    # -----------------------------
    # Orbit forest
    # -----------------------------
    def plot_forest(self):
        start_values = range(10, 200, 10)
        G = nx.DiGraph()

        for s in start_values:
            orbit = forward_orbit(s)
            for i in range(len(orbit)-1):
                G.add_edge(orbit[i], orbit[i+1])

        self.ax.clear()
        pos = nx.spring_layout(G, k=0.5)
        nx.draw(G, pos, with_labels=True, node_size=900, arrows=True, ax=self.ax)
        self.ax.set_title("Forward-Orbit Forest")
        self.canvas.draw()

    # -----------------------------
    # Distance coloring
    # -----------------------------
    def plot_distance(self):
        start_values = range(10, 200, 10)
        G = nx.DiGraph()
        dist = {}

        for s in start_values:
            orbit = forward_orbit(s)
            for i in range(len(orbit)-1):
                G.add_edge(orbit[i], orbit[i+1])
                dist[orbit[i]] = distance_to_cycle(orbit[i])
            dist[orbit[-1]] = distance_to_cycle(orbit[-1])

        self.ax.clear()
        pos = nx.spring_layout(G, k=0.5)
        nx.draw(G, pos, with_labels=True,
                node_color=[dist[n] for n in G.nodes()],
                cmap=plt.cm.plasma, node_size=900, arrows=True, ax=self.ax)
        self.ax.set_title("Distance to 4↔7 Cycle")
        self.canvas.draw()

    # -----------------------------
    # Cycle detection
    # -----------------------------
    def show_cycles(self):
        cycles = detect_cycles(2000)
        self.ax.clear()
        self.ax.text(0.1, 0.5, f"Cycles detected:\n{cycles}", fontsize=16)
        self.ax.axis("off")
        self.canvas.draw()


# -----------------------------
# Run GUI
# -----------------------------
root = tk.Tk()
app = CollatzGUI(root)
root.mainloop()
