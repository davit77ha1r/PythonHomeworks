	# Task 1 (Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle)
class Circle:
	def __init__(self,r):
		r = int(r)
		self.r = r
	def area(self):
		area = 3.141*(self.r**2)
		print("The area od cicle with {} radius is {}\n".format(self.r,area))
	def perimeter(self):
		perimeter = 2 * 3.141 * self.r
		print("The perimeter of cicle with {} radius is {}".format(self.r,perimeter))
r = input("Please tell radius:\n")
start = Circle(r)
start.area()
start.perimeter()


	# Task 2 (Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.Input: numbers= [10,20,10,40,50,60,70], target=50 Output: 3, 4)
class Equal:
	def equal(self,target):
		answer = ""
		count = 0
		for i in range(0,len(array_1)):
			t = array_1[i]
			for x in range(i,len(array_1)-1):
				p = array_1[x+1]
				if t+p == target:
					count += 1
					answer += "(pair {}) We find 2 numbers wich sum is {} >>> {} + {} = {}\n".format(count,target,t,p,target)
		answer += "The count of pairs is {}".format(count)
		print(answer)


array_1 = []
input_1 = 0
while input_1 != "stop":
	if input_1 == "stop":
		break
	input_1 = input("PLease enter number if you want to break write stop:\n")
	try:
		input_1 = int(input_1)
	except:
		print("You do not write number:\n")
		continue
	array_1.append(input_1)
target = int(input("\nEnter target number:\n"))
start = Equal()
start.equal(target)

	# Task 3 (Create a class named Sudent, which will inherit the properties and methods from the Person class. About attributes you can improvize)
import random
names = ["Davide","Anna","Vardan","Harut","Arianna","Viktoria","Tigran"]
surnames = ["Danielyan","Harutyunyan","Vardanyan","Makaryan","Xazaryan","Qaramyan","Lalayan"]
class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

class Student(Person):
  def __init__(self, firstname, lastname, year):
    super().__init__(firstname, lastname)
    self.thisyear = year

  def printing(self):
    print("Hi {} {} nice to meet you in our class to learn many thing in {}\n".format(self.firstname, self.lastname,self.thisyear))
for i in range(10):
	start = Student(random.choice(names), random.choice(surnames), 2021)
	start.printing()
