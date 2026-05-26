from itertools import product

def test_pattern(k_list):
    # k_list = [k0, k1, ..., k_{b-1}]
    b = len(k_list)
    a = sum(k_list)

    # Compose T(x) = (3x+1)/2^{k} symbolically:
    # x_{i+1} = (3 x_i + 1)/2^{k_i}
    # After b steps: x_b = (3^b x_0 + C) / 2^a
    C = 0
    coeff = 1  # will track 3^i
    for k in k_list:
        C = (C * 3 + 1)  # affine accumulation
        coeff *= 3
    # Now coeff = 3^b, total divisions = a
    denom = 2**a - 3**b
    if denom == 0:
        return None
    if C % denom != 0:
        return None
    x0 = C // denom
    if x0 <= 0:
        return None
    return x0, a, b

# Example: brute-force small patterns
def search_cycles(max_b=6, max_k=5):
    found = []
    for b in range(1, max_b+1):
        for k_list in product(range(1, max_k+1), repeat=b):
            res = test_pattern(list(k_list))
            if res is not None:
                found.append((k_list, res))
    return found

print(search_cycles(8,6))