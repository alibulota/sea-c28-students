#TypeError
numDogs = 100
def dog(object):
	if dog is numDogs:
		print('There are' + numDogs + 'dogs.')

dog(numDogs)


#SyntaxError
def dog(object):
	if dog is cat;
		print("DOG!")
#Cris' ex:
#def bad_func():
#	eval("foo = 'This is bad")

#bad_func()


#NameError
def animal():
	if cats is kitten:
		print('CATS!')

cats(kitten)

#AttributeError
class animal(object):
	def reptile(self):
		self.lizard

animal().reptile()

