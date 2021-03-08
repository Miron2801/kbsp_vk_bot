import random
import os
import json
import math
import requests
import vk_api
import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import pymysql
from datetime import timedelta
import time
beta_testers = [251721968,274718907]
banned_users = []
prefix = ["ББСО-04-20","ББСО-03-20","ББСО-02-20","ББСО-01-20","БСБО-04-20","БСБО-18-20","БСБО-16-20","БПБО-01-20","БББО-07-20"]
mysql_user = "PyMiron"
mysql_pass = "xzSAwq21qwerty1234567890xzsawq21"
spec = "§1"
bot_stat = 1
vk_session = vk_api.VkApi(token='bec24307e14d0b58c4857c34435ec22ec33e0a3473234fe3e4e9a743461b13fac4081638e98aa1ce79269')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
out_red("Python 3.0 bot for vk 'Расписание для КБСП'")
time.sleep(1)
out_red("Admin: @miron_root")
time.sleep(1)

def get(url):
	request_1 = requests.get(url)
	return request_1.text
def make_json(name_file,massiv):
	with open(name_file, 'w') as fw:
	 json.dump(massiv, fw)
	out_yellow("Запрос на запись "+name_file)
	return os.path.getsize(name_file) / 1000000
def load_json(name_file):
	out_yellow("Запрос на чтение "+name_file)
	with open(name_file, 'r') as fr:
		return(json.load(fr))
out_red("Запуск")
banned_users = load_json("banned.json")
prefix = load_json("timetables/prefix.json")
def get_rand_message(name): #получение рандомизированного сообщения из бд возвращает текст сообщения
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable')
		cur = con.cursor()
		cur.execute("SELECT * FROM `frases`")
		rows = cur.fetchall()
#	 message = unicode(random.choice(rows)[1], 'utf-8')
		message = random.choice(rows)[1]
		position_spec = message.find(spec)
		out_blue("Получение рандомного сообщения из бд")
		if(position_spec != -1):
			message = message[0:position_spec]+name+message[position_spec+len(spec):len(message)]
		con.close()
		return message
def get_week_by_day(date1):
	startingweek = datetime.date(2020, 8, 31)
	stopingweek = date1.date()
	#stopingweek = datetime.date(2020, 11, 9)
	delta = (stopingweek-startingweek).days/7
	if(delta == math.ceil(delta)):
		return math.ceil(delta) + 1
	if(math.ceil(delta) -1 < delta <=math.ceil(delta)):
		return math.ceil(delta)
def int_to_day(i):
	if(i == 1):
		return "Понедельник"
	elif (i == 2):
		return "Вторник"
	elif (i == 3):
		return "Среда"
	elif (i == 4):
		return "Четверг"
	elif (i == 5):
		return "Пятница"
	elif (i == 6):
		return "Суббота"
	elif (i == 7):
		return "Воскресенье"
	return "Ошибка разработчика обратитесь к нему "
def get_start_para(q):
	i = int(q)
	if(i == 1):
		return "9:00"
	elif (i == 2):
		return "10:40"
	elif (i == 3):
		return "12:40"
	elif (i == 4):
		return "14:20"
	elif (i == 5):
		return "16:20"
	return "Ошибка разработчика обратитесь к нему "
def get_end_para(q):
	i = int(q)
	if(i == 1):
		return "10:30"
	elif (i == 2):
		return "12:10"
	elif (i == 3):
		return "14:10"
	elif (i == 4):
		return "15:50"
	elif (i == 5):
		return "17:50"
	return "Ошибка разработчика обратитесь к нему "
def int_to_timepar(q):
	i = int(q)
	if(i == 1):
		return "(9:00-10:30) "
	elif (i == 2):
		return "(10:40-12:10) "
	elif (i == 3):
		return "(12:40-14:10) "
	elif (i == 4):
		return "(14:20-15:50) "
	elif (i == 5):
		return "(16:20-17:50) "
	return "Ошибка разработчика обратитесь к нему "

def make_timetable(date, group):
	nowweek = get_week_by_day(date)
	day = date.isoweekday()
	if(nowweek % 2 == 0):
		out_yellow("Запрос на четное расписание")
		timetable = load_json("timetables/"+str(group)+"/chet.json")
	else:
		out_yellow("Запрос на нечетное расписание")
		timetable = load_json("timetables/"+str(group)+"/nechet.json")
	ret_str = ""
	ret_str = "Расписание для группы: "+group+" \n"+int_to_day(date.isoweekday())+ " " + str(date.day)+"."+ str(date.month) +" "+str(nowweek) + "\n"
	day = date.isoweekday()
	if (day ==7):
		return "Это воскресенье, Карл, воскресенье отдыхай"
	try:
		for i in range(len(timetable[day])):
				ret_str += timetable[day][i]["num_para"] + " пара " + int_to_timepar(int(timetable[day][i]["num_para"])) 
				ret_str += timetable[day][i]["para"] + " "
				ret_str += timetable[day][i]["type"] + " "
				ret_str += timetable[day][i]["aud"] + " \n" 
	except Exception:
		ret_str = "какая то неведомая херь скажи разрабу"
	return ret_str
def form_keyboard(user_id):
	keyboard = VkKeyboard(one_time=False)
	keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Респект разрабу', color=VkKeyboardColor.POSITIVE)
	keyboard.add_button('Сменить группу', color=VkKeyboardColor.PRIMARY)
	if(user_id in beta_testers):
		keyboard.add_line()
		#keyboard.add_button('Сколько до пары?', color=VkKeyboardColor.POSITIVE)
		#keyboard.add_button('Какая сейчас пара по счету?', color=VkKeyboardColor.POSITIVE)
		keyboard.add_button('Системные операции', color=VkKeyboardColor.POSITIVE)
	return keyboard
def form_keyboard2(user_id):
	keyboard = VkKeyboard(one_time=True)
	if(user_id in beta_testers):
		keyboard.add_button('fan 0', color=VkKeyboardColor.PRIMARY)
		keyboard.add_button('fan 32', color=VkKeyboardColor.PRIMARY)
		keyboard.add_button('fan 255', color=VkKeyboardColor.PRIMARY)
		keyboard.add_button('Состояние сервера', color=VkKeyboardColor.POSITIVE)
	else:
		keyboard.add_button('Щас дам бан', color=VkKeyboardColor.PRIMARY)
	return keyboard

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","Температура: "))


def pay_respekt():
		f = open('respekts.resp')
		respekts = int(f.read())
		f.close()
		f = open('respekts.resp',"w")
		f.write(str(respekts+1))
		f.close()
		out_red("Кинули респект")
		return respekts + 1
def del_from_db(vk_id):
                con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable',autocommit=True)
                cur = con.cursor()
                cur.execute("DELETE FROM `ids` WHERE `vkid` = '" + str(vk_id) + "'")
                rows = cur.fetchall()
                out_red("Удаление пользователя из базы данных" +str(vk_id) )
                return 0

def message_parser(user_id,text,group):
	if(text == "Начать" or text == "начать"):
		keyboard = form_keyboard(user_id)
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= "Привет!",
			v = '5.38'
		)
		return 0
	if(text == "Банлист" or text == "банлист"):
		keyboard = form_keyboard(user_id)
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= str(banned_users),
			v = '5.38'
		)
		return 0
	if(text == "Расписание" or text == "расписание"):
		keyboard = form_keyboard(user_id)
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
#		 message= make_timetable(datetime.datetime(2020, 11, 3, 10, 32)),
			message= make_timetable(datetime.datetime.today(),group),
			v = '5.38'
		)
		return 0
	elif text == "Расписание на завтра":
		keyboard = form_keyboard(user_id)
		one_day = timedelta(1) 
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= make_timetable(datetime.datetime.today()+one_day,group),
			v = '5.38'
		)
		return 0
	elif text == "Системные операции":
		keyboard = form_keyboard2(user_id)
		vk.messages.send(keyboard=keyboard.get_keyboard(),user_id= user_id,message= "Держи клаву",v = '5.38')
		return 0

	elif text == "Состояние сервера":
		keyboard = form_keyboard(user_id)
		if(user_id in beta_testers):
				vk.messages.send(
					keyboard=keyboard.get_keyboard(),
					user_id= user_id,
					message= measure_temp(),
					v = '5.38'
				)
		else:
			vk.messages.send(
					keyboard=keyboard.get_keyboard(),
					user_id= user_id,
					message= "Иди отсюда питушок у тебя нет прав смотреть таукю инфу",
					v = '5.38'
				)
		return 0
	elif text == "Сколько до пары?":
		keyboard = form_keyboard(user_id)
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= "не реализовано рефакторинг кода",
			v = '5.38'
		)
		return 0
	elif text == "Saved":
			keyboard = form_keyboard(user_id)
			attach = ["photo-132646282_457281177", "photo-132646282_457277120","photo-183914844_457242562","photo-183914844_457241071"]
			vk.messages.send(
				keyboard=keyboard.get_keyboard(),
				user_id= user_id,
				message= "Поздравляю напиши админу что ты нашел пасхалку. Вот тебе фоточки",
				#attachment = "photo-199791244_457239018",
				attachment = ','.join(attach),
				v= '5.38'
			)
			return 0
	elif text == "Сменить группу":
		keyboard = VkKeyboard(one_time=True)
		keyboard.add_button('Начать', color=VkKeyboardColor.PRIMARY)
		del_from_db(user_id)
		vk.messages.send(
				keyboard=keyboard.get_keyboard(),
				user_id= user_id,
				message= "Введи номер группы в формате XXXX-DD-DD",
				v = '5.38'
		)
		return 0
	elif text[0:3] == "fan":
				keyboard = form_keyboard(user_id)
				if(user_id in beta_testers):
						vk.messages.send(keyboard=keyboard.get_keyboard(),user_id= user_id, message= "Ок", v = '5.38')
						os.system(text)
				else:
						vk.messages.send(keyboard=keyboard.get_keyboard(), user_id= user_id,message= "Иди отсюда питушок у тебя нет прав исполнять эту команду",v = '5.38')
				return 0

	elif text == "Какая сейчас пара по счету?":
		keyboard = form_keyboard(user_id)
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= "не реализовано рефакторинг кода",
			v = '5.38'
		)
		return 0
	elif text[0:6] == "Разбан" or text[0:6] == "разбан":
		keyboard = form_keyboard(user_id)
		echo_str = ""
		try:
			if(user_id in beta_testers):
				qwe = text.split(" ")
				flag = 0
				if(int(qwe[1]) in banned_users):
					for i in range(len(banned_users)):

						if(banned_users[i] == int(qwe[1])):
							flag = 1
							del banned_users[i]
							break
					if(flag > 0):
						make_json("banned.json",banned_users)
						echo_str = "Пользователь: " + str(qwe[1]) +" удален из бан листа."
					else:
						print("происхожит какая то хуйня")
						echo_str = "происходит какая то неведомая ебень"
				else:
					echo_str = "Пользователь "+str(qwe[1])+" не был забанен"
			else:
				echo_str = "У вас не достаточно прав если считаете что это ошибка vk.com/miron_root"
		except IndexError:
			print("exeption")
			echo_str = "Ошибка запроса!!!"
		except	ValueError:
			print("exeption")
			echo_str = "Ошибка запроса!!!"
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= echo_str,
			v = '5.38'
		)
		return 0
	elif text[0:4] == "Бан " or text[0:4] == "бан ":
		echo_str = ""
		try:
			keyboard = form_keyboard(user_id)
			if(user_id in beta_testers):
				qwe = text.split(" ")
				banned_users.append(int(qwe[1]))
				echo_str  = "Забанен пользователь админом:" + str(user_id) + " Пользователь:" + str(qwe[1])
				make_json("banned.json",banned_users)
			else:
				echo_str = "У вас не достаточно прав если считаете что это ошибка vk.com/miron_root"
		except IndexError:
			print("exeption")
			echo_str = "Ошибка запроса!!!!"
		except  ValueError:
			print("exeption")
			echo_str = "Ошибка запроса!!!"
		vk.messages.send( #Отправляем сообщение
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= echo_str,
			v = '5.38'
		)
		return 0
	elif text == "Респект разрабу":
				keyboard = form_keyboard(user_id)
				vk.messages.send( #Отправляем сообщение
					keyboard=keyboard.get_keyboard(),
					user_id= user_id,
					message= "Админ респектнут " + str(pay_respekt()) + " раз.",
					v = '5.38'
				)
				vk.messages.send( #Отправляем сообщение
					keyboard=keyboard.get_keyboard(),
					user_id= beta_testers[0],
					message= "Вас респектанул: \n vk.com/id" +str(user_id),
					v = '5.38'
				)
				return 0
	keyboard = form_keyboard(user_id)
	vk.messages.send(
                                        keyboard=keyboard.get_keyboard(),
                                        user_id= user_id,
                                        message= "Команда не найдена",v = '5.38')

	return -1
def send_you_are_banned(user_id):
		vk.messages.send(
                                        user_id= user_id,
                                        message= "Забанен, все вопросы:\n vk.com/miron_root",
                                        v = '5.38'
                                )
def is_in_db(vk_id):
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable')
		cur = con.cursor()
		cur.execute("SELECT * FROM `ids` WHERE `vkid` LIKE '"+str(vk_id)+"'")
		rows = cur.fetchall()
		print("Проверка авторизации пользователя: "+str(vk_id))
		try:
			return [len(rows),str(rows[0][1])]
		except IndexError:
			return[len(rows)]
def message_send(user_id,text):
	vk.messages.send(user_id = user_id, message = text ,v = '5.38')
def add_to_db(text,vk_id):
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
		cur = con.cursor()
		cur.execute("INSERT INTO `ids` (`id`, `groups`, `vkid`) VALUES (NULL, '"+str(text)+"', '"+str(vk_id)+"')")
		rows = cur.fetchall()
		out_red("Зарегестрировн новый пользователь с vk_id"+str(vk_id))
		con.close()
def new_user(user_id,text):
		out_blue("Написал новый пользователь")
		prefix = load_json("timetables/prefix.json")
		if(text in prefix):
				keyboard = form_keyboard(user_id)
				vk.messages.send(
					keyboard = keyboard.get_keyboard(),
					user_id = user_id,
					message = "Принято!",
					v = '5.38' )
				add_to_db(text, user_id)
		else:
			message_send(user_id,"Привет! Введи номер группы в формате XXXX-DD-DD")
			print(text)
			return -1

if(bot_stat == 1):
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
			print("new event ",event.text)
			if event.from_user: #Если написали в ЛC

				if(event.user_id in banned_users):
					send_you_are_banned(event.user_id)
					print("пишет забаненный:"+str(event.user_id))
				else:
					print("Сообщение от: "+str(event.user_id))
					user_q = is_in_db(event.user_id)
					if(user_q[0] == 0):
						new_user(event.user_id,event.text)
					else:
						message_parser(event.user_id , event.text,user_q[1])
			elif event.from_chat: #Если написали в Беседе
				print("Сообщение из чата "+event.event.chat_id + "  " + event.text)

				vk.messages.send( #Отправляем собщение
					chat_id=event.chat_id,
					message='ку чо надо хули добавили'
				)


