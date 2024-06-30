from abc import ABC, abstractmethod

class Context:
    def __init__(self, _strategy):
        self.strategy = _strategy

    def set_strategy(self, _strategy):
        self.strategy = _strategy

    def execute(self):
        return self.strategy.say()


class strategy(ABC):
    @abstractmethod
    def say(self):
        pass


class InEnglish(strategy):
    def say(self):
        return 'Hello'


class InFrench(strategy):
    def say(self):
        return 'bonjour'


class InGerman(strategy):
    def say(self):
        return 'Hallo'


def main(context):
    lang = input('Say hello in : English / French / German\n')

    if lang == 'English':
        response = context.execute()
        
    if lang == 'French':
        context.set_strategy(InFrench())
        response = context.execute()

    if lang == 'German':
        context.set_strategy(InGerman())
        response = context.execute()

    print(response)

if __name__=="__main__":   
    _context = Context(InEnglish())

    main(_context)






