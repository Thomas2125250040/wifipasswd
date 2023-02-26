import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8',errors='backslashreplace').split("\n")

profiles = [a.split(":")[1][1:-1] for a in data if "All User Profile" in a]

print("{:<30}| {:<}\n{}".format("Wi-Fi Name", "Password","-"*50))

for i in profiles:

    try:

        a = ['netsh','wlan','show','profiles',i,'key=clear']

        results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
        
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        
        try:

            print("{:<30}| {:<}".format(i, results[0]))

        except IndexError:

            print("{:<30}| {:<}".format(i, ""))

    except subprocess.CalledProcessError:
        
        print("Encoding Error Occured")
