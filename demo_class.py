class Student:

	def __init__(self,name,rollno,marks):
		self.name = name
		self.rollno = rollno
		self.marks = marks

	def getDetails(self):
		print("The name of the student is",self.name,"Roll no is",self.rollno,"Marks are",self.marks,"Class is",self.getClass())

	def getClass(self):
		
		if(self.marks>80):
			class_achieved = "Distinction"
		elif(self.marks<=80 and self.marks>70):
			class_achieved = "First class"
		elif(self.marks<=70 and self.marks>60):
			class_achieved = "Second class"
		elif(self.marks<60):
			class_achieved ="Pass class"
		else:
			class_achieved = "Failed!"

		return class_achieved	






