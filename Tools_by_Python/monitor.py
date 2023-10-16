import subprocess, time

while True:
    try:
        o=subprocess.check_output("grep V2055A /var/log/nginx/access.log",shell=True).decode('utf-8')
        a=f"{o}\n"
    except:
        a=""
    with open ('zzy.log', 'a') as f:
        f.write(f"{a}")
    time.sleep(86400)
