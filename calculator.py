class Calculator:
    """A simple calculator that works just summation and multiplication"""
    @staticmethod
    def sum_nums(self, *inputs):
        """returns the sum of numbers passed"""
        result = 0
        for num in inputs:
            result += num
        print(inputs)
        return result
    @staticmethod
    def multiply(self, *inputs):
        if not inputs:
            return 0
        result = 1
        for num in inputs:
            result *= num
        return result