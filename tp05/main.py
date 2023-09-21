from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from IMetaCalcGeo import IMetaCalcGeo


def show_surface(o:IMetaCalcGeo):
    print(o.surface)

def main():
    r = Rectangle(10,8)
    c= Carre(10)
    ce = Cercle(5)
    print(c.surface)
    print(c)
    c.cote=12
    print(c.surface)
    print(c)

    print(50*'-')
    print(ce.rayon)
    print("surface",ce.surface)

    show_surface(r)
    show_surface(c)
    show_surface(ce)

if __name__=='__main__':
    main()
