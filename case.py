import random
from random import randint

class cases:
    def __init__(self, price: float, consumer, consumerprices, industrial, industrialprices, milspec, milspecprices, restricted, restrictedprices, classified, classifiedprices, covert, covertprices, gold, goldprices):
        self.__price = price
        self.__consumer = consumer
        self.__consumerprices = consumerprices
        self.__industrial = industrial
        self.__industrialprices = industrialprices
        self.__milspec = milspec
        self.__milspecprices = milspecprices
        self.__restricted = restricted
        self.__restrictedprices = restrictedprices
        self.__classified = classified
        self.__classifiedprices = classifiedprices
        self.__covert = covert
        self.__covertprices = covertprices
        self.__gold = gold
        self.__goldprices = goldprices

        self.__inventory = []
        self.__inventory_names = []
        self.__inventory_prices = []

        if len(self.__consumer) == 0 and len(self.__industrial) == 0:
            self.__averagereturn = (sum(self.__goldprices) / len(self.__goldprices)) / 391 + (sum(self.__covertprices) / len(self.__covertprices)) / 156.4 + (sum(self.__classifiedprices) / len(self.__classifiedprices)) / 31.28 + (sum(self.__restrictedprices) / len(self.__restrictedprices)) / 6.25 + (sum(self.__milspecprices) / len(self.__milspecprices)) / 1.25
        else:
            self.__averagereturn = (sum(self.__covertprices) / len(self.__covertprices)) / 3759 + (sum(self.__classifiedprices) / len(self.__classifiedprices)) / 751.2 + (sum(self.__restrictedprices) / len(self.__restrictedprices)) / 150.2 + (sum(self.__milspecprices) / len(self.__milspecprices)) / 30.05 + (sum(self.__industrialprices) / len(self.__industrialprices)) / 6.26 + (sum(self.__consumerprices) / len(self.__consumerprices)) / 1.25

        self.roi = (self.__averagereturn / self.__price) * 100
    #get average return method
    def get_averagereturn(self):
        return int(self.__averagereturn * 100) / 100

    #get price method
    def get_price(self):
        return self.price

    #get ROI method
    def get_roi(self):
        return int(self.roi)

    #set price method
    def set_price(self, newprice):
        self.price = newprice

    #open case method
    def open(self, count):
        list = []
        list2 = []
        if len(self.__consumer) == 0 and len(self.__industrial) == 0:
            for i in range(count):
                index = randint(0, 391)
                if index == 391:
                    pos = randint(0, len(self.__gold) - 1)
                    list.append(self.__gold[pos])
                    list.append(self.__goldprices[pos])

                elif index <= 390 and index >= 388:
                    pos = randint(0, len(self.__covert) - 1)
                    list.append(self.__covert[pos])
                    list.append(self.__covertprices[pos])


                elif index <= 387 and index >= 375:
                    pos = randint(0, len(self.__classified) - 1)
                    list.append(self.__classified[pos])
                    list.append(self.__classifiedprices[pos])

                elif index <= 374 and index >= 311:
                    pos = randint(0, len(self.__restricted) - 1)
                    list.append(self.__restricted[pos])
                    list.append(self.__restrictedprices[pos])

                elif index <= 310 and index >= 0:
                    pos = randint(0, len(self.__milspec) - 1)
                    list.append(self.__milspec[pos])
                    list.append(self.__milspecprices[pos])

        else:
            for i in range(count):
                index = randint(0, 3756)

                if index == 3756:
                    pos = randint(0, len(self.__covert) - 1)
                    self.__inventory_names.append(self.__covert[pos])
                    self.__inventory_prices.append(self.__covertprices[pos])

                elif index <= 3755 and index >= 3750:
                    pos = randint(0, len(self.__classified) - 1)
                    self.__inventory_names.append(self.__classified[pos])
                    self.__inventory_prices.append(self.__classifiedprices[pos])

                elif index <= 3749 and index >= 3725:
                    pos = randint(0, len(self.__restricted) - 1)
                    self.__inventory_names.append(self.__restricted[pos])
                    self.__inventory_prices.append(self.__restrictedprices[pos])

                elif index <= 3724 and index >= 3600:
                    pos = randint(0, len(self.__milspec) - 1)
                    self.__inventory_names.append(self.__milspec[pos])
                    self.__inventory_prices.append(self.__milspecprices[pos])

                elif index <= 3599 and index >= 2900:
                    pos = randint(0, len(self.__industrial) - 1)
                    self.__inventory_names.append(self.__industrial[pos])
                    self.__inventory_prices.append(self.__industrialprices[pos])

                elif index <= 2899 and index >= 0:
                    pos = randint(0, len(self.__consumer) - 1)
                    self.__inventory_names.append(self.__consumer[pos])
                    self.__inventory_prices.append(self.__consumerprices[pos])

        self.__inventory = []
        for i in range(0, len(self.__inventory_names)):

            self.__inventory.append(self.__inventory_names[i])
            self.__inventory.append(f"{self.__inventory_prices[i]}€")


        return self.__inventory_names, self.__inventory_prices

    #get inventory method
    def get_inventory(self):
        return self.__inventory

    #sort inventory after value method
    def sort_inventory(self):

        list1 = []
        list2 = []
        groeßte = 0
        for i in range(len(self.__inventory_prices)):
            groeßte = self.__inventory_prices[0]
            for i in range(len(self.__inventory_prices)):
                if self.__inventory_prices[i - 1] > groeßte:
                    groeßte = self.__inventory_prices[i - 1]

            list1.append(self.__inventory_names[self.__inventory_prices.index(groeßte)])
            self.__inventory_names.remove(self.__inventory_names[self.__inventory_prices.index(groeßte)])
            self.__inventory_prices.remove(groeßte)
            list2.append(groeßte)
        self.__inventory_prices = list2
        self.__inventory_names = list1

        self.__inventory = []
        for i in range(0, len(self.__inventory_names)):

            self.__inventory.append(self.__inventory_names[i])
            self.__inventory.append(f"{self.__inventory_prices[i]}€")


    def create_enemy(self):
        self.case_hp = random.randint(20, 40)
        self.case_dmg = random.randint(3, 8)

    def is_defeated(self):
        return self.case_hp <= 0












