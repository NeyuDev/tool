# Dec by KhanhNguyen9872

den='[1;90m'
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\e[35m'
hong='[1;95m'
thanh_xau=trang+'~'+red+'['+vang+'⟨⟩'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'✓'+red+'] '+trang+'➩ '+luc
import requests,json,os,sys
from sys import platform
from datetime import datetime        
from time import sleep,strftime
try:from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:os.system('pip install pystyle'); from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
bug_duoc_cai_lon={'pass':'bongocvidaii'}
def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1',53))
        return True
    except OSError:
        pass
    return False
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
banners=f"""   ███╗   ██╗   ████████╗ ██████╗  ██████╗ ██╗     \n   ████╗  ██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n   ██╔██╗ ██║█████╗██║   ██║   ██║██║   ██║██║     \n   ██║╚██╗██║╚════╝██║   ██║   ██║██║   ██║██║     \n   ██║ ╚████║      ██║   ╚██████╔╝╚██████╔╝███████╗\n   ╚═╝  ╚═══╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"""
thongtin=f"""        \033[1;37mCopyright © N-Tool 2022 | Version 3.2\n\033[1;31m────────────────────────────────────────────────────────\n\033[1;37m~\033[1;31m[\033[1;32m●\033[1;31m]\033[1;37m ➩\033[1;35m Admin: \033[1;36mNguyễn Chính Ngọc  \n\033[1;37m~\033[1;31m[\033[1;32m●\033[1;31m]\033[1;37m ➩\033[1;36m Zalo: \033[1;31m0369889638\n\033[1;37m~\033[1;31m[\033[1;32m●\033[1;31m]\033[1;37m ➩\033[1;32m Box Zalo: \033[1;37mhttps://zalo.me/g/cklqap965\n\033[1;37m~\033[1;31m[\033[1;32m●\033[1;31m]\033[1;37m ➩\033[1;33m YouTube: \033[1;37mhttps://youtube.com/@ngoctool\n\033[1;37m~\033[1;31m[\033[1;32m●\033[1;31m]\033[1;37m ➩ {Colorate.Horizontal(Colors.yellow_to_red, 'Mua Key Tại: ')}{Colorate.Horizontal(Colors.white_to_red, 'ngocbansub.com  ')}\n\033[1;31m────────────────────────────────────────────────────────\033[0m"""
# def luu(key):
# 	try:
# 		luu=requests.get('https://sever.ngocbansub.com/api_by_ngoc/luuip.php?key='+key).txt
# 	except:
# 		pass
# def checkkey(key):
# 	try:
# 		check_keyphi=requests.get(f'https://sever.ngocbansub.com/api_by_ngoc/checkkey.php?key={key}').json()
# 		if check_keyphi['status']=='success':
# 			return check_keyphi['name'],check_keyphi['coun']
# 		else:
# 			return[check_keyphi['messenger']]
# 	except:
# 		return False
def bongoc(so):
	a='────'*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.000003)
	print()
def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
	    os.system('cls')
def banner():
	print('[0m',end='')
	clear()
	a=Colorate.Horizontal(Colors.yellow_to_red,banners)
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
	print()
	print(thongtin)
try:
	#a='[1;32mVui Lòng Chờ...[0m'
	#for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		#sleep(0.05)
	# url=requests.post(f'https://sever.ngocbansub.com/api_by_ngoc/key2.php',headers=headers,data=bug_duoc_cai_lon).json()
	# ip=url['ip']
	# coun=url['coun']
except:
#	ip=vang+'null'
	coun=vang+'null'
exec(open('bansaongocv3.2/lib.py','rb').read())
# try:
# 	exec(requests.post('https://sever.ngocbansub.com/code_by_ngoc/key.php',data={'pass':'bongocvidai'}).text)
# except:
# 	print('Sever Gặp Lỗi Hãy Liên Hệ Admin')
# banner()
# while True:
# 	check_file_key=os.path.exists('key_N-Tool.txt')
# 	if check_file_key==False:
# 		print(f'{thanh_xau}{luc}Tool Đã Bỏ Key Free Mọi Người Mua Key Nhé Chỉ 500₫/ngày')
# 		print(f'{thanh_xau}{luc}Số Lượt Truy Cập Tool: {vang}{coun}')
# 		print(f'{thanh_xau}{luc}IP Hiện Tại Của Bạn Là: {vang}{ip}')
# 		print('[1;31m────────────────────────────────────────────────────────')
# 		key=input(f'{thanh_xau}{luc}Nhập Api Key Đã Mua: {vang}');print(red,end='')
# 		bongoc(14)
# 		check_keyphi=checkkey(key)
# 		if check_keyphi==False:print(red+'Sever Key Phí Gặp Lỗi Hãy Dùng Key Free'); continue 
# 		elif check_keyphi !=False:
# 			try:
# 				name=check_keyphi[0];coun=check_keyphi[1];check=True;keycode=key
# 				print(f'{lam}Key API Chính Xác')
# 				luu(key)
# 				file_key=open(f"key_N-Tool.txt",'a+')
# 				file_key.write(key)
# 				file_key.close()
# 				break
# 			except:
# 				print(f"{red}{check_keyphi[0]}")
# 				exit(0)
# 		else:
# 			print(f"{red} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
# 			exit(0)
# 	else:
# 		file_key=open(f"key_N-Tool.txt",'r')
# 		key_cu=file_key.read()
# 		file_key.close()
# 		check_keyphi=checkkey(key_cu)
# 		if check_keyphi==False:print(red+'Sever Key Phí Gặp Lỗi Hãy Dùng Key Free');os.remove('key_N-Tool.txt'); continue 
# 		elif check_keyphi !=False:
# 			try:
# 				name=check_keyphi[0];coun=check_keyphi[1];check=True;keycode=key_cu
# 				print(f'{lam}Key API Chính Xác')
# 				luu(key_cu)
# 				break
# 			except:
# 				if check_keyphi[0]=='Key Không Tồn Tại! Bạn Chắc Chắc Rằng Đã Nhập Đúng Key?':
# 					print(f'{thanh_xau}{luc}Key {vang}{key_cu} {luc}Đã Được Thay Thế Vui Lòng Lấy Key Mới')
# 				else:
# 					print(red+check_keyphi[0])
# 				os.remove('key_N-Tool.txt')
# 				continue 
# 		else:
# 			print(f"{red} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
# 			exit(0)
banner()
name="KhanhNguyen9872"
coun="9999999"
check=True
keycode="KhanhNguyen9872"
if check==True:
	if len(keycode)==3 or len(keycode)==2 or len(keycode)==1:keycode='*'*len(keycode)
	elif len(keycode)==4:keycode=keycode.replace(keycode[0:3],'***')
	elif len(keycode)==5:keycode=keycode.replace(keycode[0:4],'****')
	elif len(keycode)==6:keycode=keycode.replace(keycode[0:5],'*****')
	elif len(keycode)==7:keycode=keycode.replace(keycode[0:5],'*****')
	else:keycode=keycode.replace(keycode[0:len(keycode)-3],'*'*len(keycode[0:len(keycode)-3]))
	print('[1;33m[[1;31mWARNING[1;33m] [1;32mBạn Đang Dùng Key Phí')
	print(thanh_xau+luc+'Người Mua: '+vang+name)
	print(thanh_xau+luc+'Key Code: '+vang+keycode)
	print(thanh_xau+luc+'Số Ngày Còn Lại: '+vang+str(coun)+vang+' Ngày'+red)
	bongoc(14)
print(f"""{hong}┏━━━━━━━━━━━━━━━━━━━━━┓
{hong}┃  {vang}Tool Trao Đổi Sub  {red}┃
{red}┗━━━━━━━━━━━━━━━━━━━━━┛ """)
print(f'{thanh_xau}{luc}Nhập {hong}[{vang}1.1{red}] {luc}Để Chạy Tool Cày Xu TDS Facebook')

chon=input(f'{thanh_xau}{luc}Nhập Số {trang}8===D: {vang}')
try:
	# if chon=='1.1':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/tdsck.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='1.2':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/tdspro5.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='1.3':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/tdstik.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='1.4':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/tdstik2.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='1.5':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/tdsig.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='2.1':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/ttcck.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='2.2':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/ttctik.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='2.3':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/vipig.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.1':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/story.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.2':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/group.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.3':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/follow.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.4':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/setad.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.5':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/regpro5.php',headers=headers,data=bug_duoc_cai_lon).text
	# elif chon=='3.6':
	# 	run=requests.post('https://sever.ngocbansub.com/code_by_ngoc/addfen.php',headers=headers,data=bug_duoc_cai_lon).text
	# else:
	# 	run='print(red+'Lựa Chọn Không Xác Định') '
	run=open('bansaongocv3.2/tool/{}.py'.format(chon),'rb').read()
except FileNotFoundError:
	run='print(red+"Lựa Chọn Không Xác Định") '
except KeyboardInterrupt:
	if not is_connected():
		print(red+'Hãy Kiểm Tra Kết Nối Mạng !!! ')
	else:
		print(red+'Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
	exit()
exec(run)
