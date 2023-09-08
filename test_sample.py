def sum():
    x = 0
    y = []
    z = []
    for i in range(10):
        z.append(i)
        if i % 2 == 0:
            y.append(i)
            x += i
    return (x, y, z)


def inc(x):
    return x + 1


def test_answer_1():
    assert inc(3) == 4


def test_answer_2():
    assert sum() == (
        20,
        [0, 2, 4, 6, 8],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
