from openpyxl import load_workbook
import json
week = 1
prefix = "БСБО-16-20"
# 1- чет 0 - нечет
wb = load_workbook('table.xlsx')

sheet = wb['Лист1']

q = 1

print("--------------------------------")
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

column_lesson = mass[0]   		#название пары
colum_type = mass[1] 			#тип пары практик/лекция
colum_fio = mass[2]	    		#фио препода
colum_aud = mass[3]     		#аудитоия


#column_lesson = "DB"            #название пары
#colum_type = "DC"               #тип пары практик/лекция
#colum_fio = "DD"                #фио препода
#colum_aud = "DE"                #аудитоия


def make_json(name_file,massiv):
	with open(name_file, 'w') as fw:
	    json.dump(massiv, fw)
	return os.path.getsize(name_file) / 1000000

def load_json(name_file):
        with open(name_file, 'r') as fr:
                return(json.load(fr))
q = 0
w = 0
num_par =0
mass1 = [[],[],[],[],[],[],[]]
day = 1
for i in range(4,76):
	w +=1
	num_par = sheet['FZ'+str(i-week)].value #это не трогать работает
	if q == 12:
		q = 0
		print("-----------------------------------")
		day = day + 1
	if i % 2 == week:

		if(str(sheet[column_lesson+str(i)].value) == "None"):
				print(num_par)
		else:
				print(num_par, "   ", str(sheet[column_lesson+str(i)].value).replace("\n", " "), "     ", sheet[colum_type+str(i)].value, "     ", str(sheet[colum_fio+str(i)].value).replace("\n", " "), "   ", str(sheet[colum_aud+str(i)].value).replace("\n", " "))
				buffer = {}
				buffer["num_para"] = str(num_par)
				buffer["para"] = str(sheet[column_lesson+str(i)].value).replace("\n", " ")
				buffer["type"] = str(sheet[colum_type+str(i)].value).replace("\n", " ")
				buffer["fio"]  = str(sheet[colum_fio+str(i)].value).replace("\n", " ")
				buffer["aud"]  = str(sheet[colum_aud+str(i)].value).replace("\n", " ")
				mass1[day].append(buffer)
	q +=1

