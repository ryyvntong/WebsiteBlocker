import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
while True:
    if (8< dt.now().hour<15):
        print("We are currently in productivity hours! :)")
    else:
        print("We are in free time :)")
    time.sleep(5)
