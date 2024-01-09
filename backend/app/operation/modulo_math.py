class Modulo:
    def calculate(self, x, y):
        if y == 0:
            raise ValueError("Cannot calculate modulo by zero")
        return x % y