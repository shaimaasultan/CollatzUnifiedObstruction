import numpy as np
import matplotlib.pyplot as plt
import random

# ---------------------------------------------------------
# 1. Compute the next odd Collatz child of n
# ---------------------------------------------------------
def odd_child(n):
    x = 3*n + 1
    while x % 2 == 0:
        x //= 2
    return x

# ---------------------------------------------------------
# 2. Classify each odd number into its family
# ---------------------------------------------------------
def classify_families(N=20000):
    families = {}
    for n in range(1, N, 2):  # odd numbers only
        m = odd_child(n)
        if m not in families:
            families[m] = []
        families[m].append(n)
    return families

# ---------------------------------------------------------
# 3. Plot the Collatz galaxy with angle offsets
# ---------------------------------------------------------
def plot_collatz_galaxy(N=20000):
    families = classify_families(N)

    plt.figure(figsize=(12,12))

    # assign each family a unique angle offset
    offsets = {}
    for i, m in enumerate(families.keys()):
        offsets[m] = 2*np.pi * i / len(families)

    for m, nums in families.items():
        nums = np.array(nums, dtype=np.float64)

        r = nums
        theta = np.log(nums) + offsets[m]   # <-- KEY FIX

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        color = (random.random(), random.random(), random.random())
        plt.scatter(x, y, s=1, color=color)

    plt.title("Full Collatz Galaxy (Each Family = One Spiral Arm)")
    plt.axis('equal')
    plt.show()

# ---------------------------------------------------------
# Run it
# ---------------------------------------------------------
plot_collatz_galaxy(N=5000)
