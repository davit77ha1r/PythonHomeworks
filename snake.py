import os
import time
settings = ""
print("ooooooooooooooo")
symbol = "X"
part = ("O"+"\n" * 3) + (" " * 20)
os.system("cls")
position_x =70
position_y = 15
row = ("\n" + "O" + (" "*77) + symbol)*30
row_1 = ("\n" + "O" + ((" "*position_x) + "X" + (" "*(76 - position_x))) + "O")
for i in range(100):
	if (position_x < 78) and (position_x > 1) and (position_y < 50) and (position_y > 1):
		row_1 = ("\n" + "O" + ((" "*position_x) + symbol + (" "*(76-position_x))) + "O")
		row = ("\n" + "O" + (" "*77) + "O")*position_y  + row_1 +("\n" + "O" + (" "*77) + "O")*(40-position_y)
		part = ("O" * 79) + row + "\n" + ("O" * 79)
		position_x += 1
		position_y = 15
		time.sleep(0.2)
		os.system("cls")
		print(part)
	else:
		os.system("cls")
		if position_x == 78:
			position_x = position_x - 2
			row_1 = ("\n" + "O" + ((" "*position_x) + symbol + (" "*(76-position_x))) + "O")
			row = ("\n" + "O" + (" "*77) + "O")*position_y  + row_1 +("\n" + "O" + (" "*77) + "O")*(40-position_y)
			part = ("O" * 79) + row + "\n" + ("O" * 79)
			print(part)
			for i in range(5):
				os.system("color 5")
				time.sleep(0.2)
				os.system("color a")
				time.sleep(0.2)
		print("you lose",position_x)
		break


