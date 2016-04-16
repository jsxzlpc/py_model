#coding = utf8


'''abstract product'''

class Operation:
    def result(self):
        pass
    
'''product'''

class Operation_Add(Operation):
    def result(self):
        return self.a + self.b
    
class Operation_Sub(Operation):
    def result(self):
        return self.a - self.b
    
class Operation_Mul(Operation):
    def result(self):
        return self.a * self.b

class Operation_Div(Operation):
    def result(self):
        try:
            if b != 0:
                return self.a / self.b
        except:
            print'the divided must not be zero'
            return 0

class Operation_Notin(Operation):
    def result(self):
        print 'the operation is not defined' 
        return 0
    
    
'''create factory'''

class Factory:
    def Create_Operation(self):
        return Operation()

'''concrete factory '''

class Add_Factory(Factory): 
    def Create_Operation(self):
        return Operation_Add()

'''concrete factory '''
class Sub_Factory(Factory):    
    def Create_Operation(self):
        return Operation_Sub()

 
'''concrete factory '''

class Mul_Factory(Factory):    
    def Create_Operation(self):
        return Operation_Mul()

'''concrete factory '''
class Div_Factory(Factory):    
    def Create_Operation(self):
        return Operation_Div()
   
    
if __name__ == '__main__':
    
    a = input("the a is:")
    b = input("the b is:")
    
    operationer = Add_Factory()
    operation = operationer.Create_Operation()
    operation.a = a
    operation.b = b
    print 'a add b equal:',operation.result()
    
    operation = Sub_Factory().Create_Operation()
    operation.a = a
    operation.b = b
    print 'a sub b equal:',operation.result() 
