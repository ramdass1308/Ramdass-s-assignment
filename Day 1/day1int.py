class Person:
    age = 25
	
    def __index__(self):
	     return self.age
		 
    def __int__(self):
         return self.age
		 
person = Person()
print('int(person) is:', int(person))		 