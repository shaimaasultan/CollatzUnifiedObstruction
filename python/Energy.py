import math

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

# Example:
for x in [1, 3, 5, 7, 9, 27, 31, 63]:
    print(x, collatz_energy(x))


import math
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

# Compute energy for odd x up to 10,000
xs = list(range(1, 10001, 2))
Es = [collatz_energy(x) for x in xs]
logs = [math.log2(x) for x in xs]
drift = [E - math.log2(x) for E, x in zip(Es, xs)]

plt.figure(figsize=(16, 8))

# Plot E(x)
plt.plot(xs, Es, label="E(x) = log2(3x+1) - v2(3x+1)", color="blue", linewidth=1)

# Plot log2(x) for comparison
plt.plot(xs, logs, label="log2(x)", color="orange", linestyle="--")

plt.title("Collatz Energy E(x) for Odd x ≤ 10,000")
plt.xlabel("x (odd integers)")
plt.ylabel("Energy")
plt.legend()
plt.grid(True)
plt.show()

# Plot drift E(x) - log2(x)
plt.figure(figsize=(16, 6))
plt.plot(xs, drift, color="purple", linewidth=1)
plt.axhline(0, color="black", linestyle="--")
plt.title("Net Drift:  E(x) - log2(x)")
plt.xlabel("x (odd integers)")
plt.ylabel("Drift")
plt.grid(True)
plt.show()


import math
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

# Compute drift for odd x
xs = list(range(1, 10001, 2))
drift = [collatz_energy(x) - math.log2(x) for x in xs]

# Running average
running_avg = []
s = 0
for i, d in enumerate(drift):
    s += d
    running_avg.append(s / (i+1))

plt.figure(figsize=(16, 6))
plt.plot(xs, running_avg, color="green")
plt.axhline(0, color="black", linestyle="--")
plt.title("Running Average of Collatz Drift  E(x) - log2(x)")
plt.xlabel("x (odd integers)")
plt.ylabel("Running average drift")
plt.grid(True)
plt.show()



plt.figure(figsize=(12, 6))
plt.hist([collatz_energy(x) for x in xs], bins=200, color="steelblue")
plt.title("Histogram of Collatz Energy E(x) for Odd x ≤ 10,000")
plt.xlabel("Energy")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


import math
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

xs = list(range(1, 10001, 2))
Es = [collatz_energy(x) for x in xs]

# Compute lower envelope
lower_env = []
current_min = float('inf')
for E in Es:
    current_min = min(current_min, E)
    lower_env.append(current_min)

plt.figure(figsize=(16, 6))
plt.plot(xs, Es, color="lightgray", linewidth=0.5)
plt.plot(xs, lower_env, color="red", linewidth=2)
plt.title("Lower Envelope of Collatz Energy E(x)")
plt.xlabel("x (odd integers)")
plt.ylabel("Energy")
plt.grid(True)
plt.show()

upper_env = []
current_max = float('-inf')
for E in Es:
    current_max = max(current_max, E)
    upper_env.append(current_max)

plt.figure(figsize=(16, 6))
plt.plot(xs, Es, color="lightgray", linewidth=0.5)
plt.plot(xs, upper_env, color="purple", linewidth=2)
plt.title("Upper Envelope of Collatz Energy E(x)")
plt.xlabel("x (odd integers)")
plt.ylabel("Energy")
plt.grid(True)
plt.show()


import math
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

# Compute values for odd x up to 10,000
xs = list(range(1, 10001, 2))
v2_vals = [v2(3*x + 1) for x in xs]
E_vals  = [collatz_energy(x) for x in xs]

plt.figure(figsize=(12, 8))
plt.scatter(v2_vals, E_vals, s=10, alpha=0.5, color="purple")

plt.title("Scatter Plot:  v2(3x+1)  vs  Collatz Energy E(x)")
plt.xlabel("v2(3x + 1)")
plt.ylabel("E(x) = log2(3x+1) - v2(3x+1)")
plt.grid(True)
plt.show()


import math
import matplotlib.pyplot as plt

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

def collatz_energy(x):
    y = 3*x + 1
    return math.log2(y) - v2(y)

xs = list(range(1, 10001, 2))
v2_vals = [v2(3*x + 1) for x in xs]
E_vals  = [collatz_energy(x) for x in xs]

plt.figure(figsize=(12, 8))
plt.scatter(v2_vals, E_vals, c=xs, cmap="viridis", s=10, alpha=0.6)

plt.title("v2(3x+1) vs E(x) — Color‑coded by x")
plt.xlabel("v2(3x + 1)")
plt.ylabel("E(x)")
plt.colorbar(label="x value")
plt.grid(True)
plt.show()

from collections import defaultdict
import numpy as np

groups = defaultdict(list)
for x, v, E in zip(xs, v2_vals, E_vals):
    groups[v].append(E)

v2_levels = sorted(groups.keys())
avg_E = [np.mean(groups[k]) for k in v2_levels]

plt.figure(figsize=(12, 6))
plt.plot(v2_levels, avg_E, marker="o", color="red")
plt.title("Conditional Expectation  E(x) | v2(3x+1)=k")
plt.xlabel("k = v2(3x+1)")
plt.ylabel("Average E(x)")
plt.grid(True)
plt.show()
