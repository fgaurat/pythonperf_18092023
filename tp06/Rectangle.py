

class Rectangle:

    def __init__(self,longueur,largeur) -> None:

        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur


    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, value):
        self._largeur = value

    @property
    def surface(self)-> int:
        return self._longueur*self._largeur
    
    def __str__(self) -> str:
        return f"{__class__.__name__} - {self.__dict__}"
    
    def __eq__(self, __value: object) -> bool:
        return self._longueur == __value._longueur and self._largeur == __value._largeur

    def __int__(self):
        return self.surface
    