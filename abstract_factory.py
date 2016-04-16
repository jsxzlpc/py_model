#coding = utf8


'''abstract product'''

class Dec_Operation:
    def result(self):
        pass
    
'''product'''

class Dec_Operation_Add(Dec_Operation):
    def result(self):
        return self.a + self.b
    
class Dec_Operation_Sub(Dec_Operation):
    def result(self):
        return self.a - self.b
    
class Dec_Operation_Mul(Dec_Operation):
    def result(self):
        return self.a * self.b

class Dec_Operation_Div(Dec_Operation):
    def result(self):
        try:
            if b != 0:
                return self.a / self.b
        except:
            print'the divided must not be zero'
            return 0

'''abstract product'''

class Bin_Operation:
    def result(self):
        pass
    
'''product'''

class Bin_Operation_And(Bin_Operation):
    def result(self):
        return self.a & self.b
    
class Bin_Operation_Or(Bin_Operation):
    def result(self):
        return self.a | self.b
    
class Bin_Operation_Xor(Bin_Operation):
    def result(self):
        return self.a ^ self.b

    
'''create factory'''

class Factory:
    def Create_Dec_Operation(self):
        return Operation()
    def Create_Bin_Operation(self):
        return Operation()



'''concrete factory '''

class Add_Factory(Factory): 
    def Create_Dec_Operation(self):
        return Dec_Operation_Add()
    def Create_Bin_Operation(self):
        return Bin_Operation_And()


'''concrete factory '''
class Sub_Factory(Factory):    
    def Create_Dec_Operation(self):
        return Dec_Operation_Sub()
    def Create_Bin_Operation(self):
        return Bin_Operation_Or()


'''concrete factory '''

class Mul_Factory(Factory):    
    def Create_Dec_Operation(self):
        return Dec_Operation_Mul()
    def Create_Bin_Operation(self):
        return Bin_Operation_Xor()



'''concrete factory '''

class Div_Factory(Factory):    
    def Create_Operation(self):
        return Operation_Div()
   
    
if __name__ == '__main__':
    
    a = input("the a is:")
    b = input("the b is:")
    
    operation = Add_Factory().Create_Dec_Operation()
    operation.a = a
    operation.b = b
    print 'a add b equal:',operation.result()
    
    operation = Add_Factory().Create_Bin_Operation()
    operation.a = a
    operation.b = b
    print 'a and b equal:',operation.result() 
