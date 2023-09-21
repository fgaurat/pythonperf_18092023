from copy import deepcopy
def main():
    s = "toto"
    print(hex(id(s)))
    
    s = "tutu"
    print(hex(id(s)))


    # s[0] = 'u'
    # print(s)


    a = 2
    print(hex(id(a)))
    a = 4
    print(hex(id(a)))
    b=4
    print(50*"-")
    print(hex(id(a)))
    print(hex(id(b)))

    print("valeur de b :"+str(b))
    print(50*'-')

    l = [10,20,30,40,50,60]
    portion = l[:4]
    portion = l[4:]
    
    portion = l[:]
    portion = l.copy()

    portion[0]=1000
    print("portion",portion)
    l1 = l.copy()
    l1[0] = 1000
    print(l)
    print(l1)
    print(50*"-")
    l = [
        [10,20],
        [30,40],
        [50,60],
    ]
    # l1 = l[:]
    l1 = deepcopy(l)
    # l1 = l.copy()
    print(l)
    print(l1)
    l[1][1] = 1557
    print(l)
    print(l1)

    # print(l[1][1])
if __name__=='__main__':
    main()
