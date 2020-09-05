s = input()
alphanum = alphabet = digit = lowercase = uppercase = False
for i in s:
    if alphanum == True & alphabet == True & digit == True & lowercase == True & uppercase == True:
        break
    else:
        print(i)
        if i.isalnum():
            alphanum = True
        if i.isalpha():
            alphabet = True
        if i.isdigit():
            digit = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True

print(alphanum)
print(alphabet)
print(digit)
print(lowercase)
print(uppercase)
# qW2sadjkhakjhkjashkjsahdweuiyiuy231876876dsajhkjhqweoiuou!!@$#asdsczxxczx