


def add(*args):
    print(args)
    r = 0
    for v in args:
        r+=v
    return r

def hello(**kwargs):
    """
    Hello !
    """
    print(kwargs['name'])

    for k,v in kwargs.items():
        print(k,v)


def truc():
    return 12,25




def main():
    l = [10,20,30]
    l1 = [100,200,300]
    r = add(*l,*l1) 
    # r = add(10,20,30) 
    # r = add(l) 
    print(r) #60

    a,*b=0,1,3
    print(a)
    print(b)
    print(50*'-')
    hello(name="GAURAT",firstName="Fred")
    print(hello.__doc__)

    print(a,b)

    print(50*'-')

    a,b = truc()
    print(50*'-')
    l = [10,20,30]

    def mult2(i):
        return i*2
    
    l2 = map(mult2,l)

    l2 = list(map(lambda i:i*2 ,l))
    
    the_lambda = lambda i:i*2
    l2 = list(map(the_lambda ,l))

    print(l2) # [20,40,60]
    l = [15,20,31,5,9,8,2,4]
    l2 =[i*2 for i in l if i%2 ==0]
    print(l2) # [20,40,60]
    ls = ['  ligne 01','  ligne 02    ','ligne 03   ']
    ls = [i.strip() for i in ls]
    print(ls)
if __name__=='__main__':
    main()
