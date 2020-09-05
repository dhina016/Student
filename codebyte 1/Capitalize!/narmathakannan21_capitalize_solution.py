import string
s="hello world"
for i in s[:].split(""):
    s=s.replace(i,i.capitalize())
    print(s)