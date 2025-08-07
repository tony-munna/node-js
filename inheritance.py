'''
single inheritance
multilevel inheritance
multiple inheritance
hierarchial inheritance
'''

# class parent():
#  def output(self):
#     print("i am the parent")
# class child(parent):
#    def outputc(self):
#        print("i am the child")
# c=child() # child object
# c.outputc() # child method
# c.output() # parent method



# class grandfather():
#    def outputgf(self):
#        print("i am the grandfather")
# class parent(grandfather):
#    def output(self):
#       print("i am the parent")
# class child(parent):
#    def outputc(self):
#        print("i am the child")
# c=child() # child object
# c.outputc() # child method
# c.output() # parent method
# c.outputgf() # grandfather method 


# class father():
#    def outputf(self):
#        print("i am the father")
# class mother():
#   def outputm(self):
#        print("i am the mother")
# class child(father,mother):
#    def outputc(self):
#        print("i am the child")
# c=child() # child object
# c.outputc() # child method
# c.outputm() # mother method
# c.outputf() # father method 



class father():
    def outputf(self):
        print("i am the father")
class child1(father):
    def output1(self):
        print("i am the child1")
class child2(father):
    def output2(self):
        print("i am the child2")
c1=child1() # childc1 object
c2=child2() # childc2 object
c1.output1() # childc1 method
c1.outputf() # father method
c2.output2() # childc2 method
c2.outputf() # father method 
