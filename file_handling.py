'''
open

read/write

close

'''
# s=open('demo.file',mode='r')
# print(s.read())
# s.close 

# s=open('demo.file',mode='w')
# (s.write("bye bye"))
# s.close  

# s=open('demo.file',mode='a')
# (s.write("abc abc bye"))
# s.close  

# s=open('demo.file',mode='r+')
# print(s.read())
# (s.write("r+ method"))
# s.close  

s=open('demo.file',mode='w+')
s.write("w+ mode")
s.seek(0)
print(s.read())
