from abc import ABC, abstractmethod, abstractproperty

class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

class ModernFactory(FurnitureFactory):
    def __init__(self):
        FurnitureFactory.__init__(self)

    def create_chair(self):
        '''
        returns modern chair
        '''
        chair = ModernChair()

        return chair

    def create_sofa(self):
        '''
        returns modern sofa
        '''
        sofa = ModernSofa()

        return sofa


class TraditionalFactory(FurnitureFactory):
    def __init__(self):
        FurnitureFactory.__init__(self)

    def create_chair(self):
        '''
        returns traditional chair
        '''
        chair = TraditionalChair()

        return chair

    def create_sofa(self):
        '''
        returns traditional sofa
        '''
        sofa = TraditionalSofa()

        return sofa

class GetFactory:
    def get(self, factory):
        if factory == 'modern':
            
            return ModernFactory()
        elif factory == 'traditional':
            
            return TraditionalFactory()
        else:
            print('No such factory')

'''
chair interface
'''
class Chair(ABC):

    @abstractproperty
    def pattern(self):
        pass

    @abstractmethod
    def print_chair(self):
        pass

    @abstractmethod
    def add_pattern(self):
        pass

'''
we create chair products for different families
available
'''
class ModernChair(Chair):

    def __init__(self):
        Chair.__init__(self)

    def pattern(self, _pattern):
        '''
        sets the pattern property
        '''
        self.pattern = _pattern

    def print_chair(self):
        '''
        makes a modern chair
        '''
        
        print('Modern chair')

    def add_pattern(self, usr_pattern):
        '''
        calls the function that sets the pattern
        property for a modern chair
        '''  
        self.pattern(usr_pattern)


class TraditionalChair(Chair):

    def __init__(self):
        Chair.__init__(self)

    def pattern(self, _pattern):
        '''
        sets the pattern property
        '''
        self.pattern = _pattern

    def print_chair(self):
        '''
        makes a traditional chair
        '''
        
        print('Traditional chair')

    def add_pattern(self, usr_pattern):
        '''
        calls the function that sets the pattern
        property for a traditional chair
        '''  
        self.pattern(usr_pattern)

'''
sofa interface
'''
class Sofa(ABC):

    @abstractproperty
    def pattern(self):
        pass

    @abstractmethod
    def print_sofa(self):
        pass

    @abstractmethod
    def add_pattern(self):
        pass

'''
we create sofa products for different families
available
'''
class ModernSofa(Sofa):

    def __init__(self):
        Sofa.__init__(self)

    def pattern(self, _pattern):
        '''
        sets the pattern property
        '''
        self.pattern = _pattern

    def print_sofa(self):
        '''
        makes a modern sofa
        '''
        
        print('Modern sofa')

    def add_pattern(self, usr_pattern):
        '''
        calls the function that sets the pattern
        property for a modern sofa
        '''  
        self.pattern(usr_pattern)


class TraditionalSofa(Sofa):

    def __init__(self):
        Sofa.__init__(self)

    def pattern(self, _pattern):
        '''
        sets the pattern property
        '''
        self.pattern = _pattern

    def print_sofa(self):
        '''
        makes a traditional sofa
        '''
        
        print('Traditional sofa')

    def add_pattern(self, usr_pattern):
        '''
        calls the function that sets the pattern
        property for a traditional sofa
        '''  
        self.pattern(usr_pattern)


def main():
    _factory = GetFactory()

    usr_factory = input('factory: modern, traditional\n')

    factory = _factory.get(usr_factory)

    chair = factory.create_chair()

    chair.print_chair()

    sofa = factory.create_sofa()

    sofa.print_sofa()

    
if __name__ == "__main__":main()
    
