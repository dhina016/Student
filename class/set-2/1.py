a = int(input())
b = int(input())


for i in range(a, b+1):
    for j in range(2, int(i**0.5)):
        if(i%j == 0):
            print('not prime', i)
            break
    else:
        print('prime', i)


# for i in range(2, int(a**0.5)+1):
#     if(a%i == 0):
#         print('not prime')
#         break
# else:
#     print('prime')