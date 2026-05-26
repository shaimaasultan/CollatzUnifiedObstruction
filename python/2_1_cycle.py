def g(x):
    """Generalized Collatz map with (a,b,d) = (5, -1, 2)."""
    if x % 2 == 0:      # even
        return x / 3
    else:               # odd
        return (9*x+1) / 3



def orbit(x, steps=50):
    """Generate the orbit of x under g."""
    seq = [x]
    for _ in range(steps):
        x = g(x)
        seq.append(x)
    return seq


# Example: track the orbit starting from 7
print(orbit(101, steps=1200))
