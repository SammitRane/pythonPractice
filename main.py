from Modules import demo_class

"""s1 = demo_class.Student("Sammit",1,79)
s2 = demo_class.Student("Varad",2,80)
s3 = demo_class.Student("Roshani",3,75)
s4 = demo_class.Student("Mitali",4,69)
s5 = demo_class.Student("Abhishek",5,58)
s1.getDetails()
s2.getDetails()
s3.getDetails()
s4.getDetails()
s5.getDetails()"""

students = {"name":"Sammit","rollno":"1","marks":"89",
            "name":"Varad","rollno":"2","marks":"75"
            }
stu = {1: "Sammit",2 : "Varad",3 : "Mitali"}

#print(students)
for student in stu:
	print(stu[student])