'''1'''
# r = lambda q: q * 2
# s = lambda q: q * 3
# x = 2
# x = r(x) 
# x = s(x) 
# x = r(x)  
# print(x)


# '''2'''

# a = 4.5
# b = 2
# print(a//b) 

# '''3'''

# a = True
# b = False
# c = False
  
# if a or b and c: 
#     print("GEEKSFORGEEKS")
# else: 
#     print("geeksforgeeks")


# # '''4'''

# a = True
# b = False
# c = False
  
# if not a or b: 
#     print(1)
# elif not a or not b and c: 
#     print(2)
# elif not a or b or not b and a: 
#     print(3)
# else: 
#     print(4)



# '''5'''

# count = 1 
  
# def doThis(): 
  
#     global count 
  
#     for i in (1, 2, 3):  
#         count += 1
  
# doThis()
  
# print(count)


# '''6'''
# class Acc: 
#     def __init__(self, id): 
#         self.id = id
#         id = 555 

# acc = Acc(111)
# print(acc.id)


'''7'''
# for i in  range(2): 
#     print(i) 
  
# for i in range(4,6): 
#     print(i)



# '''8'''

# values = [1, 2, 3, 4] 
# numbers = set(values)

# def checknums(num):
#     if num in numbers: 
#         return True
#     else: 
#         return False
  
# for i in  filter(checknums, values): 
#     print(i)


# '''9'''

# counter = {} 
  
# def addToCounter(country): 
#     if country in  counter: 
#         counter[country] += 1
#     else: 
#         counter[country] = 1
  
# addToCounter('China') 
# addToCounter('Japan')
# addToCounter('china') 
  
# print(len(counter)) 



# '''10'''

# class Geeks: 
#     def __init__(self, id): 
#         self.id = id
  
# manager = Geeks(100) 
  
# manager.__dict__['life'] = 49
  
# print(manager.life + len(manager.__dict__)) 


# '''11'''
# a = "GeeksforGeeks "
  
# b = 13
  
# print a + b 





# '''12'''

# dictionary = {} 
# dictionary[1] = 1
# dictionary['1'] = 2
# dictionary[1] += 1
  
# sum = 0
# for k in dictionary: 
#     sum += dictionary[k] 
  
# print sum


# '''13'''

# dictionary = {1:'1', 2:'2', 3:'3'} 
# del dictionary[1] 
# dictionary[1] = '10'
# del dictionary[2] 
# print len(dictionary) 



# '''14'''

# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
  
# print nameList[1][-1]



# '''15'''


# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
  
# pos = nameList.index("GeeksforGeeks") 
  
# print pos * 5 
