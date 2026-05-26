def g_classic(x, a, b, d):
    """Classic Collatz-type map: even → x/d, odd → a*x + b."""
    if x % 2 == 0:
        return x / d
    else:
        return (a*x + b)/d


def orbit(x0, a, b, d, steps=20):
    """Generate orbit under the classic map."""
    x = x0
    seq = [x]
    for _ in range(steps):
        x = g_classic(x, a, b, d)
        seq.append(x)
    return seq


# -------------------------
# Verify (a,b,d) = (1,1,2)
# -------------------------

a, b, d = 3, 2, 11

#print("Orbit starting from 1:", orbit(1, a, b, d))
#print("Orbit starting from 2:", orbit(2, a, b, d))
print(f" using parameters : (a = {a} , b={b} , d={d} )")
print("Orbit starting from 4:", orbit(301, a, b, d,steps=50))
