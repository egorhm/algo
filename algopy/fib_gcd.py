from rcviz import viz, callgraph


@viz
def fib1(num):
    assert num >= 0
    if num <= 1:
        return num

    fb1 = fib1(num - 1)
    fb2 = fib1(num - 2)
    res = fb1 + fb2

    return res


@viz
def fib2(num):
    assert num >= 0
    return num if num <= 1 else fib2(num - 1) + fib2(num - 2)


def gcd(a, b):
    print "a = %d, b = %d" % (a, b)
    if a == 0 or b == 0:
        return max(a, b)

    res = gcd(b % a, a)
    return res


def main():
    a, b = 24, 9
    d = gcd(a, b)

    print(d)

if __name__ == "__main__":
    # main()

    print fib1(6)
    # callgraph.reset()
    callgraph.render("test.png")
