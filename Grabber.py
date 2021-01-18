from datetime import datetime
import subprocess
  

now = datetime.now()
 
print("now =", now)
dt = now.strftime("%d/%m/%Y %H:%M:%S")

with open("Grab.out","a+") as f:
    
    f.write('Grabs of : '+dt+'\n')

    f.write("{:<30}| {:<}\n".format("Wi-Fi Name", "Password")) 
    f.write("----------------------------------------------\n") 

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        
        try:
            info = "{:<30}| {:<}".format(i, results[0])
        except IndexError:
            info = "{:<30}| {:<}".format(i, "")

        f.write(info+'\n')
        print(info)
    
    f.close()
