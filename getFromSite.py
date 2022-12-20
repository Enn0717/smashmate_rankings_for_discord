import requests
from bs4 import BeautifulSoup
import re

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getRate(id):
	url = 'https://smashmate.net/user/'+str(id)
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text, "html.parser")
	elems = soup.find_all("span", class_="rate_text")
	elem = elems[0].contents[0]
	rate = re.sub(r"\D","",elem)
	return rate

def getRateMax(id):
	url = 'https://smashmate.net/user/'+str(id)
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text, "html.parser")
	elems = soup.find_all("span", class_="rate_text")
	try:
		elem = elems[1].contents[0]
		rate = re.sub(r"\D","",elem)
	except:
		rate = 0
	return rate

def getName(id):
	url = 'https://smashmate.net/user/'+str(id)
	res = requests.get(url, verify=False)
	soup = BeautifulSoup(res.text, "html.parser")
	elems = soup.find_all("span", class_="user-name")
	elem = elems[0].contents[0]
	return elem