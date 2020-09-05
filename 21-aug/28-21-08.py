a = 'qwerty'
a = a.casefold()

# reverse the string
rev = reversed(a)

# check if the string is equal to its reverse
if list(a) == list(rev):
   print("The string is a palindrome.");
else:
   print("The string is not a palindrome.");
b=len(a)
print(b)
if(b%2==0):
    print("Even");
else:
    print("Odd");

num=int(input("Enter a Number:"));
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number");
           break
   else:
       print(num,"is a prime number");
       
else:
   print(num,"is not a prime number");