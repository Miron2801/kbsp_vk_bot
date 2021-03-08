import os
import datetime
now = datetime.datetime.now()
f = open("log.log", "w")
f.write("===========================================================\n")
f.write(str(now) + " >> Skipt restarted by user\n")
f.close()
while True:
	os.system("sudo python3 bot.py")
	print("Error. Restarting")
	f = open("log.log", "a")
	now = datetime.datetime.now()
	f.write(str(now) + " >> skript python3 bot.py crashed\n")
	f.close()
