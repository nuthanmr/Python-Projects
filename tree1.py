count=0

class Tree():

	def __init__(self,species_name,region,height,age):
		self.species_name=species_name
		self.region=region
		self.height=float(height)
		self.age=float(age)
		self.reason=""
			


	def update_census(self,age,reason,height):
		self.age=age
		self.reason=reason
		self.height=height
		
		if self.reason=="Cut Down":
			global count
			count=count-1
			print("Tree or Plant is cut down! ")
			print("Total Trees And Plants=",count)


	
class Plant(Tree):
	def __init__(self,species_name,region,height,age):
		self.species_name=species_name
		self.region=region
		self.height=float(height)
		self.age=float(age)
		self.reason=""
		
			



class Employees():
	

	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
		self.treesandplants=[]
	
	def add_tree(self):
		species_name=input("Enter The Species Name:")
		region=input("Enter The Region To Be Considered:")
		height=float(input("Enter The Height Of The Tree In Meters:"))
		age=float(input("Enter The Age Of The Tree In Years:"))
		tree= Tree(species_name,region,height,age)
		self.treesandplants.append(tree)
		print("Tree added")
		global count
		count=count+1
		print("Total Trees And Plants=",count)



	def add_plant(self):
		species_name=input("Enter The Species Name:")
		region=input("Enter The Region To Be Considered:")
		height=float(input("Enter The Height Of The Plant In Meters:"))
		age=float(input("Enter The Age Of The Plant In Years:"))
		plant=Plant(species_name,region,height,age)
		self.treesandplants.append(plant)
		print("Plant added")
		global count
		count=count+1
		print("Total Trees And Plants=",count)
		
