#Palindrome Checker

value=input("Enter any data type:")

if (value.upper()==value.upper()[::-1]):
    print(value," is Palindrome")
else:
    print(value,"is not Palindrome")