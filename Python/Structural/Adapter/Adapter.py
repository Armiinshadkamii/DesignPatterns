
class Old:
    '''
    Your program works with string data
    '''
    def get(self) -> str:
        
        return '123'


class New:
    '''
    The new library which you need to use
    works with int data
    '''
    def get_data(self) -> int:

        return 123
'''
Your client code cant work with the new
library beacause of incompatible formats.
so we need to change the new libraries
code so that it can work with 
'''

class Adapter(New, Old):

    def get(self) -> str:
        
        return str(self.get_data())

def main(protocol):
    print('Number: '+protocol.get())

if __name__=="__main__":

    _protocol : Adapter() = Adapter()

    main(_protocol)
