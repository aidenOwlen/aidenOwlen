import time 
from Tkinter import * 
import xlrd
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from tkMessageBox import * 
from threading import Thread, RLock
import re





class interface(Frame):
	class Start_it(Thread):
		def __init__(self):
			Thread.__init__(self)
		def run(self):
			book = xlrd.open_workbook("fbP.xlsx")
			first_sheet = book.sheet_by_index(0)
			p = 0
			try:
				chrome_path = "chromedriver.exe"
				driver = webdriver.Chrome(chrome_path)
			 	driver.get("https://en-gb.facebook.com/login/")
			 	username1 = driver.find_element_by_id("""email""")

			 	
				username1.send_keys(Interface.username.get(0.0, END))
				
				password1 = driver.find_element_by_id("""pass""")
				password1.send_keys(Interface.password.get(0.0, END))
				
				driver.find_element_by_id("""loginbutton""").click()
				
			except:
				pass
			while 1:
				    
				 	try:
				 		urll = first_sheet.cell(p,0)
				 		
				 		msgg = first_sheet.cell(p,1)

				 		url = urll.value
				 		msg = msgg.value
				 		
				 		driver.get(url)
				 		time.sleep(5)
				 		
				 		box_count = len(driver.find_elements_by_class_name("innerWrap"))
				 		for x in range(0, box_count):
				 			text_box = driver.find_element_by_tag_name('textarea')
				 			text_box.send_keys(msg)
				 		time.sleep(3)


				 		driver.find_element_by_xpath(("//*[text()='Post']")).click()
				 		time.sleep(6)
				 		
				 		xx = Interface.combo.curselection()
				 		x = re.search("(?P<grp1>[0-9]{1,4})","""str({})""".format(xx))
				 		
				 		time.sleep(float(x.group("grp1")))
				 		Interface.texte.insert(END, "{}) Url : {}\nText : {} \n\n".format(p,url, msg))
				 		Interface.texte.see(END)
				 		p +=1
				 		

				 	except IndexError:
				 		Interface.texte.insert(END, "\n\n END")
				 		Interface.texte.see(END)
				 		
				 		break
				 	except:
				 		Interface.texte.insert(END, "{}) Url : {}\nText : {} #Page didn't allow post \n\n".format(p,url, msg))
				 		p +=1



	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width = 900, height = 500, **kwargs)
		self.pack(fill = BOTH)

		self.combo = Listbox(self, height = 1, width = 10)
		i = 0
		while i < 300:
			
			self.combo.insert(END, i)
			i += 1
		self.combo.grid(row = 0, column = 0)
		self.texte = Text(self, width = 30, fg = "blue", height = 15)
		self.texte.grid(row = 3, column = 0, sticky = NS)
		self.but = Button(self, text = "Start", command = self.start)
		self.but.grid(row = 4, column = 0)
		self.username = Text(self, height = 1, width = 29)
		self.username.grid(row=1, column = 0)
		self.bar = Scrollbar(self)
		self.password = Text(self, height = 1, width = 29)
		self.password.grid(row=2, column = 0)
		self.bar.config(command = self.texte.yview)
		self.texte.config(yscrollcommand = self.bar.set)
		self.bar.grid(row=3, column=1,sticky=NS)
		self.start_it = self.Start_it()


	def start(self):
		
		self.start_it.start()
		self.start_it.join()
		
	   	    

		 	
fenetre = Tk()
Interface = interface(fenetre)
Interface.mainloop()



