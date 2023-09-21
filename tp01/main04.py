def main():
    a=2
    b=3
    c=a/b
    print(f"{a=}/{b=} = {c=:.2%}")
    l = [10,20,30]

    s = "{0}".format(l)
    print(s)
    s = "{2} {1} {0}".format(l[0],l[1],l[2])
    print(s)
    s = "{2} {1} {0}".format(*l)
    print(s)

    d = {"key1":"value1","key2":"value2","key3":"value3"}
    s = "{k1},{k2},{k3}".format(k1=d["key1"],k2=d["key2"],k3=d["key3"])
    print(s)
    # s = "{k1},{k2},{k3}".format(key1=d["key1"],k2=d["key2"],k3=d["key3"])
    s = "{key1},{key2},{key3}".format(**d)
    print(s)

if __name__=='__main__':
    main()
