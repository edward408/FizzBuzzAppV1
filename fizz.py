#Version 1 of FizzBuzz
n = int(raw_input("Please enter a number: "))
for i in range(n):
	if i %3 == 0 and i % 5 ==0:
		print "fizz buzz"
	elif i % 3 == 0:
		print "fizz"
	elif i % 5 ==0:
		print "buzz"
	else:
		print str(i)
