from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    # r = Rectangle(5,3)
    # r1 = Rectangle(5,3)

    # # r.longueur = 12
    # # print(r.longueur)
    # # print(r.surface)
    # print(r)
    # s = str(r)
    # print(s)


    # int_value = int(r)

    # print("surface",int_value)



    # # if r.__eq__(r1):
    # if r==r1:
    #     print("ok")
    # else:
    #     print("ko")

    # d = DataRectangle(5,6)
    # print(d) #DataRectangle(longueur=5, largeur=6)
    # print(d.surface)

    print(50*'-')
    r = Rectangle(5,3)
    r1 = Rectangle(5,3)

    print(Rectangle.get_cpt())
    print(Rectangle.get_cptoffset(10))
    r1.get_cptoffset(10)

    row = "1,2"
    r2 = Rectangle.build_from_str(row)
    print(r2)

if __name__=='__main__':
    main()

