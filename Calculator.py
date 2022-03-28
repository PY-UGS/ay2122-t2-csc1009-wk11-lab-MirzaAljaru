class Calculator:
    #Constructor
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2

    #Addition Function
    def adder(self):
        return self.input1 + self.input2
    
    #Substraction Function
    def subtractor(self):
        return self.input1 - self.input2
    
    #Multiply Function
    def multiplier(self):
        return self.input1 * self.input2
    
    #Divide Function
    def divider(self):
        return self.input1/self.input2
    
    #Clear Function
    def clear(self):
        self.input1 = self.input2 = 0
    
#Ask User for input
input1 = float(input("Enter first Number :"))
input2 = float(input("Enter Second Number : "))

#Initialize  a new calculator based on the inputs
calculator = Calculator(input1,input2)

#Print the resultant
print("Addition: " , calculator.adder())
print("Subtracting : " , calculator.subtractor())
print("Multiply: " , calculator.multiplier())
print("Divide: " , calculator.divider())
print("Clear: " , calculator.clear())