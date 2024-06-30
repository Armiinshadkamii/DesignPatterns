from abc import ABC, abstractmethod

class IClientAdapter(ABC):
    @abstractmethod
    def get_request(self) -> str:
        pass

class Old:
    def send_data(self) -> str:

        return '200'

class Adaptee:
    def send_specific_data(self) -> int:

        return 200

class Adapter(IClientAdapter):
    def __init__(self, adaptee : Adaptee()):
        self.adaptee = adaptee
        
    def get_request(self) -> str:

        return str(self.adaptee.send_specific_data())


def main():
    data: str = None
    new_method : Adaptee() = Adaptee()
    '''
    1- An interface gives us a structure for our code
    so that we wont need to change the client code
    with each update we make.
    2- also when working in
    a team everyone will know the signiture of the
    mehtods used.
    '''
    adapter: IClientAdapter() = Adapter(new_method)
    print(adapter.get_request())
    print(type(adapter.get_request()))

if __name__=="__main__":main()
