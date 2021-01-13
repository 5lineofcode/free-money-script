import http.client
import requests
import random
import string
import sqlite3
from sqlite3 import Error
import sys

from faker import Faker
fake = Faker()

withdraw = False
address = "D87S8xBmWjgy6UWUhBjeRs8cMjpMyXdQe5"

db = sqlite3.connect('database.db')
conn = http.client.HTTPSConnection("dogeminer.fun")

def query(sql):
    cursor = db.cursor()
    res = cursor.execute(sql)
    db.commit()
    return res



def getSession():
    length_of_string = 40

    letters_and_digits = string.ascii_lowercase + string.digits
    random_string = ""

    for _ in range(length_of_string):
        random_string += random.choice(letters_and_digits)
    print(random_string)

    ci_session = "wolven_core_session=" + random_string
    return ci_session


def getAddress():
    URL = "http://localhost:3000/get-target-linked-address"
    r = requests.get(url = URL) 
    data = r.json() 

    address = data['data']
    return address.strip()

def register(username,address):
    session_id = getSession()
    payload = 'user_name='+username+'&email='+username+'%40gmail.com&email_repeat='+username+'%40gmail.com&password=123456&password_repeat=123456&address='+address+'&tos_agree=1&register=Register%2BSecurely'
    headers = {
        'authority': 'dogeminer.fun',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://dogeminer.fun',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://dogeminer.fun/account/register',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': session_id
    }
    conn.request("POST", "/account/register", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    print(res.status)

    if("Your account was successfully created" in str(data)):
        print("Register Success : " + username)
        query("insert into dogeminner_address (username,address,status) values('"+username+"','"+address+"','Pending')")


def withdraw_doge(username):
    session_id = getSession()
    payload = 'user_name='+username+'&password=123456&login=Login%2BSecurely'
    headers = {
        'authority': 'dogeminer.fun',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://dogeminer.fun',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://dogeminer.fun/account/login',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': session_id
    }
    conn.request("POST", "/account/login", payload, headers)
    res = conn.getresponse()
    res.read()


    payload = 'claim=Start%2BAuto%2BFaucet'
    headers = {
    'authority': 'dogeminer.fun',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://dogeminer.fun',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://dogeminer.fun/page/dashboard',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': session_id
    }
    conn.request("POST", "/page/dashboard", payload, headers)
    res = conn.getresponse()
    res.read()


    redirectUrl = res.headers['Location']
    print("RedirectUrl: " + str(redirectUrl))

    payload = ''
    headers = {
    'authority': 'dogeminer.fun',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://dogeminer.fun/page/dashboard',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': session_id
    }
    conn.request("GET", redirectUrl, payload, headers)
    res = conn.getresponse()
    res.read()

    print("Withdraw Complete for User : " + username)

def initialize():
    sql = """ CREATE TABLE IF NOT EXISTS dogeminner_address (
                                        id integer PRIMARY KEY ,
                                    username text,
                                    address text,
                                    status text
                                ); """
    query(sql)

    res = query("select count(*) as count from dogeminner_address")
    rows = res.fetchall()
    data_count = rows[0][0]

    
    min_data_count = 500
    if(data_count < min_data_count):
        for i in range(min_data_count-data_count):
            name = fake.name().split(" ")[1]
            number = '{:03d}'.format(random.randrange(1, 999))
            username = (name + number)

            register(username,address)
    
def do_main_job():
    cursor = db.cursor()

    sql = "select username from dogeminner_address where status = 'Pending' LIMIT 1"
    res = cursor.execute(sql)
    rows = res.fetchall()
    
    if(len(rows)==0):
        sql = "update dogeminner_address set status = 'Pending'"
        res = cursor.execute(sql)
        
        db.commit()
        do_main_job()
        return

    username = rows[0][0]

    sql = "update dogeminner_address set status = 'Completed' where username = '"+username+"'"
    res = cursor.execute(sql)
    db.commit()

    withdraw_doge(username)
    do_main_job()

initialize()
do_main_job()