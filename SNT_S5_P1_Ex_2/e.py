def approx_e_u(n):
    return (1 + 1 / n) ** n


def approx_e_v(n):
    p = 1
    s = 0
    for k in range(1, n + 1):
        s = s + 1 / p
        p = p * k
    return s


for n in range(1, 1000):
    print(n, " ", approx_e_v(n=n))
