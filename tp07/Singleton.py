class Singleton(type):

    _instance=None

    def __call__(self, *args, **kwargs):
        print(type(self))
        if self._instance is None:
            self._instance = super(Singleton,self).__call__(*args, **kwargs)
        
        return self._instance
        
        
        
        
