from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def handle(self):
        pass


class BaseHandler(Handler):
    next_handler = None
    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle(self, request):
        '''
        it is crucial to use return in a base handlers
        handle mehtod. otherwise you just call mehtods
        with it and wont return any value.
        '''
        if self.next_handler:
            
            return self.next_handler.handle(request)


class Login(BaseHandler):
    def handle(self):
        print('login done')
        
        return super().handle('login done')


class Pass(BaseHandler):
    def handle(self, request):
        if request == 'login done':
            print('pass checked')
            
            return super().handle('pass checked')


class Role(BaseHandler):
    def handle(self, request):
        if request == 'pass checked':
            
            return 'normal user'



def main(handler):
    response = handler.handle()
    print(response)

if __name__=="__main__":
    login = Login()
    password = Pass()
    role = Role()

    login.set_next(password)
    password.set_next(role)

    main(login)











        





            
