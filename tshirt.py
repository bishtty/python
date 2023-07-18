# exercise 8-3 pg 174/141

def make_shirt(size, txt):
	print("size of t-shirt: " + size)
	print("the text i want is: " + txt)
	
make_shirt('42', 'hello kitty')


def make_shirt(size = '44', txt = 'bye bye kitty'):
	print("size of t-shirt: " + size)
	print("the text i want is: " + txt)

make_shirt()

def default_shirt(txt, size = 'large'):
	print('default size: ' + size)
	print('the text i want is: ')
	
default_shirt('non lo so')
