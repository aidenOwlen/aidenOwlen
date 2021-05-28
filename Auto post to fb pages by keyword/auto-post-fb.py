from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options 
import bs4 as bs
import time
import re


#FACEBOOK LOGS
Username = "USERNAME"
Password = "PASSWORD"

#KEYWORD
Keyword = "Keyword"
 

def Find_Pages(Keyword):
	""" This functions return 2 lists : Pages & groups , support 1 parameter for the keyword to search for .
	Pages,Groups = Find_Pages(Your_keyword)
	It takes about 20 seconds to scroll down and capture urls """

	Pages = []
	Groups = []
	driver.get("https://www.facebook.com/search/pages/?q={}".format(Keyword))
	time.sleep(4)
	h = driver.find_elements_by_tag_name("a")
	for g in h:
		try:
			if g.get_attribute("action") == "cancel" and g.get_attribute("role") == "button":
				g.click()
		except:
			pass
	iba3 = 0		
	while iba3 < 20:
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		iba3 += 1

	Tag_P = driver.find_elements_by_tag_name("a")
	for kali in Tag_P:
		try:
			sobek = kali.get_attribute("href")
			if re.match("https://www.facebook.com/" + Keyword.lower() + "|" + Keyword.upper() + "|" + Keyword.capitalize() + "|" + Keyword + ".*/?ref=br_rs",sobek) is not None:
				Pages.append(sobek)
		except:
			pass
	Pages = list(set(Pages)) ############ REMOVE DUPLICATE URLS
	
	driver.get("https://www.facebook.com/search/groups/?q={}".format(Keyword))
	time.sleep(4)
	iba3 = 0
	while iba3 < 20:
		time.sleep(1)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		iba3 += 1
	Tag_G = driver.find_elements_by_tag_name("a")
	for fuckshit in Tag_G:
		try:
			tnakt = fuckshit.get_attribute("href")
			dd = re.search("/groups/(?P<grp1>.*)/?ref=br_rs",tnakt)
			if dd is not None:				
				Groups.append(tnakt)
		except:
			pass
	Groups = list(set(Groups))
	return Pages,Groups



if __name__ == "__main__":
	chrome_options = Options()
	chrome_options.add_argument("--start-maximized")
	driver = webdriver.Chrome(chrome_options = chrome_options)
	driver.get("https://www.facebook.com")
	driver.find_element_by_name("email").send_keys(Username)
	driver.find_element_by_name("pass").send_keys(Password)
	tag = driver.find_elements_by_tag_name("input")
	for j in tag:
		try:
			if j.get_attribute("value") == "Connexion" and j.get_attribute("type") == "submit":
				try:
					j.submit()
				except:
					print("Error 1")
		except:
			pass

	Pages,Groups = Find_Pages(Keyword)
	print("PAGES : ##################################")
	print(Pages)
	print("\n\n")
	print("GROUPES : ###############################")
	print(Groups)






