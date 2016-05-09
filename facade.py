#encoding=utf-8    
  
def printInfo(info):  
    print unicode(info, 'utf-8').encode('gbk')  
      
class Stock1():  
    name = '��Ʊ1'  
    def buy(self):  
        printInfo('�� '+self.name)  
      
    def sell(self):  
        printInfo('�� '+self.name)  
          
class Stock2():  
    name = '��Ʊ2'  
    def buy(self):  
        printInfo('�� '+self.name)  
      
    def sell(self):  
        printInfo('�� '+self.name)  
  
class NationDebt1():  
    name = '��ծ1'  
    def buy(self):  
        printInfo('�� '+self.name)  
      
    def sell(self):  
        printInfo('�� '+self.name)  
  
class Realty1():  
    name = '���ز�1'  
    def buy(self):  
        printInfo('�� '+self.name)  
      
    def sell(self):  
        printInfo('�� '+self.name)  
  
#����  
class Fund():  
    gu1 = None  
    gu2 = None  
    nd1 = None  
    rt1 = None  
    def __init__(self):  
        self.gu1 = Stock1()  
        self.gu2 = Stock2()  
        self.nd1 = NationDebt1()  
        self.rt1 = Realty1()  
          
    def buyFund(self):  
        self.gu1.buy()  
        self.gu2.buy()  
        self.nd1.buy()  
        self.rt1.buy()  
      
    def sellFund(self):  
        self.gu1.sell()  
        self.gu2.sell()  
        self.nd1.sell()  
        self.rt1.sell()  
      
def clientUI():  
    myFund = Fund()  
    myFund.buyFund()  
    myFund.sellFund()  
    return  
  
  
if __name__ == '__main__':  
    clientUI();