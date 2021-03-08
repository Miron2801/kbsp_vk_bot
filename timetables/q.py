from openpyxl import load_workbook
import json
import os
import hashlib
import time
week = 0
def make_json(name_file,massiv):
	with open(name_file, 'w') as fw:
	    json.dump(massiv, fw)
	return os.path.getsize(name_file) / 1000000
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
out_red("Python 3.0 addon for vk bot 'Рапсписание КБСП' for online parsing http://mirea.ru")
time.sleep(1)
print("Разработка: @Miron_root")
time.sleep(1)
out_red("Starting")
def load_json(name_file):
        with open(name_file, 'r') as fr:
                return(json.load(fr))
def md5summ(filename):
	return hashlib.md5(open(filename, 'rb').read()).hexdigest()

out_red("Загрузка расписания с офф сайта МИРЭА")
print("")
os.system("rm table.xlsx")

os.system("wget -O table.xlsx https://webservices.mirea.ru/upload/iblock/1b2/%D0%9A%D0%91%D0%B8%D0%A1%D0%9F%201%20%D0%BA%D1%83%D1%80%D1%81%202%20%D1%81%D0%B5%D0%BC-%D0%94.xlsx")
out_red("Завершено!")

wb = load_workbook('table.xlsx')
sheet = wb['Лист1']
print("--------------------------------")
q = 0
w = 0
num_par =0
mass1 = [[],[],[],[],[],[],[]]
day = 1
prefixs = load_json("prefix.json")
for week in range(2):

	for  prefix in prefixs:
		if(prefix == "ББСО-04-20"):
			mass = ["FT","FU","FV","FW"] #ББСО-04-20
		elif prefix == "ББСО-03-20":
			mass = ["FO","FP","FQ","FR"] #ББСО-03-20
		elif prefix == "ББСО-02-20":
			mass = ["FJ","FK","FL","FM"] #ББСО-02-20
		elif prefix == "ББСО-01-20":
			mass = ["EZ","FA","FB","FC"] #ББСО-01-20
		elif prefix == "БСБО-04-20":
			mass = ["GD","GE","GF","GG"] #БСБО-04-20
		elif prefix == "БСБО-18-20":
			mass = ["KJ","KK","KL","KM"] #БСБО-18-20
		elif prefix == "БСБО-16-20":
			mass = ["JZ","KA","KB","KC"] #БСБО-16-20
		elif prefix == "БББО-07-20":
			mass = ["BX","BY","BZ","CA"] #БББО-07-20
		elif prefix == "БПБО-01-20":
			mass = ["IB","IC","ID","IE"] #БПБО-01-20
		elif prefix == "БИСО-01-20":
			mass = ["DG","DH","DI","DJ"] #БИСО-01-200

		column_lesson = mass[0]                 #название пары                  ББСО-04-20
		colum_type = mass[1]                    #тип пары практик/лекция
		colum_fio = mass[2]                     #фио препода
		colum_aud = mass[3]                     #аудитоия

		out_blue("Создание расписание для группы:"+str(prefix))
		for i in range(4,76):
			w +=1
			num_par = sheet['FZ'+str(i-week)].value #это не трогать работает
			if q == 12:
				q = 0
#				print("-----------------------------------")
				day = day + 1
			if i % 2 == week:

				if(str(sheet[column_lesson+str(i)].value) == "None"):
					o=1
				else:
#					print(num_par, "   ", str(sheet[column_lesson+str(i)].value).replace("\n", " "), "     ", sheet[colum_type+str(i)].value, "     ", str(sheet[colum_fio+str(i)].value).replace("\n", " "), "   ", str(sheet[colum_aud+str(i)].value).replace("\n", " "))
					buffer = {}
					buffer["num_para"] = str(num_par)
					buffer["para"] = str(sheet[column_lesson+str(i)].value).replace("\n", " ")
					buffer["type"] = str(sheet[colum_type+str(i)].value).replace("\n", " ")
					buffer["fio"]  = str(sheet[colum_fio+str(i)].value).replace("\n", " ")
					buffer["aud"]  = str(sheet[colum_aud+str(i)].value).replace("\n", " ")
					mass1[day].append(buffer)
			q +=1
#		filemd5 = md5summ(prefix+"/nechet.json")
		if (week == 0):
			make_json(prefix+"/nechet.json",mass1)
			out_blue("Сохранено нечетное расписание для группы " + str(prefix) + " по пути " + str(prefix) + "/nechet.json")
			print("=======================================")
		else:
			make_json(prefix+"/chet.json",mass1)
			out_blue("Сохранено четное расписание для группы " + str(prefix) + " по пути " + str(prefix) + "/chet.json")
			print("=======================================")
#		if (md5summ(prefix+"/chet.json") == filemd5):
#					out_yellow("Расписание группы: "+prefix+" не изменено")
#		else:
#					out_red("Расписание группы: "+prefix+" изменилось")
#					print(filemd5 + " " + md5summ(prefix+"/chet.json"))
		q = 0
		w = 0
		num_par =0
		mass1 = [[],[],[],[],[],[],[]]
		day = 1
