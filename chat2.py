import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

while True:
	message = raw_input("Enter your message to the bot: ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	elif message == "reload":
		kernel.respond("load aiml b")	
	else: 	       	
		bot_response = kernel.respond(message)
		if bot_response is None:    		
			print "sorry I didnt quite get it."
		else:
			print bot_response
