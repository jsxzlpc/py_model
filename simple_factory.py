#coding = utf8


'''
abstract product
'''
class Operation:
    def result(self):
        pass
    
'''
product
'''
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
    
    
'''
 create factory
'''
class Operation_Factory:
    operation = {}
    operation['+'] = Operation_Add()
    operation['-'] = Operation_Sub()
    operation['*'] = Operation_Mul()
    operation['/'] = Operation_Div()
    
    def Create_Operation(self,method):
        if method in self.operation:
            op = self.operation[method]
        else:
            op = Operation_Notin()
        return op

if __name__ == '__main__':
    op = raw_input("the operate is:")
    a = input("the a is:")
    b = input("the b is:")
    operation = Operation_Factory().Create_Operation(op)
    operation.a = a
    operation.b = b
    print operation.result()
    
    