def solve_classic(cycle, d_values=range(2,50)):
    """
    CLASSIC FAMILY:
        g(x) = x/d        if x even
        g(x) = a*x + b    if x odd
    """
    k = len(cycle)
    solutions = []

    for d in d_values:
        eqs = []
        ok = True

        for i in range(k):
            x = cycle[i]
            xn = cycle[(i+1) % k]

            if x % 2 == 0:
                # even step: x/d = xn  →  x = d*xn
                if x != d * xn:
                    ok = False
                    break
            else:
                # odd step: a*x + b = xn
                eqs.append((x, xn))

        if not ok:
            continue

        if len(eqs) == 0:
            continue

        if len(eqs) == 1:
            x, xn = eqs[0]
            # infinite family: choose a, solve b
            for a in range(-50, 51):
                b = xn - a*x
                solutions.append((a, b, d, "classic"))
            continue

        # Solve two odd equations
        x1, xn1 = eqs[0]
        x2, xn2 = eqs[1]

        denom = (x1 - x2)
        if denom == 0:
            continue
        if (xn1 - xn2) % denom != 0:
            continue

        a = (xn1 - xn2) // denom
        b = xn1 - a*x1

        # Check all odd equations
        if all(a*x + b == xn for x, xn in eqs):
            solutions.append((a, b, d, "classic"))

    return solutions



def solve_flipped(cycle, d_values=range(2,50)):
    """
    FLIPPED FAMILY:
        g(x) = (3x + a)/d    if x even
        g(x) = (x + b)/d     if x odd
    """
    k = len(cycle)
    solutions = []

    for d in d_values:
        eq_even = []
        eq_odd = []

        for i in range(k):
            x = cycle[i]
            xn = cycle[(i+1) % k]

            if x % 2 == 0:
                eq_even.append((x, d*xn))
            else:
                eq_odd.append((x, d*xn))

        # Solve odd equations: x + b = d*xn
        if len(eq_odd) > 0:
            x, C = eq_odd[0]
            b = C - x
            if not all((x + b) == C for x, C in eq_odd):
                continue
        else:
            b = None

        # Solve even equations: 3x + a = d*xn
        if len(eq_even) > 0:
            x, C = eq_even[0]
            a = C - 3*x
            if not all((3*x + a) == C for x, C in eq_even):
                continue
        else:
            a = None

        if a is not None and b is not None:
            solutions.append((a, b, d, "flipped"))

    return solutions



def solve_cycle(cycle):
    """
    Solve both families and return all valid (a,b,d).
    """
    return solve_classic(cycle) + solve_flipped(cycle)



# -------------------------
# Example usage:
# -------------------------

cycle = [4, 7]
params = solve_cycle(cycle)

print("Cycle:", cycle)
print("Valid (a,b,d) solutions:")
for sol in params:
    print(sol)
