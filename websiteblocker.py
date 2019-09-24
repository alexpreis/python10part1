import time
from datetime import datetime as dt
#hosts_path = "/etc/hosts"
hosts_path = "hosts"
redirect = "127.0.0.1"
websites_block_list =["www.facebook.com","www.mail.ru","www.ok.ru","facebook.com","mail.ru","ok.ru"]

while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,16 ):
        with open(hosts_path,"r+") as hosts_file:
            content = hosts_file.read()
            for website in websites_block_list:
                if website in content:
                    pass
                else:
                    hosts_file.write(redirect +" "+ website +"\n")
        print("Working hours ....")
        break # only for loop stop in deb
    else:
        with open(hosts_path,"r+") as hosts_file:
            content = hosts_file.readlines()
            hosts_file.seek(0)
            for line in content:
                print(line)
                if not any(website in line for website in websites_block_list):
                    hosts_file.write(line)
            hosts_file.truncate()
        print("Non working hours......")
        break # only for loop stop in deb

    time.sleep(5)

