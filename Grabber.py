from datetime import datetime
import subprocess
  
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) 
  
data = meta_data.decode('utf-8', errors ="backslashreplace") 

data = data.split('\n') 

profiles = [] 

for i in data: 
    if "All User Profile" in i : 
        i = i.split(":") 
        i = i[1] 
        i = i[1:-1] 
        profiles.append(i) 
          
now = datetime.now()
 
print("now =", now)
dt = now.strftime("%d/%m/%Y %H:%M:%S")

with open("Grab.out","a+") as f:
    f.write('Grabs as of : '+dt+'\n')
    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    f.write("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    f.write('\n')
    print("----------------------------------------------") 
    f.write("----------------------------------------------")
    f.write('\n')
       
    for i in profiles: 
        try: 
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])
            results = results.decode('utf-8', errors ="backslashreplace") 
            results = results.split('\n') 
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try: 
                print("{:<30}| {:<}".format(i, results[0]))
                f.write("{:<30}| {:<}".format(i, results[0]))
                f.write('\n')
            except IndexError: 
                print("{:<30}| {:<}".format(i, ""))
                f.write("{:<30}| {:<}".format(i, ""))
                f.write('\n')
              
        except subprocess.CalledProcessError: 
            print("Encoding Error Occured") 
    f.close()
