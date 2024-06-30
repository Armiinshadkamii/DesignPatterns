from abc import ABC, abstractmethod, abstractproperty

class Creator(ABC):

    @abstractmethod
    def return_chair(self):
        pass

class ChairCreator(Creator):
    def __init__(self):
        Creator.__init__(self)
    
    def return_chair(self):
        chair = Chair()
            
        return chair.make_chair()

class ModernChairCreator(Creator):
    def __init__(self):
        Creator.__init__(self)
    
    def return_chair(self):
        modern_chair = ModernChair()
        
        return modern_chair.make_chair()

class GetChair:
    def __init__(self):
        chair = ChairCreator()
        modern_chair = ModernChairCreator()
    def get(self, _chair):
        if _chair == 'chair':
            ret_chair = ChairCreator()
            
            return ret_chair.return_chair()
        elif _chair == 'modern chair':
            ret_modern_chair = ModernChairCreator()
            
            return ret_modern_chair.return_chair()

class ChairInterface(ABC):
    @abstractmethod
    def make_chair(self):
        pass

    @abstractproperty
    def color(self, _color):
        pass

    @abstractmethod
    def add_color(self, color):
        pass

class Chair(ChairInterface):
    def __init__(self):
        ChairInterface.__init__(self)

    def make_chair(self):
        return 'simple chair object'

    def color(self, _color):
        self.color = _color

    def add_color(self, color):
        self.color(color)


class ModernChair(ChairInterface):
    def __init__(self):
        ChairInterface.__init__(self)

    def make_chair(self):
        return 'modern chair object'

    def color(self, _color):
        self.color = _color

    def add_color(self, color):
        self.color(color)

   
def main():
    chair = GetChair()

    usr_input = input('order object (chair / modern chair)')
    
    final_product = chair.get('usr_input')
    
    print(final_product)
    
if __name__=="__main__":main()
