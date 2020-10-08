f = open("gumar.txt","r")
text = f.read()
f.close()
list_1 = []
list_2 = []
value = 0
txt = ""
for i in text:
	if i == " ":
		list_1.append(txt)
		txt = ""
	else:
		txt += i
for i in list_1:
	try:
		if int(i) < 300000000 and int(i) > 5000:
			list_2.append(int(i))
	except ValueError:
		continue
for i in list_2:
	value += i
print(list_2,"\n",value)
input()