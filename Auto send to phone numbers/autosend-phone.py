from tkinter import *
from tkinter import filedialog
import tkinter.ttk
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import bs4 as bs
from selenium.webdriver.common.by import By
import time

class TextBot:
	fenetre = Tk()
	fenetre.configure(background = "deep sky blue")

	def __init__(self):
		Label(self.fenetre, text = "Username", fg = "black", bg = "deep sky blue").grid(row=0,column=0)
		self.Username = Entry(self.fenetre, bg = "deep sky blue",fg = "white")
		self.Username.grid(row=0,column=1)

		Label(self.fenetre, text = "Password", fg = "black", bg = "deep sky blue").grid(row=1,column=0)
		self.Password = Entry(self.fenetre, bg="deep sky blue",show = "*",fg ="white")
		self.Password.grid(row=1,column=1)

		self.Message = ScrolledText(self.fenetre, bg="light sky blue", width = 30, height = 10,fg = "black")
		self.Message.grid(row=2,column=0, columnspan=4)
		self.Message.insert(0.0, "Your message here")

		self.Phones = Button(self.fenetre, bg="deep sky blue",fg ="blue", text = "Import phone numbers", width = 33,command = self.phone)
		self.Phones.grid(row=3,column=0,columnspan = 4, sticky=NW)
		self.PhoneNumbers = ScrolledText(self.fenetre, bg ="light sky blue", width = 30, height =10,fg = "black")
		self.PhoneNumbers.grid(row=4,column=0,columnspan=4)
		self.PhoneNumbers.insert(0.0, "Phone numbers will be uploaded here")

		self.Start = Button(self.fenetre, bg = "deep sky blue", fg = "blue",text = "Start bot", width = 33, command = self.start)
		self.Start.grid(row=8,column=0,columnspan=4,sticky=NW)

		Label(self.fenetre, text = "Sleep (s)", bg = "deep sky blue",fg ="black").grid(row=5, column=0)
		self.sleeping = IntVar()
		self.Sleep = tkinter.ttk.Combobox(self.fenetre, width = 30,textvariable = self.sleeping)
		self.Sleep.grid(row=5, column=1)
		self.Sleep["value"] = list(range(4,400,4))
		self.Sleep.current(0)

		self.DelOrNot = IntVar()
		self.DeleteMessage = Checkbutton(self.fenetre, text = "delete messages after each X message", fg = "blue",bg = "deep sky blue", variable = self.DelOrNot,command = self.checked)
		self.DeleteMessage.grid(row = 6, column =0,columnspan = 2, sticky = NW)

		self.Each = IntVar()
		self.EachX = tkinter.ttk.Combobox(self.fenetre, textvariable = self.Each,width = 12)
		



		self.fenetre.mainloop()

	def start(self):
		self.MESSAGE = self.Message.get(0.0,END)
		self.MESSAGE = self.MESSAGE.split("*\n")
		print(self.MESSAGE)
		self.tt = self.sleeping.get()
		self.driver = webdriver.Chrome()
		self.driver.get("https://textfree.us/")
		

		self.url = self.driver.current_url
		oo = open(self.filename,"r")
		self.Numeros = oo.readlines()
		oo.close()
		self.wait = WebDriverWait(self.driver, 20)
		self.wait.until(EC.presence_of_element_located((By.NAME,"username")))
		self.driver.find_element_by_name("username").send_keys(self.Username.get())
		self.wait.until(EC.presence_of_element_located((By.NAME,"password")))
		self.driver.find_element_by_name("password").send_keys(self.Password.get())
		try:
			self.driver.find_element_by_xpath("""//*[@id="loginForm"]/div[3]/button""").click()
		except:
			self.driver.find_element_by_xpath("""//*[@id="loginForm"]/div[3]/button""").submit()

		t = 0
		while t <= 20:
			time.sleep(self.tt/4)
			t+= 1
			if self.driver.current_url != self.url:
				break
		self.driver.get("https://textfree.us/#/conversation")
		self.counting = 0
		self.M = 0
		for j in self.Numeros:
			try:
				self.MESSAGE[self.M]
			except IndexError:
				self.M = 0
			
			self.wait.until(EC.presence_of_element_located((By.ID,"startNewConversationButton")))
			try:
				self.driver.find_element_by_id("startNewConversationButton").click()
			except:
				self.driver.find_element_by_id("startNewConversationButton").submit()

			self.wait.until(EC.presence_of_element_located((By.ID, "contactInput")))

			try:
				self.driver.find_element_by_id("contactInput").send_keys(j)
			except:
				pass


			time.sleep(self.tt/4)
			d = self.driver.find_elements_by_tag_name("div")
			for i in d:
				try:
					i.send_keys(self.MESSAGE[self.M])
				except:
					pass
			time.sleep(self.tt/4)

			try:
				self.driver.find_element_by_id("sendButton").click()
			except:
				self.driver.find_element_by_id("SendButton").submit()
			time.sleep(self.tt/4)
			self.counting+=1
			

			if self.DelOrNot.get() == 1:
				

				if self.counting == self.Each.get():
					for l in range(10):
						try:
							self.driver.find_element_by_xpath("/html/body/div[1]/conversation-container/div/div/aside[1]/conversation-list/div[3]/conversation-list-element/div/div[1]").click()
							time.sleep(1)
							self.driver.find_element_by_xpath("/html/body/div[1]/conversation-container/div/div/aside[1]/conversation-list/div[3]/conversation-list-element/div/div[3]").click()
							time.sleep(1)
							dd = self.driver.find_elements_by_tag_name("li")
							for kk in dd:
								if str(kk.get_attribute("id")) == "deleteButton":
									try:
										kk.click()
										self.wait.until(EC.presence_of_element_located((By.ID, "deleteBtn")))
										self.driver.find_element_by_id("deleteBtn").click()
									except:
											pass
								


						except:
							pass
					self.counting = 0
				self.M += 1
				


#deleteBtn



	def phone(self):
		self.filename = filedialog.askopenfilename()
		op = open(self.filename, "r")
		rop = op.read()
		self.PhoneNumbers.insert(0.0,rop)
		op.close()

	def checked(self):
		if self.DelOrNot.get() == 1:
			self.EachX.grid(row=7,column=0,columnspan = 2,sticky=NW)
		else:
			self.EachX.grid_forget()







TextBot()


