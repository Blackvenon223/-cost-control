import  Main
import json
def draw_dialog():
	window = Main.ListDialogWindow("Категория","выберите категорию из предложенного списка",["спорт","питание","здоровье","образование","транспорт","развлечения","другое"])
	main_window = Main.MainWindow()
	if window.list_ok:
		category = window.list_dialog
		cat_file = open('cat.txt','w')
		cat_file.write(str(category))
		cat_file.close()
		
		

def create_dictionary(summ,date,category = 'не выбрана'):
	in_out_dictionary = {'сумма': None,'дата':  None,'категория':  None}
	in_out_dictionary['сумма'] = summ

	in_out_dictionary['дата'] = str(date)
	if summ < 0:
		in_out_dictionary['категория'] = category
	else:
		in_out_dictionary.pop('категория')
	return in_out_dictionary
	
	
def get_summ(days):
	dicts = []
	nums = []
	summ = 0
	for line in open('in_out_data.json','r'):
		dicts.append(json.loads(line))
	dicts = dicts[::-1]
	print(dicts)
	for elem in dicts[:days]:
		nums.append(elem['сумма'])
	print (nums)
	for num in nums:
		summ += num
	print(summ)
	draw_out_in_dialog(summ,str(days))
	
	
def draw_out_in_dialog(summ,days):
	summ = summ
	days = days
	out_in_window = Main.MoneyOutputWindow(summ,days)
	
	
	
def draw_days_dialog():
	days_choice = Main.ListDialogWindow("Кол-во дней","Выберите кол-во дней",['30','60','90','120','180','240','365','730','3650'])
	if days_choice.list_ok:
		days = int(days_choice.list_dialog)
		get_summ(days)
	
	

	
	
