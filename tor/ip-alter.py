from stem import Signal
from stem.control import Controller
import requests
import json
import random
import time
import _thread
#pip install pysocks
#tor --controlport 9051

with open("user-agents.txt","r") as f:
	list_user_agents=f.readlines()
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

def switchIP():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
	print("ip changed")
	
def random_ua():
	ua=random.choice(list_user_agents).replace("\n","")
	#print(ua)
	return ua
def req_via_tor():
    resp = requests.get("https://example.com/archives/13/", proxies=proxies,headers={"User-Agent":random_ua()})
    if resp.status_code==200:
        #print(resp.content.decode("utf-8"))
        print(resp.status_code)
    else:
	    print(resp.status_code)
    return True

t1=time.time()
num_thread=0
while True:
    if time.time()-t1>30:
        switchIP()
        t1=time.time()
	      
    if num_thread<10:
        x_event=_thread.start_new_thread(req_via_tor, ())
    else:
        time.sleep(1)
        print(num_thread)

    
