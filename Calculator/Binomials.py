def f(x: int):
    return 1 - 6 * ((5.0 / 6.0) ** x) \
        + 15 * ((4.0 / 6.0) ** x) \
        - 20 * ((3.0 / 6.0) ** x) \
        + 15 * ((2.0 / 6.0) ** x) \
        - 6 * ((1.0 / 6.0) ** x)


for n in range(40):
    print(f"f(n={n})={f(n)}")
