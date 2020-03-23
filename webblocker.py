import time
from datetime import datetime as dt
# hosts_path=r"C:\Windows\System32\drivers\etc"
hosts_path="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
while True:
    if (8< dt.now().hour<17):
        print("We are currently in productivity hours! :)")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    print('hi')
                    # We are remaking the file, so if the line we read doesnt containt
                    # the website of interest, write it to the new line
                    # so when it comes to the websites we wrote to the file before, they wont be save to the new one.
            file.truncate()            
        print("We are in free time :)")
    time.sleep(5)

