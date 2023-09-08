def sum():
    x = 0
    for i in range(10):
        x+=i
        if x % 2:
            print("x")
    return x

def inc(x):
    return x + 1

def test_answer_1():
    assert inc(3) == 4

def test_answer_2():
    assert sum() == 45