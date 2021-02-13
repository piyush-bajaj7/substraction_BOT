import time
import random
level_1_num1 = int(random.randint(100 , 120))
level_2_num1 = int(random.randint(121 , 140))
level_3_num1 = int(random.randint(141 , 160))

level_1_num2 = int(random.randint(30 , 50))
level_2_num2 = int(random.randint(51 , 60))
level_3_num2 = int(random.randint(61 , 90))

num1_randomizer = random.randint(1 , 3)
num2_randomizer = random.randint(1 , 3)

if num1_randomizer == 1 and num2_randomizer == 1: #1 to 1
	you = int(input(f"{level_1_num1}-{level_1_num2}\n"))
elif num1_randomizer == 2 and num2_randomizer == 2: #2 to 2
	you = int(input(f"{level_2_num1}-{level_2_num2}\n"))
elif num1_randomizer == 3 and num2_randomizer == 3: #3 to 3
	you = int(input(f"{level_3_num1}-{level_3_num2}\n"))
elif num1_randomizer == 1 and num2_randomizer == 2: #1 to 2
	you = int(input(f"{level_1_num1}-{level_2_num2}\n"))
elif num1_randomizer == 1 and num2_randomizer == 3: #1 to 3
	you = int(input(f"{level_1_num1}-{level_3_num2}\n"))
elif num1_randomizer == 2 and num2_randomizer == 1: #2 to 1
	you = int(input(f"{level_2_num2}-{level_1_num2}\n"))
elif num1_randomizer == 2 and num2_randomizer == 3: #2 to 3
	you = int(input(f"{level_2_num1}-{level_3_num2}\n"))
elif num1_randomizer == 3 and num2_randomizer == 1: #3 to 1
	you = int(input(f"{level_3_num1}-{level_1_num2}\n"))
elif num1_randomizer == 3 and num2_randomizer == 2: #3 to 2
	you = int(input(f"{level_3_num1}-{level_2_num2}\n"))


if num1_randomizer == 1 and num2_randomizer == 1: #1 to 1
	ans = level_1_num1-level_1_num2
elif num1_randomizer == 2 and num2_randomizer == 2: #2 to 2
	ans = level_2_num1-level_2_num2
elif num1_randomizer == 3 and num2_randomizer == 3: #3 to 3
	ans = level_3_num1-level_3_num2
elif num1_randomizer == 1 and num2_randomizer == 2: #1 to 2
	ans = level_1_num1-level_2_num2
elif num1_randomizer == 1 and num2_randomizer == 3: #1 to 3
	ans = level_1_num1-level_3_num2
elif num1_randomizer == 2 and num2_randomizer == 1: #2 to 1
	ans = level_2_num2-level_1_num2
elif num1_randomizer == 2 and num2_randomizer == 3: #2 to 3
	ans = level_2_num1-level_3_num2
elif num1_randomizer == 3 and num2_randomizer == 1: #3 to 1
	ans = level_3_num1-level_1_num2
elif num1_randomizer == 3 and num2_randomizer == 2: #3 to 2
	ans = level_3_num1-level_2_num2


if you == ans:
	print("Yes its correct!!!")
else:
	print(f"Its wrong \n The Correct answer is {ans}")

time.sleep(4)

print("MADE BY PiyushOP")