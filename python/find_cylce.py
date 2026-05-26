def g(x, a, b, d):
    """Generalized Collatz-type map."""
    if x % 2 == 0:      # even
        return x // d
    else:               # odd
        return (a*x + b) 


def floyd_cycle_detection(x0, a, b, d, max_iter=10000):
    """
    Floyd's cycle-finding algorithm.
    Returns (mu, lam, cycle_list)
    where:
        mu  = index of first cycle element
        lam = cycle length
        cycle_list = actual cycle values
    """
    # Phase 1: find meeting point
    tortoise = g(x0, a, b, d)
    hare = g(g(x0, a, b, d), a, b, d)
    steps = 0

    while tortoise != hare and steps < max_iter:
        tortoise = g(tortoise, a, b, d)
        hare = g(g(hare, a, b, d), a, b, d)
        steps += 1

    if steps >= max_iter:
        return None  # no cycle detected within bounds

    # Phase 2: find start of cycle (mu)
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = g(tortoise, a, b, d)
        hare = g(hare, a, b, d)
        mu += 1

    # Phase 3: find cycle length (lam)
    lam = 1
    hare = g(tortoise, a, b, d)
    while tortoise != hare:
        hare = g(hare, a, b, d)
        lam += 1

    # Extract actual cycle
    cycle = [tortoise]
    for _ in range(lam - 1):
        tortoise = g(tortoise, a, b, d)
        cycle.append(tortoise)

    return mu, lam, cycle


def find_all_cycles(a, b, d, search_range=200):
    """
    Search for all distinct cycles for parameters (a,b,d)
    by scanning starting values 1..search_range.
    """
    seen_cycles = []
    for x0 in range(1, search_range + 1):
        result = floyd_cycle_detection(x0, a, b, d)
        if result is None:
            continue

        mu, lam, cycle = result
        cycle_sorted = tuple(sorted(cycle))

        # Avoid duplicates
        if cycle_sorted not in seen_cycles:
            seen_cycles.append(cycle_sorted)

    return seen_cycles


# -------------------------
# Example: parameters (5, -1, 2)
# -------------------------
cycles = find_all_cycles(a=5, b=-1, d=2, search_range=200)

cycles = find_all_cycles(a=6, b=-1, d=2, search_range=200)

cycles = find_all_cycles(a=7, b=-2, d=2, search_range=200)
print("Cycles found:", cycles)
