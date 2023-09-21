import timeit

def the_loop():
    l = [10,20,30,40]
    r = []

    for i in range(1_000_000):
        r.append(i*2)

def the_map():
    l = [10,20,30,40]
    r = list(map(lambda i:i*2,range(1_000_000)))


def the_comp():
    # l = [10,20,30,40]
    r = [i*2 for i in range(1_000_000)]


def main():
    t1 = timeit.timeit("the_loop()",setup="from __main__ import the_loop",number=100)
    t2 = timeit.timeit("the_map()",setup="from __main__ import the_map",number=100)
    t3 = timeit.timeit("the_comp()",setup="from __main__ import the_comp",number=100)
    print(t1)
    print(t2)
    print(t3)




if __name__=='__main__':
    main()
