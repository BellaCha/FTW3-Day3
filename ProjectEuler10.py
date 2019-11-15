#Summation of Prime numbers

number=int(input("Enter any number:  "))
X=list(range(2,number))
if number>1:
    for num in range(2,number):
        for i in range(2,num):
            if (num % i) ==0 :
                X.remove(num)
                break
    #print("List of prime numbers:", X)
    print("Total sum of all the prime numbers less than {}:".format(number) , sum(X))
else:
    print("Please enter a natural number")
