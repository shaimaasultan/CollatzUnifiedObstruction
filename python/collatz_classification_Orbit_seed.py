import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Determine first k for each m
# ---------------------------------------------------------
def first_k(m):
    if m % 3 == 1:
        return 2
    if m % 3 == 2:
        return 1
    return None  # m divisible by 3 → no parents

# ---------------------------------------------------------
# 2. First odd parent of m
# ---------------------------------------------------------
def first_parent(m):
    k0 = first_k(m)
    if k0 is None:
        return None
    return (m * (2**k0) - 1) // 3

# ---------------------------------------------------------
# 3. Generate the true 4n+1 branch (Python ints, no overflow)
# ---------------------------------------------------------
def branch_of_m(m, length=300):
    o0 = first_parent(m)
    if o0 is None:
        return []
    branch = [o0]
    for _ in range(length - 1):
        branch.append(4 * branch[-1] + 1)  # Python ints → infinite precision
    return branch

# ---------------------------------------------------------
# 4. Plot spiral arms for selected m values
# ---------------------------------------------------------
def plot_m_branches(m_values, length=300):
    plt.figure(figsize=(14,14))

    # unique angle offset per m
    offsets = {m: 2*np.pi*i/len(m_values) for i, m in enumerate(m_values)}

    # unique color per m
    colors = {m: (np.random.rand(), np.random.rand(), np.random.rand())
              for m in m_values}

    for m in m_values:
        branch = branch_of_m(m, length)

        # convert to float64 only here
        branch = np.array(branch, dtype=np.float64)

        r = branch
        theta = np.log(branch) + offsets[m]

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        plt.scatter(x, y, s=10, color=colors[m], label=f"m = {m}")

    plt.title("Collatz Spiral Arms — True 4n+1 m‑Branches")
    plt.axis('equal')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    plt.show()

# ---------------------------------------------------------
# Run it
# ---------------------------------------------------------
plot_m_branches([3, 5, 7, 11, 17, 19], length=300)


print(branch_of_m(5, length=500))


import numpy as np
import matplotlib.pyplot as plt

def first_k(m):
    if m % 3 == 1:
        return 2
    if m % 3 == 2:
        return 1
    return None

def first_parent(m):
    k0 = first_k(m)
    if k0 is None:
        return None
    return (m * (2**k0) - 1) // 3

def branch_of_m(m, length=300):
    o0 = first_parent(m)
    if o0 is None:
        return []
    branch = [o0]
    for _ in range(length - 1):
        branch.append(4 * branch[-1] + 1)
    return branch

def plot_m_branches(m_values, length=300):
    plt.figure(figsize=(14,14))

    offsets = {m: 2*np.pi*i/len(m_values) for i,m in enumerate(m_values)}
    colors  = {m: (np.random.rand(), np.random.rand(), np.random.rand())
               for m in m_values}

    for m in m_values:
        branch = np.array(branch_of_m(m, length), dtype=np.float64)

        # FIX: use log radius to avoid overflow and scaling collapse
        r = np.log(branch)
        theta = r + offsets[m]

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        plt.scatter(x, y, s=10, color=colors[m], label=f"m = {m}")

    plt.title("Collatz Spiral Arms — True 4n+1 m‑Branches (Normalized Radius)")
    plt.axis('equal')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    plt.show()

plot_m_branches([3, 5, 7, 11, 17, 19], length=300)


import numpy as np
import matplotlib.pyplot as plt

def first_k(m):
    if m % 3 == 1:
        return 2
    if m % 3 == 2:
        return 1
    return None

def first_parent(m):
    k0 = first_k(m)
    if k0 is None:
        return None
    return (m * (2**k0) - 1) // 3

def branch_of_m(m, length=300):
    o0 = first_parent(m)
    if o0 is None:
        return []
    branch = [o0]
    for _ in range(length - 1):
        branch.append(4 * branch[-1] + 1)
    return branch

def plot_m_branches(m_values, length=300, Rmax=1e8):
    plt.figure(figsize=(14,14))

    offsets = {m: 2*np.pi*i/len(m_values) for i,m in enumerate(m_values)}
    colors  = {m: (np.random.rand(), np.random.rand(), np.random.rand())
               for m in m_values}

    for m in m_values:
        branch = np.array(branch_of_m(m, length), dtype=np.float64)

        # TRUE radius (no normalization)
        r_true = branch

        # CLIPPED radius for plotting
        r = np.minimum(r_true, Rmax)

        theta = np.log(r_true) + offsets[m]

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        plt.scatter(x, y, s=10, color=colors[m], label=f"m = {m}")

    plt.title("Collatz Spiral Arms — True 4n+1 m‑Branches (No Normalization)")
    plt.axis('equal')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
    plt.show()

plot_m_branches([3, 5, 7, 11, 17, 19], length=300, Rmax=1e8)

