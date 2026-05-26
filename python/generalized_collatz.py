from fractions import Fraction

def generalized_cycle(a, b, c, d, r, s):
    """
    Solve the Diophantine cycle equation for the generalized map:
        g(x) = (a*x + b)/c   if x is odd
        g(x) = x/d           if x is even

    A cycle with r odd steps and s even steps satisfies:
        x = (a^r * x + K) / (c^r * d^s)
    =>  x * (c^r * d^s - a^r) = K
    """

    # Build the affine macro-map for one full loop
    A = Fraction(1, 1)   # slope
    B = Fraction(0, 1)   # intercept

    # Apply r odd steps: x -> (a*x + b)/c
    for _ in range(r):
        A = Fraction(a, c) * A
        B = Fraction(a, c) * B + Fraction(b, c)

    # Apply s even steps: x -> x/d
    for _ in range(s):
        A = Fraction(1, d) * A
        B = Fraction(1, d) * B

    # Solve x = A*x + B
    if A == 1:
        return None  # no fixed point possible

    x = B / (1 - A)

    # Return integer positive solutions only
    if x.denominator == 1 and x > 0:
        return int(x)
    else:
        return None


def orbit_until_repeat(x0, a, b, c, d, max_steps=1000):
    """
    Generate the orbit starting from x0 until a cycle is detected.
    """
    seen = {}
    orbit = []  # <-- FIXED: define the list before using append()

    x = x0
    for i in range(max_steps):
        if x in seen:
            start = seen[x]
            return orbit[start:]  # return the cycle only

        seen[x] = i
        orbit.append(x)

        # Apply the generalized map
        if x % 2 == 0:
            x = x / d
        else:
            x = (a * x + b) / c

    return None  # no cycle found within max_steps

# x0 = generalized_cycle(3, 1 , 1, 2, r=1, s=2)
# print("Cycle odd element:", x0)

# cycle = orbit_until_repeat(x0, 3, 1, 1, 2)
# print("Full cycle:", cycle)

x0 = generalized_cycle(5, -1 , 1, 2, r=1, s=2)
print("Cycle odd element:", x0)

cycle = orbit_until_repeat(x0, 5, -1, 1, 2)
print("Full cycle:", cycle)
