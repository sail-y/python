class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__pri_name = name

    def print_score(self):
        print '%s: %s' % (self.name, self.score)
	
	def get_pri_name(self):
		return self.__pri_name       

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()        
# print bart.get_pri_name()

class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    pass
dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()        