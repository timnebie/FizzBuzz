# FizzBuzz Challenge
# Print from 1 to 100
# if number is divisible by 3, print "fizz"
# if number is divisible by 5, print "buzz"
# if number is divisible by 15, print "fizzbuzz"

for i in range(1, 101):
    if i % 3 == 0 and not i % 15 == 0:
        print("fizz")
    elif i % 5 == 0 and not i % 15 == 0:
        print("buzz")
    elif i % 15 == 0:
        print("fizzbuzz")
    else:
        print(i)
