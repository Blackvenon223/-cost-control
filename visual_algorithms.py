from datetime import datetime
from matplotlib import pyplot as plt
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
import Main
import json
import csv
import pandas



def set_keyword_diag():
	keyword = 'diag'
	draw_days_dialog(keyword)
def set_keyword_graph():
	keyword = 'graph'
	draw_days_dialog(keyword)
	
def  set_keyword_csv():
	keyword = 'csv'
	draw_days_dialog(keyword)
def draw_days_dialog(keyword):
	keyword = keyword
	days_choice = Main.ListDialogWindow("Кол-во дней","Выберите кол-во дней",['30','60','90','120','180','240','365','730','3650'])
	if days_choice.list_ok:
		days = int(days_choice.list_dialog)
		get_data(days,keyword)
		
		
		
def get_data(days,keyword):
	keyword = keyword
	days = days
	categorys = []
	dicts = []
	all_nums = []
	outcome_nums = []
	dates = []
	dataframe = []
	if keyword == 'csv':
		for line in open('in_out_data.json','r'):
			dicts.append(json.loads(line))
		dicts = dicts[::-1]
		for elem in dicts[:days]:
			all_nums.append(elem['сумма'])
			dates.append(elem['дата'])
			if 'категория' in elem.keys():
				categorys.append(elem['категория'])
			else:
				categorys.append("")
		
	load_csv(all_nums,(dates),categorys,days)
	if keyword == 'graph':
		for line in open('in_out_data.json','r'):
			dicts.append(json.loads(line))
		dicts = dicts[::-1]
		for elem in dicts[:days]:
			all_nums.append(elem['сумма'])
			dates.append(elem['дата'])
		draw_save_graph(all_nums,dates,str(days))
	elif keyword == 'diag':
		nums = [0,0,0,0,0,0,0]
		for line in open('in_out_data.json','r'):
			dicts.append(json.loads(line))
		dicts = dicts[::-1]
		for elem in dicts[:days]:
			if 'категория' in elem.keys():
				if elem['категория'] == 'спорт':
					nums[0] += elem['сумма']
				elif elem['категория'] == 'питание':
					nums[1] += elem['сумма']
				elif elem['категория'] == 'здоровье':
					nums[2] += elem['сумма']
				elif elem['категория'] == 'образование':
					nums[3] += elem['сумма']
				elif elem['категория'] == 'транспорт':
					nums[4] += elem['сумма']
				elif elem['категория'] == 'развлечения':
					nums[5] += elem['сумма']
				elif elem['категория'] == 'другое':
					nums[6] += elem['сумма']
		
				
			
		draw_save_diag(nums,str(days))
	
def draw_save_graph(nums,dates,days):
	nums = nums[::-1]
	dates = dates[::-1]
	days = days
	fig = plt.figure(dpi = 128,figsize=(20,10))
	plt.plot(dates,nums,c = 'red')
	f = open('files_counter_graph.txt','r')
	counter = int(f.read(1))
	count = counter + 1
	f = open('files_counter_graph.txt','w')
	f.write(str(count))
	f.close()
	plt.savefig('график доходов расходов за'+days+'дней'+str(counter)+'.png')
	plt.show()
	

def draw_save_diag(nums,days):
	pre_nums = nums
	ready_nums = []
	for i in pre_nums:
		i = -i
		ready_nums.append(i)
	categorys = ["спорт","питание","здоровье","образование","транспорт","развлечения","другое"]
	my_style = LS('#333366', base_style = LCS)
	chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=True)
	chart.title = "Расходы по категориям"
	chart.x_labels = categorys
	chart.add('',ready_nums)
	f = open('files_counter_diag.txt','r')
	counter = int(f.read(1))
	count = counter + 1
	f = open('files_counter_diag.txt','w')
	f.write(str(count))
	f.close()
	chart.render_to_file('диаграмма расходов по категориям за'+days+'дней'+str(counter)+'.svg')
	

def load_csv(nums,dates,categorys,days):
	nums = nums
	pre_dates = dates
	ready_dates = []
	i = 0
	for dat in pre_dates:
		one_date = pre_dates[i]
		ready_data = datetime.strptime(one_date,'%Y-%m-%d').date()
		ready_dates.append(one_date)
		i +=1
	categorys = categorys
	days = days
	list1 = [nums,ready_dates,categorys]
	f = open('files_counter_csv.txt','r')
	counter = int(f.read(1))
	count = counter + 1
	f = open('files_counter_csv.txt','w')                                        
	f.write(str(count))
	f.close()
	path = ('доходы_расходы за'+str(days)+str(count)+'.csv')
	with open(path, "w", newline='') as csv_file:
		writer = csv.writer(csv_file, delimiter=';')
		for line in list1:
			writer.writerow(line)
