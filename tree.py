
count=0
trees=[]


class Tree():

	def __init__(self,species_name,region,height,age):
		self.species_name=species_name
		self.region=region
		self.height=float(height)
		self.age=float(age)
		self.reason=""
		count=count+1	


	def update_census(self,age,reason,height):
		self.age=age
		self.reason=reason
		self.height=height
		if self.reason=="Cut Down":
			count=count-1


		


class Employees(Tree):

	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
	
	def add_tree():
		species_name=input("Enter The Species Name:")
		region=input("Enter The Region To Be Considered:")
		height=float(input("Enter The Height Of The Tree In Meters:"))
		age=float(input("Enter The Age Of The Tree In Years:"))
		tree= Tree(species_name,region,height,age)
		trees.append(tree)



