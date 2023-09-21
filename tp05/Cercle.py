import math
from ICalcGeo import ICalcGeo
from IMetaCalcGeo import IMetaCalcGeo
class Cercle(IMetaCalcGeo):

    def __init__(self,rayon) -> None:
        self._rayon=rayon

    @property
    def rayon(self):
        return self._rayon
    
    @rayon.setter
    def rayon(self,r):
        self._rayon = r
    
    @property
    def surface(self):
        return math.pi*self._rayon**2
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self._rayon=}"
    

