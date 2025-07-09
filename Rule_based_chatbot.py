def rule_based_chatbot():
	while True:	
		user_input=input("User(You): ")

		if user_input=="Hello" or user_input=="hello":
			print("Bot: Hi!")
		elif user_input=="How are you" or user_input=="how are you":
			print("Bot: I'm fine, thanks!")
		elif user_input=="Bye" or user_input=="bye":
			print("Goodbye!")
			break

		else:
			print("Bot: I can't understand!")

rule_based_chatbot()
