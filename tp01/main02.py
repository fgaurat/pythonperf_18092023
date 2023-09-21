from collections import deque
def main():
    l = [10,20,30]
    # FILO
    l.append(40)
    print(l)
    a = l.pop()
    print(a)
    print(l)

    print(50*'-')
    l.insert(0,0)
    print(l)
    a = l.pop(0)
    print(l)
    print(a)
    print(50*'-')
    d = deque(l)
    print(d)
    f = d.appendleft(0)
    print(d)
if __name__=='__main__':
    main()
