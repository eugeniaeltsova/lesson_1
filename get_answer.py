def get_answer(statement):

	dialogue = {"hi" : "hi, how are you", "how are you" : "fine, tnks", "bye" : "see you"}

	return  (dialogue [statement.lower()])

print (get_answer(input ("say smth ")))
while input() != "bye":
	get_answer(statement)

