from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #Change the stop to be 5, not 6 and the start to be 0, not 1
print(dice_num) #The easies way to catch this specific buf, since the error is IndexError
print(dice_images[dice_num])
