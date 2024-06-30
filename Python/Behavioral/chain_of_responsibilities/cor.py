from abc import ABC, abstractmethod

class Handler(ABC):
    '''
    This is an interface for all handlers
    '''
    @abstractmethod
    def set_next(self):
        pass
    
    @abstractmethod
    def handle(self):
        pass


class BaseHandler(Handler):
    '''
    in order to prevent writing set_next method
    for all handlers and to prevetn writing the
    code that passes the responsibility to the
    next handler we define a base handler.
    next-handler variable is for preventing a not
    defined error when self.next_handler is not
    defined.
    '''
    next_handler = None
    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)




class Monkey(BaseHandler):
    '''
    Monkey handler
    '''
    def handle(self, request):
        if request == 'banana':
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)
        
        
    
class Squirrel(BaseHandler):
    '''
    squirrel handler
    '''
    def handle(self, request):
        if request == 'nut':
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class Dog(BaseHandler):   
    def handle(self, request):
        if request == 'meat':
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def main(handler):
    usr_request = input('enter request: banana / nut / meat\n')

    response = handler.handle(usr_request)

    print(response)

if __name__=="__main__":
    '''
    here we initialize the next handler for
    each handler so that the request can be
    passed through all of the handlers
    '''
    monkey = Monkey()
    squirrel = Squirrel()
    dog = Dog()

    monkey.set_next(squirrel)
    squirrel.set_next(dog)
    #dog.set_next()

    main(monkey)
















                
