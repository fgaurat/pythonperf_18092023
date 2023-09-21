from multiprocessing import Pool
import time
import os


def f(x):
    t=5
    start = time.time()
    while time.time()-start<t:
        pass
    return x*x



def main():

    print(os.cpu_count())

    with Pool() as p:
        print(p.map(f, [1, 2, 3]))

if __name__=='__main__':
    main()
