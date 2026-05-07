students=[]
def Add():
	name=input("Enter Student Name:")
	rno=int(input("Enter Rollno:"))
	course=input("Enter Course:")
	student={
	"Name":name,
	"Rollno":rno,
	"Course":course
	}
	students.append(student)
	print("Student Added")
def View():
	if len(students)==0:
		print("No Students")
	else:
		count=1
		for i in students:
			print("---------------")
			print("Student",count,"Details")
			print("Name:",i["Name"])
			print("Rollno:",i["Rollno"])
			print("Course:",i["Course"])
			count=count+1
def Delete():
	if len(students)==0:
		print("No Students")
	deles=int(input("Enter Rollno to Delete the Student Record:"))
	for i in students:
		if i["Rollno"]==deles:
			students.remove(i)
			print("Student Deleted")
			return
	print("Student not Found")
def Search():
	keys=int(input("Enter RollNo. to Search:"))
	for i in students:
		if i["Rollno"]==keys:
			print("Student Found:")
			print("Name:",i["Name"])
			print("Rollno:",i["Rollno"])
			print("Course:",i["Course"])
			return
	print("Student Not Found")
while(True):
	print("------Student Management System------")
	print("1.Add Student Details")
	print("2.Delete the Student Details")
	print("3.Search the Student")
	print("4.View All Students")
	print("5.Exit")
	choice=int(input("Enter Your Choice:"))
	if choice==1:
		Add()
	elif choice==2:
		Delete()
	elif choice==3:
		Search()
	elif choice==4:
		View()
	elif choice==5:
		print("Exit.Bye")
		break
	else:
		print("Invalid Choice")