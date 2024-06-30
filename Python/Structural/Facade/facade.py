

class Chef:
    def cook(self, _food):
        food_is_ready = ('%s is ready !!'%(_food))
        return food_is_ready


class Preprocess:
    def prepare(self):
        return 'foodstuffs are all set up for making food . . . '


class Buyer:
    def buy(self):
        return 'Groseries have been bought by the buyer '


class Order:
    def __init__(self):
        self.chef = Chef()

        self.pre_process = Preprocess()

        self.buyer = Buyer()

    def order_food(self, order):

        print(self.buyer.buy())

        print(self.pre_process.prepare())

        print(self.chef.cook(order))

def main():
    food = input('name of the food:\n')
    
    get_order = Order()

    get_order.order_food(food)

if __name__=="__main__":main()

