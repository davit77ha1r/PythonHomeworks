import random
class StrHelp:
	def __init__(self):
		new_dict = {}
		self.new_dict = new_dict
	def add_dict(self,string):
		c = 0  
		for i in string:
			c += 1
			self.new_dict[c] = i 
		print("This is dictionary:\n",self.new_dict)

	def remove_dubl(self,string):
		list_1 = []
		dict_2 = {}
		new_dict = self.new_dict
		c = 0
		for i in new_dict:
			c = c + 1
			if (new_dict[i] in list_1) == False:
				list_1.append(new_dict[i])
				dict_2[c] = new_dict[i]
		print("This is dictionari without dublicate values:\n",dict_2)

	def find_3_highest(self,string):
		list_1 = []
		new_dict = self.new_dict
		for i in new_dict:
			list_1.append(i)
		a = list_1[2]
		b = list_1[1]
		c = list_1[0]
		for i in list_1:
			if i > a:
				c = b 
				b = a
				a = i
			elif (i > b) and (i < a):
				c = b
				b = i
			elif (i > c) and (i < b):
				c = i
		print("The highest 3 values are 1. {}   2. {}   3. {}".format(a,b,c))


get_string = input("Enter string:\n")
start = StrHelp()
start.add_dict(get_string)
start.remove_dubl(get_string)
start.find_3_highest(get_string)

