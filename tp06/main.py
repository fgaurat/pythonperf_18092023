from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from ICalcGeoProtocol import ICalcGeoProtocol



def show_surface(o:ICalcGeoProtocol):
    print(o.surface)

def main():
    r = Rectangle(10,8)
    show_surface(r)
   

if __name__=='__main__':
    main()
