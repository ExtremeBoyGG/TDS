#coding: utf-8

# OPEN SOURCE TDS BOT FREE TO USE
import os, sys, re, json
from time import sleep
fbid = []
from datetime import datetime
import requests
dem=0
salah=0
os.system("clear")
merah = '\033[1;91m'
sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m ➺❥ \033[1;92m"
logo = """
\033[1;92m             ████████╗██████╗ ███████╗
\033[1;91m             ╚══██╔══╝██╔══██╗██╔════╝
\033[1;93m                ██║   ██║  ██║███████╗
\033[1;96m                ██║   ██║  ██║╚════██║
\033[1;97m                ██║   ██████╔╝███████║
\033[1;95m                ╚═╝   ╚═════╝ ╚══════╝
"""
def NotFound():
	exit(merah+'TIDAK ADA MISI, SILAHKAN COBA NANTI')
t=datetime.now().strftime("%H:%M:%S")
print(logo)
try:
	hung=open('tokentds.txt').read()
	hdoi='n'
except FileNotFoundError:
	hung=input(sr+'Masukkan Token TDS : ')
	file=open('tokentds.txt','w')
	file.write(hung)
	file.close()
	hdoi='n'
if hdoi.lower()=='y':
	h=open('tokentds.txt',mode='w')
	os.system('clear')
	print(logo)
	htk=input(sr+'Masukkan Token TDS : ')
	h.write(htk)
	h.close()
	TDS_Token=htk
else:
	TDS_Token=hung
log=json.loads(requests.get("https://traodoisub.com/api/?fields=profile&access_token="+ TDS_Token).text)
try:
	open('tokenfb.txt').read()
except FileNotFoundError:
	Token_fb=input(sr+'Masukkan Token FB : ')
	file=open('tokenfb.txt','w')
	file.write(Token_fb)
	file.close()
if "success" in log:
	print(f"{sr} Login Berhasil !")
	xu=log['data']['xu']
	user=log['data']['user']
	sleep(0.5)
	os.system('clear')
	print(logo)
	print("-"*50)
	print(f"{sr} Username TDS : {user}")
	print(f"{sr} Koin Terkumpul : {xu}")
	print("-"*50)
	try:
		Token_fb=open('tokenfb.txt').read()
	except FileNotFoundError:
		Token_fb=input(sr+' Masukkan Token Facebook : ')
		file=open('tokenfb.txt','w')
		file.write(Token_fb)
		file.close()
	check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+Token_fb).text)
	try:
		idfb = check_token['id']
	except KeyError:
		os.remove('tokenfb.txt')
		exit(merah+' TOKEN INVALID ')
	fbid.append(idfb)
	namefb = check_token['name']
	run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+TDS_Token).text)
	if "success" in run:
		os.system("clear")
		print(logo)
		print("-"*50)
		print(f"{sr} Username TDS   : {user}")
		print(f"{sr} Koin Terkumpul : {xu}")
		print("-"*50)
		print("\033[1;92m🌍 Akun FB : " + str(namefb) +" | ID " + str(idfb))
		print('-'*50)
		print(f"{sr}\033[1;92m [00] \033[1;91mHapus Token TDS")
		print(f"{sr}\033[1;92m [01] Jalankan Misi Like")
		print(f"{sr}\033[1;92m [02] Jalankan Misi Follow")
		print("-"*50)
		try:
			ls=int(input(f"{sr} Pilih Nomor : "))
		except ValueError:
			exit(merah+'INVALID INPUT')
		delay=int(input(f"{sr} Delay : "))
		print("-"*50)
		print('Tekan CTRL+C ATAU CTRL+Z Untuk Berhenti')
		print("-"*50)
		if ls==0:
			yakin=input(sr+merah+'Apakah Anda Yakin? (y/n) : \033[1;37m')
			if yakin.lower()=='y':
				os.remove('tokentds.txt')
				exit('[#] Selesai')
			else:
				exit()
		while True:
			if ls==1:
				try:
					getlike=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+TDS_Token).json()
					idlike=getlike[0]['id']
				except IndexError:NotFound()
				urllike='https://graph.facebook.com/'+str(idlike)+'/reactions?type='+getlike[0]['type']
				datalike="access_token="+Token_fb
				like=requests.post(urllike, data=datalike)
				nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+TDS_Token).text)
				id=idlike[0:15]
				if "success" in nhan:
					dem=dem+1
					t=datetime.now().strftime("%H:%M:%S")
					print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92m{getlike[0]['type']}\033[1;97m]\033[1;92m {idlike} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
					for demtg in range(delay,-1,-1):
						print(f"♡Delay {demtg}",end='\r')
						sleep(1)
				else:
					print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {idlike}")
					testing=requests.get('https://graph.facebook.com/me?access_token='+Token_fb).json()
					salah+=1
					if salah==6:
						os.remove('tokenfb.txt')
						exit(merah+' TOKEN INVALID ')
					try:
						nama=testing['id']
					except KeyError:
						os.remove('tokenfb.txt')
						exit('\r'+merah+' TOKEN INVALID ')

			elif ls==2:
				try:
					getsub=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+TDS_Token)
					idsub=getsub.json()[0]['id']
				except IndexError:NotFound()
				datasub = "access_token="+Token_fb
				urlsub = 'https://graph.facebook.com/'+str(idsub)+'/subscribers'
				sub=requests.post(urlsub, data=datasub)
				nhan = json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idsub)+'&access_token='+TDS_Token).text)
				if "success" in nhan:
					dem=dem+1
					t=datetime.now().strftime("%H:%M:%S")
					print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idsub} \033[1;97m[\033[1;92m+600\033[1;97m] \033[1;97m[\033[1;92m{str(nhan['data']['xu'])}\033[1;97m]")
					for demtg in range(delay,-1,-1):
						print("♡Delay "+str(demtg),end='\r')
						sleep(1)
				else:
					print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mFOLLOW\033[1;97m]\033[1;92m {idsub}",end='\r')
					testing=requests.get('https://graph.facebook.com/me?access_token='+Token_fb).json()
					salah+=1
					if salah==6:
						os.remove('tokenfb.txt')
						exit(merah+' TOKEN INVALID ')
					try:
						nama=testing['id']
					except KeyError:
						os.remove('tokenfb.txt')
						exit('\r'+merah+' TOKEN INVALID ')
			else:
				print(sr+"Error!!")
		else:
			exit(merah+"Masukkan ID "+fbid[0]+" Ke Konfigurasi !")
	else:
		try:
			os.remove('tokenfb.txt')
		except:pass
		exit(merah+"Token Die")
else:
	os.remove('tokentds.txt')
	print(f"{sr}Token TDS INVALID !")


#credit: Duyhoan
