class Fraction:
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def Addition(self,fraction):
        self.num *= fraction.denom
        fraction.num *= self.denom
        self.denom *= fraction.denom
        
        return(Fraction(self.num+fraction.num,self.denom))
               
    def Subtraction(self,fraction):
        return (self.Addition(Fraction(fraction.num * -1, fraction.denom)))
               
    def Multiplication(self,fraction):
        return(Fraction(self.num*fraction.num,self.denom*fraction.denom))
               
    def Division(self,fraction):
        return (self.Multiplication(fraction.Inverse()))
               
    def Inverse(self):
        return(Fraction(self.denom,self.num))

    def PrintFraction(self):
        print(str(self.num)+"/"+str(self.denom))


fraction1 = Fraction(3,5)
fraction2 = Fraction(2,5)

fraction1.Multiplication(fraction2).PrintFraction()


