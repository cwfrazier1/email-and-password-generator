#!python3

import subprocess
import time
import string
import random
import secrets
import pymysql

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

time = str(time.time())
time = time.replace(".", "") + ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(6))
newEmail = time + "@cwfrazier.com"

write_to_clipboard(newEmail)

generatePassword = input("Generate password? ")

newPassword = ""

if (generatePassword == "y" or generatePassword == "Y"):
	num = 14
	res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
	newPassword = str(res)+"!"  
	write_to_clipboard(newPassword)  

name = input("Name: ")

if name == "":
	name = "(blank)"

host = "192.168.4.45"  
user = "root"       
password = "krvg797C8T!"           
  
database = "cwfrazier"
  
conn  = pymysql.connect(host=host, user=user, password=password, database=database)
cur  = conn.cursor()
query = f"INSERT INTO passwords (emailAddress, password, name) VALUES ('{newEmail}', '{newPassword}', '{name}')"
  
cur.execute(query)
print(f"{cur.rowcount} password saved")
conn.commit()
conn.close()
