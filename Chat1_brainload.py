import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
	
	message=raw_input("Enter your message >> ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	elif message == "reload":
		kernel.respond("load aiml b")
	else:
		print kernel.respond(message)
