import random
import math
import os
import vk_api
import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import pymysql
from datetime import timedelta
import time
import staff_functions
from vk_api.longpoll import VkLongPoll, VkEventType
import threading
import schedule

beta_testers = []
banned_users = []
groups = ["ББСО-04-20"]
mysql_user = "miron_root"
mysql_pass = ""
spec = "§1"

bot_stat = 1
Main_prefix = "timetables/tests/"

secrets = staff_functions.load_json("/secrets.json")

mysql_pass      		   = secrets["mysql_pass"]
vk_token_production        = secrets["vk_token_production"]
vk_token_test   		   = secrets["vk_token_testing"]
mysql_pass				   = secrets["mysql_pass"]
beta_testers			   = secrets["betta_testers"]
vk_session = vk_api.VkApi(token = vk_token_production)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

staff_functions.out_red("Python 3.0 bot for vk 'Расписание для КБСП'")
time.sleep(1)
staff_functions.out_red("Admin: @miron_root")
time.sleep(1)
staff_functions.out_red("Запуск")
banned_users = staff_functions.load_json("banned.json")
prefix = staff_functions.load_json(Main_prefix+"prefix.json")

frase_for_vs = "Это воскресенье, отдыхай"



def get_rand_message(name): 
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable')
		cur = con.cursor()
		cur.execute("SELECT * FROM `frases`")
		rows = cur.fetchall()
#	 message = unicode(random.choice(rows)[1], 'utf-8')
		message = random.choice(rows)[1]
		position_spec = message.find(spec)
		staff_functions.out_blue("Получение рандомного сообщения из бд")
		if(position_spec != -1):
			message = message[0:position_spec]+name+message[position_spec+len(spec):len(message)]
		con.close()
		return message
def get_week_by_day(date1):
	startingweek = datetime.date(2021, 2, 7)
	stopingweek = date1.date()
	#stopingweek = datetime.date(2020, 11, 9)
	delta = (stopingweek-startingweek).days/7
	if(delta == math.ceil(delta)):
		return math.ceil(delta) + 1
	if(math.ceil(delta) -1 < delta <=math.ceil(delta)):
		return math.ceil(delta)

def make_timetable(date, group):
	nowweek = get_week_by_day(date)
	day = date.isoweekday()
	paras_1 = []
	if(nowweek % 2 == 0):
		timetable = staff_functions.load_json(Main_prefix+str(group)+"/chet.json")
	else:
		timetable = staff_functions.load_json(Main_prefix+str(group)+"/nechet.json")
	ret_str = ""
	ret_str = "Расписание для группы: "+group+" \n"+staff_functions.int_to_day(date.isoweekday())+ " " + str(date.day)+" "+ staff_functions.int_to_mounth(date.month) +" \nТекущая неделя: "+str(nowweek) + "\n\n"
	day = date.isoweekday()
	if (day ==7):
		return [frase_for_vs,[]]
	try:
		for i in range(len(timetable[day])):
				if(timetable[day][i]["para"][0:3] == "кр "):
						weeks = timetable[day][i]["para"][3:len(timetable[day][i]["para"])][0:timetable[day][i]["para"][3:len(timetable[day][i]["para"])].find("н") - 1].split(",")
						if(not(str(nowweek) in weeks)):
							weeks = []
							timetable[day][i]["para"] = timetable[day][i]["para"].replace(timetable[day][i]["para"][0:timetable[day][i]["para"].find("н")+2],"")
						else:
							continue
				else:	
					if(timetable[day][i]["para"][0].isdigit() or timetable[day][i]["para"][1].isdigit()):
						weeks = timetable[day][i]["para"][0:len(timetable[day][i]["para"])][0:timetable[day][i]["para"][0:len(timetable[day][i]["para"])].find("н") -1].split(",")
						if(str(nowweek) in weeks):
							weeks = []
							timetable[day][i]["para"] = timetable[day][i]["para"].replace(timetable[day][i]["para"][0:timetable[day][i]["para"].find("н")+2],"")							
						else:
							weeks = []
							continue
				paras_1.append(timetable[day][i]["num_para"])
				ret_str += timetable[day][i]["num_para"] + " пара " + staff_functions.int_to_timepar(int(timetable[day][i]["num_para"])) 
				ret_str += timetable[day][i]["para"] + " "
				if(timetable[day][i]["type"] != "None"):
					if (timetable[day][i]["type"] == "лр"):
						ret_str += "лаба" + " "
					elif timetable[day][i]["type"] == "пр":
						ret_str += "практика" + " "	
					elif timetable[day][i]["type"] == "лек":
						ret_str += "лекция" + " "
					else:
						ret_str += timetable[day][i]["type"] + " "
				if(timetable[day][i]["fio"] != "None"):
					ret_str += timetable[day][i]["fio"] + " "
				if(timetable[day][i]["aud"] == "Д"):
					ret_str += "Дистант" + " \n"
				else:	
					if(timetable[day][i]["aud"] == "None"):
						ret_str += "" + " \n"
					else:
						ret_str += timetable[day][i]["aud"] + "\n"
	except Exception:
		ret_str = "Произошла ошибка сообщи разработчику"
	return [ret_str, paras_1]
def get_paras_by_group(date, group):
	return make_timetable(date,group)

#print(get_paras_by_group(datetime.datetime.today(),"ББСО-04-20"))
def get_now_para(date, group):
	current_time = datetime.datetime.now().hour,datetime.datetime.now().minute
	minutes_from00 = current_time[0]*60 + current_time[1]
	paras_rasp_1 = get_paras_by_group(date,group)
	paras_rasp = paras_rasp_1[1]
	if(paras_rasp[1] == []):
		return "Нет пар."
	time_paras = []
	for i in paras_rasp:
			current_time_para = staff_functions.get_start_para(i).split(":"), staff_functions.get_end_para(i).split(":")
			minutes_current_time_para_start = int(current_time_para[0][0])*60 + int(current_time_para[0][1])
			minutes_current_time_para_stop= int(current_time_para[1][0])*60 + int(current_time_para[1][1])
			time_para = [minutes_current_time_para_start,minutes_current_time_para_stop]
			time_paras.append(time_para)

	if( minutes_from00 < time_paras[0][0]):
		return "До начала пар : " + str(time_paras[0][0] - minutes_from00) + " минут."
	if( minutes_from00 > time_paras[len(time_paras)-1][1]):
		return "Пары закончились"

	for i in range(len(time_paras)):
				if(time_paras[i][0] <= minutes_from00 <= time_paras[i][1]):
					return "Сейчас идет: " + str(paras_rasp[i]) + " пара.\nДо ее конца: " + str(time_paras[i][1] - minutes_from00) +" минут."
	return "Сейчас перемена"
			
def get_empty_keyboard():
	keyboard = VkKeyboard(one_time=False)
	return keyboard

def form_keyboard(user_id):
	keyboard = VkKeyboard(one_time=False)
	keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
	#keyboard.add_line()
	keyboard.add_button('Расписание на завтра', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Какая сейчас пара по счету?', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()

	keyboard.add_button('Сменить группу', color=VkKeyboardColor.PRIMARY)
	keyboard.add_button('Респект разрабу', color=VkKeyboardColor.POSITIVE)

	keyboard.add_line()

	keyboard.add_button('Настройки уведомлений', color=VkKeyboardColor.POSITIVE)

	if(user_id in beta_testers):
		keyboard.add_line()
		keyboard.add_button('Системные операции', color=VkKeyboardColor.POSITIVE)
	return keyboard
def check_notifications_availible(vk_id): 
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
		cur = con.cursor()
		cur.execute("SELECT * FROM `notification` WHERE vk_id = " + str(vk_id))
		return cur.rowcount
def turn_on_notifiactions(vk_id): 
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
		cur = con.cursor()
		cur.execute("INSERT INTO `notification` (`id`, `vk_id`, `is_notifications_assepted`, `study_group`) VALUES (NULL, '"+str(vk_id)+"', '1', '');")
		return cur.rowcount
def turn_off_notifiactions(vk_id): 
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
		cur = con.cursor()
		cur.execute("DELETE FROM `notification` WHERE `notification`.`vk_id` = "+str(vk_id))
		return cur.rowcount
def update_group_to_notify(vk_id, group): 
		con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
		cur = con.cursor()
		cur.execute("UPDATE `notification` SET `study_group` = '"+group+"' WHERE `notification`.`vk_id` = "+str(vk_id))
		return cur.rowcount
def form_keyboard_settings(user_id, buffer):
		keyboard = VkKeyboard(one_time=False)
		if(buffer > 0):
			keyboard.add_button('Выключить уведоления', color=VkKeyboardColor.NEGATIVE)
		else:
			keyboard.add_button('Включить уведоления', color=VkKeyboardColor.POSITIVE)

		keyboard.add_line()
		keyboard.add_button('Назад', color=VkKeyboardColor.POSITIVE)		

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
		staff_functions.out_red("Кинули респект")
		return respekts + 1
def del_from_db(vk_id):
                con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable',autocommit=True)
                cur = con.cursor()
                cur.execute("DELETE FROM `ids` WHERE `vkid` = '" + str(vk_id) + "'")
                rows = cur.fetchall()
                staff_functions.out_red("Удаление пользователя из базы данных" +str(vk_id) )
                return 0

staff_functions.out_red("Запуск потока рассылки сообщений!!!!")



def timetablesender_thread():
				print("sended rasp")
				con = pymysql.connect('localhost', mysql_user, mysql_pass, 'timetable', autocommit=True)
				cur = con.cursor()
				cur.execute("SELECT * FROM `notification` WHERE `is_notifications_assepted` = 1 AND `study_group` != ''")
				rows = cur.fetchall()
				for i in rows:
					keyboard = form_keyboard(i[1])
					one_day = timedelta(1) 
					
					buffer = make_timetable(datetime.datetime.today()+one_day,i[3])
					
					if(buffer == frase_for_vs):
						break
					message = "Сообщение было сгенерированно автоматически\n" + buffer
					vk.messages.send(keyboard=keyboard.get_keyboard(), user_id= i[1], message= message, v = '5.38')
					time.sleep(1)

schedule.every().day.at("17:00").do(timetablesender_thread)


def worker_thread():
	while True:
			schedule.run_pending()
			time.sleep(1)

mythrd = threading.Thread(target=worker_thread, daemon=True)

mythrd.start()





stage = {}
def message_parser(user_id,text,group):
	try:
			if(stage[user_id] == 1):
				if(text in prefix):
					keyboard = form_keyboard_settings(user_id, 1)

					update_group_to_notify(user_id, text)
					vk.messages.send(keyboard = keyboard.get_keyboard(), user_id= user_id,message= "Уведомления успешно включены для группы: "+text,v = '5.38')

					stage[user_id] = 0
				else:
					keyboard = form_keyboard_settings(user_id, 0)
					vk.messages.send(keyboard = keyboard.get_keyboard(), user_id= user_id,message= "Группа не найдена попробуйте еще раз",v = '5.38')
					stage[user_id] = 0
					turn_off_notifiactions(user_id)
	except:
		pass
	if(text == "Начать" or text == "начать"):
		keyboard = form_keyboard(user_id)
		vk.messages.send( 
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= "Привет!",
			v = '5.38'
		)
		return 0
	if(text == "Банлист" or text == "банлист"):
		keyboard = form_keyboard(user_id)
		vk.messages.send( 
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= str(banned_users),
			v = '5.38'
		)
		return 0
	elif text == "Расписание на завтра":
		keyboard = form_keyboard(user_id)
		one_day = timedelta(1) 
		vk.messages.send( 
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= make_timetable(datetime.datetime.today()+one_day,group)[0],
			v = '5.38'
		)
		return 0
	elif text == "Настройки уведомлений":			
			buffer = check_notifications_availible(user_id)

			keyboard = form_keyboard_settings(user_id,buffer)
			vk.messages.send(
				keyboard=keyboard.get_keyboard(),
				user_id= user_id,
				message= "Вы в меню настройки уведомлений",
				v = '5.38'
			)
			return 0



	elif text == "Включить уведоления":
				buffer = check_notifications_availible(user_id)
				keyboard = form_keyboard_settings(user_id, buffer)

				if(buffer == 0):
					turn_on_notifiactions(user_id)
					keyboard = form_keyboard_settings(user_id, 1)

				else:
						vk.messages.send(keyboard=keyboard.get_keyboard(),user_id= user_id,message= "Уведомления уже включены",v = '5.38')
						return 0
				stage[user_id] = 1
				vk.messages.send(
					keyboard = keyboard.get_empty_keyboard(), 
					user_id= user_id,
					message= "Отправь мне учебную группу для которой тебе присылать уведомления",
					v = '5.38'
				)
				return 0
	elif text == "Выключить уведоления":

				buffer = check_notifications_availible(user_id)

				if(buffer == 0):
					keyboard = form_keyboard_settings(user_id, 1)
					vk.messages.send(keyboard=keyboard.get_keyboard(),user_id= user_id,message= "Уведомления уже выключены",v = '5.38')
					keyboard = form_keyboard_settings(user_id, buffer)
				else:
					turn_off_notifiactions(user_id)
					keyboard = form_keyboard_settings(user_id, 0)
				vk.messages.send(
					keyboard=keyboard.get_keyboard(),
					user_id= user_id,
					message= "ok",
					v = '5.38'
				)
				return 0
	elif text == "Назад":
			keyboard = form_keyboard(user_id)
			vk.messages.send( 
				keyboard=keyboard.get_keyboard(),
				user_id= user_id,
				message= "Ok",
				v = '5.38'
			)
			stage[user_id] = 0
			return 0
	if(text[0:10] == "Расписание" or text[0:10] == "расписание" ):
				keyboard = form_keyboard(user_id)
				try:
						qwe = text.split(" ")[1].split(".")
				except:
						vk.messages.send( 
                                        keyboard=keyboard.get_keyboard(),
                                        user_id= user_id,
                                        message= make_timetable(datetime.datetime.today(),group)[0],
                                        v = '5.38'
                        )
						return 0
				try:
					vk.messages.send( 
                    	    keyboard=keyboard.get_keyboard(),
                        	user_id= user_id,
                        	message= make_timetable(datetime.datetime(2021, int(qwe[1]), int(qwe[0]), 10, 32), group)[0],
                        	v = '5.38'
					)
				except:
						vk.messages.send( 
                    	    keyboard=keyboard.get_keyboard(),
                        	user_id= user_id,
                        	message= "Неверная дата",
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
	elif text == "Saved":
			keyboard = form_keyboard(user_id)
			attach = ["photo-132646282_457281177", "photo-132646282_457277120","photo-183914844_457242562","photo-183914844_457241071"]
			vk.messages.send(
				keyboard=keyboard.get_keyboard(),
				user_id= user_id,
				message= "Поздравляю напиши админу что ты нашел пасхалку. Ах ну да админ же выложил исходники. Вот тебе фоточки",
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
		vk.messages.send(
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= get_now_para(datetime.datetime.today(),group),
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
						staff_functions.make_json("banned.json",banned_users)
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
		vk.messages.send(
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
				staff_functions.make_json("banned.json",banned_users)
			else:
				echo_str = "У вас не достаточно прав если считаете что это ошибка vk.com/miron_root"
		except IndexError:
			print("exeption")
			echo_str = "Ошибка запроса!!!!"
		except  ValueError:
			print("exeption")
			echo_str = "Ошибка запроса!!!"
		vk.messages.send(
			keyboard=keyboard.get_keyboard(),
			user_id= user_id,
			message= echo_str,
			v = '5.38'
		)
		return 0
	elif text == "Респект разрабу":
				keyboard = form_keyboard(user_id)
				vk.messages.send( 
					keyboard=keyboard.get_keyboard(),
					user_id= user_id,
					message= "Админ респектнут " + str(pay_respekt()) + " раз.",
					v = '5.38'
				)
				vk.messages.send(
					keyboard=keyboard.get_keyboard(),
					user_id= beta_testers[0],
					message= "Вас респектанул: \n vk.com/id" +str(user_id),
					v = '5.38'
				)
				return 0


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
		staff_functions.out_red("Зарегестрировн новый пользователь с vk_id"+str(vk_id))
		con.close()
def new_user(user_id,text):
		staff_functions.out_blue("Написал новый пользователь")
		prefix = staff_functions.load_json(Main_prefix + "prefix.json")
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
			if event.from_user: 

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
			elif event.from_chat:
				print("Сообщение из чата "+event.event.chat_id + "  " + event.text)

				vk.messages.send(
					chat_id=event.chat_id,
					message='ку чо надо хули добавили'
				)


