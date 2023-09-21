from Rectangle import Rectangle

class Carre(Rectangle):
    
    
    def __init__(self, cote) -> None:
        super().__init__(cote, cote)
        self._cote = cote

    @property
    def cote(self):
        return self._cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = self.largeur=cote
        # self.largeur = cote
        self._cote = cote
    
    def __str__(self) -> str:
        return f"{__class__.__name__} - {self.__dict__} {self._cote=}"