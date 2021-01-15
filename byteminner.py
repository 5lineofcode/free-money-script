import http.client
import requests
import random
import string
import threading
import time
import ssl
from bs4 import BeautifulSoup
from datetime import datetime

withdraw = True
getLoggedinAddress = True
withdrawCompletely = False
unregisteredLogin = False

def getSession():
    length_of_string = 40

    letters_and_digits = string.ascii_lowercase + string.digits
    random_string = ""

    for _ in range(length_of_string):
        random_string += random.choice(letters_and_digits)
    print(random_string)

    ci_session = "ci_session=" + random_string
    return ci_session


def getAddress():
    if(unregisteredLogin):
        URL = "http://20.198.178.250:3000/get-single-address"
    elif(withdrawCompletely):
        URL = "http://20.198.178.250:3000/linked-address/Withdraw"
    elif(getLoggedinAddress == True):
        URL = "http://20.198.178.250:3000/linked-address/LoggedIn"
    else:
        URL = "http://20.198.178.250:3000/linked-address/Pending"

    r = requests.get(url = URL) 
    data = r.json() 

    if(data['message']=="SUCCESS"):
        address = data['data']
        return address.strip()
    else:
        return ""


def main(args):
    while(True):
        f = open("status.txt", "r")
        if(f.read().strip()=="0"):
            f.close()
            break
        f.close()

        start_at = datetime.now()
        address = getAddress()
        if(not address):
            print("No Data!")
            break

        ci_session = getSession()
        print("address: "+address)
        print("ci_session: "+ci_session)
        print("----------------")

        conn = http.client.HTTPSConnection("byteminer.live")
        # conn = http.client.HTTPSConnection("byteminer.live",  context = ssl._create_unverified_context())
        payload = "username="+address+"&password=123456&reference_user_id="
        headers = {
            'authority': 'byteminer.live',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://byteminer.live',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://byteminer.live/z',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': ci_session
        }
        conn.request("POST", "/ajax_auth", payload, headers)
        res = conn.getresponse()
        data = res.read()

        print(data)

        if('success' in str(data)):
            print(".")
        elif('Duplicate' in str(data)):
            URL = "http://20.198.178.250:3000/update-address/"+address+"/BadAddress"
            requests.get(url = URL) 
            print("Duplicate Error, dont use this address again")
            continue
        else:
            URL = "http://20.198.178.250:3000/update-address/"+address+"/LoginFailed"
            requests.get(url = URL) 
            print("Login Failed")
            continue

        URL = "http://20.198.178.250:3000/update-address/"+address+"/LoggedIn"
        requests.get(url = URL) 

        print("Login Success")
        rememberCode = res.headers["Set-Cookie"].split(";")[0]

        if(withdraw==False):
            print("----------------")
            continue

        

        payload = ''
        headers = {
            'authority': 'byteminer.live',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://byteminer.live/dashboard',
            'accept-language': 'en-US,en;q=0.9',
             'cookie': rememberCode + "; " + ci_session
        }
        conn.request("GET", "/withdrawal", payload, headers)
        res = conn.getresponse()
        data = res.read()
        html = data.decode("utf-8")

        soup = BeautifulSoup(html, 'html.parser')


        current_user_address = "NO ADDRESS"
        for li in soup.select('#transfer input'):
            current_user_address = li.get("value")

        for li in soup.select('#transfer h1'):
            balance = li.text.split(":")[1].strip()
        
            payload = 'amount=' + balance
            headers = {
                'authority': 'byteminer.live',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://byteminer.live',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://byteminer.live/withdrawal',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': rememberCode + "; " + ci_session
            }
            conn.request("POST", "/withdrawal", payload, headers)
            res = conn.getresponse()
            data = res.read()

            if(withdrawCompletely):
                URL = "http://20.198.178.250:3000/update-address/"+address+"/Complete"
                requests.get(url = URL) 
            else:
                URL = "http://20.198.178.250:3000/update-address/"+address+"/Withdraw"
                requests.get(url = URL) 
            
            
            print("---")
            print("Address : " + address)
            print("Current User : " + current_user_address)
            print("Valid : " + str(address == current_user_address))
            print("Withdraw Success : " + balance)
            print("---")

            end_at = datetime.now()

            diff = end_at- start_at
            print("Finish in " + (str(diff.microseconds/1000)) + "ms")
            print("################")

def run_main_thread(args):
    try:
        main(args)
    except:
        exit()

f = open("status.txt", "w")
f.write("1")
f.close()
    
threadCount = 1
if(threadCount>1):
    for i in range(threadCount):
        t = threading.Thread(target=main, args=(i,))
        t.start()   
else:
    main(0)