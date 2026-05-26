i = 1

while True:
    
    if i%2 == 0:
        A = (3 * i + 2) / 2
    else:
        A = (i + 1)/2

    print(f"i = {int(i)} | A = {int(A)}")

    if (A == 7 and i == 4) or i == 1:
        break
    i = A


