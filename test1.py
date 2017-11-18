dct = {"kate" : {"city" : "moscow", "temperature" : "12", "wind" : "west"}, "ann" : {"city" : "munchen", "temperature" : "15", "wind" : "east"}, "peter": {"city" : "berlin", "temperature" : "15", "wind" : "west"}}
print (dct)
c = input("Name: ")
if c not in dct:
	print ("sorry")
else:
	print (dct [c])

