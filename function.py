
def calc1():
    a = 2.0
    b = 7
    c, d = 8, 30
    print(f"calc1 params: \n a={a}\n b={b} \n c={c} \n d={d}")
    result = a * b + (c * a) - (b / d)
    return result

def calc2(a=2, c=8):
    print(f"calc2 params: \n a={a}\n c={c}")
    return c / a


def calc3():
    print("calc3")
    c, a = 8, 2.0
    return c // a

def square(x):
    return x**2

def output():
    say = "Result:"
    print(f"{say} {calc1()}")
    print(f"{say} {calc2()}") # default parameters
    print(f"{say} {calc2(3, 9)}")
    print(f"{say} {calc3()}")
    print(f"{say} {square(65)}")

if __name__ == '__main__':
    output()