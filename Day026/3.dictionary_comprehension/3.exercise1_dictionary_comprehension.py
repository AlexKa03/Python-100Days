sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()

result =  {word:len(word) for word in sentence}

print(result)