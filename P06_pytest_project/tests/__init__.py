class Calculator:
    def add(self,a,b):
        return a+b
    
    def substract(self,a,b):
        return a-b
    
    def multiply (self,a,b):
        return a*b
    
    def divide (self,a,b):
        if b==0:
            raise ZeroDivisionError ("Division by zero error")
        return a/b

class TestCalculator:
    def test_add(self):

        #arrange
        a=4321
        b=1234
        cal=Calculator()

        #act
        result=cal.add(a,b)

        #assert
        expected=5555
        assert result == expected

    def test_subtract(self):

        #arrange
        a=4321
        b=1234
        cal=Calculator()

        #act
        result=cal.substract(a,b)

        #assert
        expected=5555
        assert result == expected

    def test_multiply(self):

        #arrange
        a=4321
        b=1234
        cal=Calculator()

        #act
        result=cal.multiply(a,b)

        #assert
        expected=5555
        assert result == expected

    def test_divide(self):

        #arrange
        a=4321
        b=1234
        cal=Calculator()

        #act
        result=cal.divide(a,b)

        #assert
        expected=5555
        assert result == expected
