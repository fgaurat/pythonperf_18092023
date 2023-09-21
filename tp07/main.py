from Rectangle import Rectangle


from typing import Any


class TheClass:
    def __new__(cls):
        print("def __new__(cls)")
        return super(TheClass,cls).__new__(cls)

    def __init__(self) -> None:
        print("def __init__(self)")


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call")

def main():
    c = TheClass()
    print(c)
    c()
    r1 = Rectangle(3,2)
    r2 = Rectangle(3,2)


    print(hex(id(r1)))
    print(hex(id(r2)))
    

if __name__=='__main__':
    main()
    