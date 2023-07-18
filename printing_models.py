# modifying a list in a function pg180/147

def print_models(unprinted_designs, completed_models):
	'''

	# simulating printing each design, until none are left.
	# move each design to completed model after printing
	'''
	while unprinted_designs:
		current_design = unprinted_designs.pop()
	
		# simulating creating a 3d print from design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):	
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# normal printing method
print_models(unprinted_designs, completed_models) 

# printing without losing original values
# print_models(unprinted_designs[:], completed_models)

show_completed_models(completed_models)
