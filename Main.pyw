from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pyqt_fix
import functions_algorithms as f_a
import visual_algorithms as v_a
class MainWindow(QtWidgets.QWidget):
	def __init__(self,parent = None):
		QtWidgets.QWidget.__init__(self,parent)
		self.setAutoFillBackground(True)
		self.label = QtWidgets.QLabel("Нажмите  кнопку чтобы  добавить запись")
		self.accept_button = QtWidgets.QPushButton("добавить")
		self.output_button = QtWidgets.QPushButton("посчитать все доходы за выбранный промежуток дней")
		self.graph_button = QtWidgets.QPushButton("построить график расходов по дням за выбранный промежуток дней")
		self.diag_button = QtWidgets.QPushButton("Траты по категориям за выбранный промежуток дней")
		self.csv_button = QtWidgets.QPushButton("таблица расходов за кол-во дней")
		self.save_button = QtWidgets.QPushButton("подтвердить")
		self.vbox = QtWidgets.QVBoxLayout()
		self.line = QtWidgets.QSpinBox()
		self.line.setMaximum(99999999)
		self.value = None
		self.checkbox = QtWidgets.QCheckBox("расход")
		self.date = QtWidgets.QDateEdit()
		self.date.setCalendarPopup(True)
		self.accept_button.clicked.connect(self.write_dictionary)
		self.category_сhoice_button = QtWidgets.QPushButton("Категория")
		self.category_сhoice_button.clicked.connect(f_a.draw_dialog)
		self.output_button.clicked.connect(f_a.draw_days_dialog)
		self.graph_button.clicked.connect(v_a.set_keyword_graph)
		self.diag_button.clicked.connect(v_a.set_keyword_diag)
		self.csv_button.clicked.connect(v_a.set_keyword_csv)
		self.dictionary = None
	
	
		##группировка
		self.box1 =  QtWidgets.QGroupBox()
		self.box2 = QtWidgets.QGroupBox()
		self.box3 = QtWidgets.QGroupBox()
		self.group1 = QtWidgets.QHBoxLayout()
		self.group2 = QtWidgets.QHBoxLayout()
		self.group3 = QtWidgets.QHBoxLayout()
	
		self.group1.addWidget(self.accept_button)
		self.group1.addWidget(self.line)
		self.group1.addWidget(self.checkbox)
		self.group1.addWidget(self.date)
		self.group1.addWidget(self.category_сhoice_button)
		
		self.group2.addWidget(self.output_button)
		self.group2.addWidget(self.graph_button)
		self.group2.addWidget(self.diag_button)
		
		self.group3.addWidget(self.csv_button)
		
		
		
		
		self.box1.setLayout(self.group1)
		self.box2.setLayout(self.group2)
		self.box3.setLayout(self.group3)
		##группировка
		
		self.toolbox = QtWidgets.QToolBox()
		self.toolbox1 = QtWidgets.QToolBox()
		self.toolbox2 = QtWidgets.QToolBox()
		self.toolbox.addItem(self.box1,'добавить доход/расход')
		self.toolbox1.addItem(self.box2,'анализ доходов/расходов')
		self.toolbox1.addItem(self.box3,'Таблица расходов/доходов')
		
		self.vbox.addWidget(self.toolbox)
		self.vbox.addWidget(self.toolbox1)
		self.vbox.addWidget(self.toolbox2)
		
	

	
	def accept_data(self):
		self.dictionary = self.get_values()
		
	def set_category():
		return category
		
	def write_dictionary(self):
		if self.checkbox.checkState():
			summ = -self.line.value()
		else:
			summ = self.line.value()
		pre_date = self.date.date()
		date = pre_date.toPyDate()
		cat_file = open('cat.txt','r')
		category = cat_file.read()
		dictionary = f_a.create_dictionary(summ,date,category)
		dec_dict= json.dumps(dictionary,ensure_ascii=False)
		dec_dict = dec_dict
		with open('in_out_data.json', 'a') as f:
			f.write(dec_dict + '\n')		
	
		cat_file.close()
		
			
		
			
class ListDialogWindow(QtWidgets.QWidget):
	def __init__(self,title,descrip,var_list,parent = None):
		QtWidgets.QWidget.__init__(self,parent)
		
		self.title = title
		self.descrip = descrip
		self.var_list = var_list
		self.vbox = QtWidgets.QVBoxLayout()
		self.list_dialog,self.list_ok = QtWidgets.QInputDialog.getItem(None,self.title,self.descrip,self.var_list,editable = False)
		
		

class MoneyOutputWindow(QtWidgets.QWidget):
	def __init__(self,summ,days,parent = None):
		QtWidgets.QWidget.__init__(self,parent)
		
		self.vbox = QtWidgets.QVBoxLayout()
		self.money_message = summ
		self.days = days
		self.text_message = ''
		self.message_set() 
		self.message = (self.text_message + ">>>" + str(-self.money_message) + " Рублей")
		self.dialog = QtWidgets.QMessageBox.information(None,"Расходы/Доходы за " + self.days +  " :дней",self.message,buttons=QtWidgets.QMessageBox.Close,defaultButton=QtWidgets.QMessageBox.Close)
			
	def message_set(self):
		if self.money_message > 0:
			self.text_message =  'Ваша прибыль за последние ' + self.days +   ' :дней:'
		elif self.money_message < 0:
			self.text_message =  'Ваш убыток за последние ' + self.days + ': дней:'
		else:
			'За последние' +  'дней ваша финансовое состояние не изменилось'
		
			

			
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.setWindowTitle("контроль расходов")
	window.setLayout(window.vbox)
	window.resize(1200,420)
	window.show()
	sys.exit(app.exec_())
