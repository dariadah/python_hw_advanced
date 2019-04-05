def fac(number):
    if number == 0:
        return 1  
    else:
        return number * factorial(number - 1)  


x = factorial(20)
print(x)

while True:
	y = int(input('Number for Fibonacci>>> '))

	def fib(y):
			if y in (1, 2):
				return 1
			return fib(y - 1) + fib(y - 2)
	print(fib(y))
