import os
try:
 import requests,json,re
 import base64
 import xml.etree.ElementTree as ET
 from colorama import Fore
 from pyfiglet import Figlet
 import webbrowser
 from time import sleep

except:
 os.system('pip install requests')
 os.system('pip install base64')
 os.system('pip install pyfiglet')
 os.system('pip install colorama')
os.system('clear')
#_____________________________________________
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
V ='\x1b[0;34m'
G ='\x1b[0;36m'
r = requests.get('https://raw.githubusercontent.com/abdo00alo/abdo/main/password').text.strip()
m = input('Password >> ').strip()
if r == m:
	webbrowser.open("https://t.me/abdelgaf777771")
	print(F+'		Done Password')
	sleep(2)
	os.system('clear')
	ramadan_kareem = ""
	abdo_text = "By Abdo"
	f = Figlet(font='small',width=50)
	print("\033[1;31m" + "-" * 50 + "\033[0m")
	print("\033[1;32m" + f.renderText(abdo_text) + "\033[0m")
	print("\033[1;31m" + "-"*50 + "\033[0m")
	text1 = "telegram >> https://t.me/t_e_a_m_dark1\n\nTelegram >> https://t.me/abdelgaf777771"
	print("\033[1;33m" + text1.center(50) + "\033[0m")
	print("\033[1;31m" + "-" * 50 + "\033[0m")
	print()
	
#______________________________
	email = input(Z + '[' + F + '⌯' + Z + ']' + X + ' Email' + Z + ' :\n\n	' + B)
	password = input(Z + '[' + F + '⌯' + Z + ']' + X + ' Password' + Z + ' :\n\n	' + B)
	number = input(Z + '[' + F + '⌯' + Z + ']' + X + ' Number' + Z + ' :\n\n	' + B)
	code = email + ":" + password
	enc = code.encode("ascii")
	base64_bytes = base64.b64encode(enc)
	auth = base64_bytes.decode("ascii")
	xauth = "Basic" + " " + auth
	url1 = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
	head1 = {
				            "applicationVersion": "2",
				            "applicationName": "MAB",
				            "Accept": "text/xml",
				            "Authorization": xauth,
				            "APP-BuildNumber": "964",
				            "APP-Version": "27.0.0",
				            "OS-Type": "Android",
				            "OS-Version": "12",
				            "APP-STORE": "GOOGLE",
				            "Is-Corporate": "false",
				            "Content-Type": "text/xml; charset=UTF-8",
				            "Content-Length": "1375",
				            "Host": "mab.etisalat.com.eg:11003",
				            "Connection": "Keep-Alive",
				            "Accept-Encoding": "gzip",
				            "User-Agent": "okhttp/5.0.0-alpha.11",
				            "ADRUM_1": "isMobile:true",
				            "ADRUM": "isAjax:true"
				        }
				        
	dat1 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
	r1 = requests.post(url1, headers=head1, data=dat1)
	if "true" in r1.text:
		st = r1.headers["Set-Cookie"]
		ck = st.split(";")[0] 
		br = r1.headers["auth"]
		num = number[+1:]
		url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrderV2"
		payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>UNSUBSCRIBE_FANZONE</operation><productName>MAIN_FAN_ZONE</productName></submitOrderRequest>"%num
		headers = {
				  'User-Agent': "okhttp/5.0.0-alpha.11",
				  'Connection': "Keep-Alive",
				  'Accept': "text/xml",
				  'Accept-Encoding': "gzip",
				  'applicationVersion': "2",
				  'applicationName': "MAB",
				  'Language': "ar",
				  'APP-BuildNumber': "10544",
				  'APP-Version': "30.7.0",
				  'OS-Type': "Android",
				  'OS-Version': "12",
				  'APP-STORE': "GOOGLE",
				  'auth': f"Bearer {br}",
				  'Is-Corporate': "false",
				  'Content-Type': "text/xml; charset=UTF-8",
				  'ADRUM_1': "isMobile:true",
				  'ADRUM': "isAjax:true",
				  'Cookie': ck
				}
		response = requests.post(url, data=payload, headers=headers)
		if "true" in response.text:
			sleep(5)
			url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrderV2"
			payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><productName>MAIN_FAN_ZONE</productName></submitOrderRequest>"%num
			headers = {
				  'User-Agent': "okhttp/5.0.0-alpha.11",
				  'Connection': "Keep-Alive",
				  'Accept': "text/xml",
				  'Accept-Encoding': "gzip",
				  'applicationVersion': "2",
				  'applicationName': "MAB",
				  'Language': "ar",
				  'APP-BuildNumber': "10544",
				  'APP-Version': "30.7.0",
				  'OS-Type': "Android",
				  'OS-Version': "12",
				  'APP-STORE': "GOOGLE",
				  'auth': f"Bearer {br}",
				  'Is-Corporate': "false",
				  'Content-Type': "text/xml; charset=UTF-8",
				  'ADRUM_1': "isMobile:true",
				  'ADRUM': "isAjax:true",
				  'Cookie': ck
				}
			req = requests.post(url, data=payload, headers=headers)
			if "true" in req.text:
				print("\033[1;31m" + "-" * 50 + "\033[0m")
				print(F+'	Done Add 100 Mega Renewed✅')
				print("\033[1;31m" + "-" * 50 + "\033[0m")
	
	
	
	
	while True:
		try:
			url1 = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
			head1 = {
				            "applicationVersion": "2",
				            "applicationName": "MAB",
				            "Accept": "text/xml",
				            "Authorization": xauth,
				            "APP-BuildNumber": "964",
				            "APP-Version": "27.0.0",
				            "OS-Type": "Android",
				            "OS-Version": "12",
				            "APP-STORE": "GOOGLE",
				            "Is-Corporate": "false",
				            "Content-Type": "text/xml; charset=UTF-8",
				            "Content-Length": "1375",
				            "Host": "mab.etisalat.com.eg:11003",
				            "Connection": "Keep-Alive",
				            "Accept-Encoding": "gzip",
				            "User-Agent": "okhttp/5.0.0-alpha.11",
				            "ADRUM_1": "isMobile:true",
				            "ADRUM": "isAjax:true"
				        }
				        
			dat1 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
			r1 = requests.post(url1, headers=head1, data=dat1)
	
			if "true" in r1.text:
				st = r1.headers["Set-Cookie"]
				ck = st.split(";")[0] 
				br = r1.headers["auth"]
				num = number[+1:]
				url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/getGenericConsumptionsV2"
				params = {
				  'requestParam': "<dialAndLanguageRequest><segmentId>XRP</segmentId><subscriberNumber>%s</subscriberNumber><language>1</language><shortCode>XRPM3</shortCode></dialAndLanguageRequest>"%num
				}
				
				headers = {
				  'User-Agent': "okhttp/5.0.0-alpha.11",
				  'Connection': "Keep-Alive",
				  'Accept': "text/xml",
				  'Accept-Encoding': "gzip",
				  'applicationVersion': "2",
				  'Content-Type': "text/xml",
				  'applicationName': "MAB",
				  'Language': "ar",
				  'APP-BuildNumber': "10544",
				  'APP-Version': "30.7.0",
				  'OS-Type': "Android",
				  'OS-Version': "12",
				  'APP-STORE': "GOOGLE",
				  'auth': f"Bearer {br}",
				  'Is-Corporate': "false",
				  'ADRUM_1': "isMobile:true",
				  'ADRUM': "isAjax:true",
				  'Cookie': ck
				}
				
				response = requests.get(url, params=params, headers=headers)
				if "true" in response.text:
					root = ET.fromstring(response.text)
					for consumption in root.iter('consumption'):
						product_name = consumption.find('productName')
						if product_name is not None and product_name.text == "هدية السوشيال للأهلي فانز":
							remaining_value = consumption.find('remainingValue')
							if remaining_value is not None:
							
					        				
					        				
				#__________________________________________
								#remaining = int(remaining_value.text)
								float_value = float(remaining_value.text)
								gg = 0
								if float_value <= 20:
									gg += 1
									url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrderV2"
									payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>UNSUBSCRIBE_FANZONE</operation><productName>MAIN_FAN_ZONE</productName></submitOrderRequest>"%num
									headers = {
				  'User-Agent': "okhttp/5.0.0-alpha.11",
				  'Connection': "Keep-Alive",
				  'Accept': "text/xml",
				  'Accept-Encoding': "gzip",
				  'applicationVersion': "2",
				  'applicationName': "MAB",
				  'Language': "ar",
				  'APP-BuildNumber': "10544",
				  'APP-Version': "30.7.0",
				  'OS-Type': "Android",
				  'OS-Version': "12",
				  'APP-STORE': "GOOGLE",
				  'auth': f"Bearer {br}",
				  'Is-Corporate': "false",
				  'Content-Type': "text/xml; charset=UTF-8",
				  'ADRUM_1': "isMobile:true",
				  'ADRUM': "isAjax:true",
				  'Cookie': ck
				}
									response = requests.post(url, data=payload, headers=headers)
									if "true" in response.text:
										sleep(3)
										url = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrderV2"
										payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><productName>MAIN_FAN_ZONE</productName></submitOrderRequest>"%num
										headers = {
				  'User-Agent': "okhttp/5.0.0-alpha.11",
				  'Connection': "Keep-Alive",
				  'Accept': "text/xml",
				  'Accept-Encoding': "gzip",
				  'applicationVersion': "2",
				  'applicationName': "MAB",
				  'Language': "ar",
				  'APP-BuildNumber': "10544",
				  'APP-Version': "30.7.0",
				  'OS-Type': "Android",
				  'OS-Version': "12",
				  'APP-STORE': "GOOGLE",
				  'auth': f"Bearer {br}",
				  'Is-Corporate': "false",
				  'Content-Type': "text/xml; charset=UTF-8",
				  'ADRUM_1': "isMobile:true",
				  'ADRUM': "isAjax:true",
				  'Cookie': ck
				}
										req = requests.post(url, data=payload, headers=headers)
										if "true" in req.text:
											print("\033[1;31m" + "-" * 50 + "\033[0m")
											print(F+f'[{gg}] Done Add 100 Mega Renewed✅')
											print("\033[1;31m" + "-" * 50 + "\033[0m")
										sleep(60)
			
			
								else:
									pass
			
							else:
								pass
						else:
							pass
							
							
				else:
					print(Z+'Check Your Number❌')
					exit()
			else:
				print('Error in email or password❌')
				exit()
			sleep(15)
				
		except Exception as e:
			pass
else:
	print('Worng password')
	exit()