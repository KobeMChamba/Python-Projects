class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        #find all divisors 
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                # If the divisors are distinct, add the other divisor
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        #sum
        sum = 0
        for num in divisors:
            sum += num
        return sum
    


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)