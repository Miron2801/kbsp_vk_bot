import json
import requests
import os
def out_red(text):
    print("\033[31m {} \033[0m " .format(text))
def out_yellow(text):
    print("\033[33m {} \033[0m " .format(text))
def out_blue(text):
    print("\033[34m {} \033[0m " .format(text))
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
def int_to_mounth(i):
	if(i == 1):
		return "Январь"
	elif (i == 2):
		return "Февраль"
	elif (i == 3):
		return "Март"
	elif (i == 4):
		return "Апрель"
	elif (i == 5):
		return "Май"
	elif (i == 6):
		return "Июнь"
	elif (i == 7):
		return "Июль"
	elif (i == 8):
		return "Август"
	elif (i == 9):
		return "Сентябрь"
	elif (i == 10):
		return "Октябрь"
	elif (i == 11):
		return "Ноябрь"
	elif (i == 12):
		return "Декабрь"

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
	elif (i == 6):
		return "18:00"
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
	elif (i == 6):
		return "19:30"
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
	elif (i == 6):
		return "(18:00-19:30) "
	return "Ошибка разработчика обратитесь к нему "
