import op

truc = "toto"
def say_hello(name):
    global truc
    truc = "tutu"
    print("Bonjour "+name)
    print(truc)


def main():
    # print("module hello",__name__)
    # print("Hello")
    # print(op.add(5,6))
    print(truc)
    say_hello("Fred")
    print(truc)


if __name__ == "__main__":
    main()
