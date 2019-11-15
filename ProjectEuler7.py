#10001st Prime Number

number=int(input("Enter a number more than 105000:  "))
X=list(range(2,number))
for num in range(2,number):
    for i in range(2,num):
        if (num % i) ==0 :
            X.remove(num)
            break
print("List of prime numbers:", X)

print(len(X))
print(X[10000], " is the 10001st Prime Number")