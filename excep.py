x = input("First number: ")
y = input("Second number: ")
try:
	result = int(x) / int(y)
except:
	print("You can't divide by zero!")
else:
	print(result)
