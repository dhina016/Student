#problem 1
a=int(input('enther the value'))  #getting input
sum=0
for i in range(1,6):
    s=a*i
    print("the required output is",s)   #multiplication output
    sum=sum+s

print("the sum of the numbers",sum)  #addition of total values

if sum%2==0:
    print("the given number is even")  #check odd or even

num=sum//10
print("The reverse number is : {}".format(num)) # Display the result



#problem 2
str1=input("enter the string")  #getting input
s=str1
if s==str1[::-1]: #string campared
    print(str1,"is a palindrome")
else:
    print(str1,"is not a palindrome")

l=len(str1) # finding length

print("length of the string",l)

if l%2==0: #finding odd or even
    print("it is even")
else:
    print("it is odd")    
