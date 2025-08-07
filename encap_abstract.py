'''
wrapping of variables and methods in a single unit is called encapsulation
public
private
protected
'''
# class demo():
#    __a=2 #private
#    _b=4 # protected
#    print(__a)
#    print(_b)


# class demo():
#    def __init__(self,a,b):
#       self.__a=a # private
#       self._b=b # protected
# class demo2(demo):
#    def output(self):
#        print(self._b)
# d=demo2(3,4)
# d.output()


'''polymorphom'''

def add(a,b):
    print(a+b)
add(1,2)
add('a','b')
add([34,4],[3,4])
add((3,4),(4,6))