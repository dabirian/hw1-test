from random_gen import gen, ave


def integ(f, a, b, n):
    samp = list(map(lambda x: f(x), gen(n, a, b)))
    return (b - a) * ave(samp)


if __name__=='__main__':
    print(integ(lambda x:x**2, 0, 1, 1000))
