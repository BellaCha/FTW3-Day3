#Sum Square Difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
number=int(input("Sum Square Diff of first:" ))
sums=0
square=0
for i in range(1,number+1):
     sums+=i
     square +=i**2
     diff=sums**2-square
print(diff ,"is the differece between the sum of the squares of the first {} natural numbers and the square of the sum".format(number))
