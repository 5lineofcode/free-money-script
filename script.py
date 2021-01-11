#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium import webdriver
from fake_useragent import UserAgent

import time
import uuid 
from random_username.generate import generate_username
import csv 
import os
import threading
import requests

def runInstance(instance):
    chrome_driver = os.environ.get("CHROMEDRIVER_PATH")
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox') 

    driver = webdriver.Chrome(
        executable_path=chrome_driver, options=options)
    driver.get("https://dogeminer.fun/")

    driver.execute_script("""
		//to stop heroku from idle
		/*
        setInterval(function(){
			$.get("https://ocr-callback.herokuapp.com/index.php?url=https://dogeminner.herokuapp.com/");
		},10000);
		*/
        //---- hehe


        $("body").html("");
        var usernameList = ["vokeSqueemoWJ73501","RaumkriegUH66939","BresnerG146703","festarmeytj97268","TeclaiQC52602","SitsgeotsGG56804","diazsanmiguelzU88829","TeoriD437405","Hogerwv34031","nowjonfusi231296","mwysairo140881","EmpomoGetzC71043","borbolhY022839","pitadasuU67835","espinlonEI66169","estensorexg80285","stellababy841x68555","kayemgee9V86212","javkaFw24871","annsameWD74174","glietiqW76581","singopationPe80789","supurarz813003","laksesgrao968717","tabiriwaT067061","naturalteas1u60955","yearlingM980801","cocleaD019224","opipseKansapeqn30566","aubamRK53285","MymnMynccoectc934594","ngilishoHp77977","nicoguateXq90532","reb1eg2y4k80734","Lockomaaw21404","bagukSp14211","hmyzemRA97612","akaitauY33804","chuspeuC78999","usclantasNN93445","skolaMS73032","Castij035349","npjbass5vO41955","rubrica7N84611","flipiGZ10255","mineralogpx69389","plejadurQ97803","wa3tr4yc73971","serwerowyPT98948","kio3558937","platimotM61031","transalveiY86179","autisthh58425","mrboingy1X17352","tlisew919076","nikawlrx65658","manevriraIU71319","MeghnagiVA61614","slambytivf54289","JacacciaTp12997","aufu0216WN91778","buiqrkpcajVC59419","CirlunurltO15251","ringedoniontO84669","asumo8r22716","smouserGJ19758","thedmannYe81386","inesiapilsHam6K22218","okulima8o93236","wihajsterKz33354","criscologyTz35381","zatrpaoMB45849","nunnibixepea280812","Nescisw433076","leschefsonqG51155","doyoung123GO94555","capricornianQG96348","auserejaneA14387","meisok7y29164","thxbobuJ76248","beenoudzv82419","DidenheimLE50356","kurugoFY49013","somovkLJ38859","ryla1Y662610","gogreengirlc763366","Mavrinovlm49537","fsbi768395","screatallro20072","ACASXl49339","metretaKi32449","pyskIE36205","Miodowiczd754182","sinopsisvital9e91207","ZipeteLz27876","MinottodV78632","apreciisPA85987","spitanrY88776","STYPESNE8H36230","nawuphih550990"];
        
        async function main() {
            $("body").prepend(` 
                <div style="padding: 20px 20px;position: fixed;bottom:0;left: 0;right: 0;background: black;z-index: 99999999;">
                    <button class='btn btn-success' id='generateBtn'>Generate Referreal</button>
                </div> 
            `);


            async function runRegisterReferealScript() {
                var username = usernameList[Math.floor(Math.random() * usernameList.length-1)] + (Math.floor(Math.random() * 900));

                /*
                await fetch("https://dogeminer.fun/", {
                    "headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-language": "en-US,en;q=0.9",
                        "cache-control": "max-age=0",
                        "upgrade-insecure-requests": "1"
                    },
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "body": null, 
                    "method": "GET",
                    "mode": "cors",
                    "credentials": "include" 
                });
                */

                await fetch("https://dogeminer.fun/account/login/", {
                    "headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-language": "en-US,en;q=0.9",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1"
                    },
                    "referrer": "https://dogeminer.fun/account/login/",
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "body": `user_name=${username}&password=123456&login=Login+Securely`,
                    "method": "POST",
                    "mode": "cors",
                    "credentials": "include"
                });

                await fetch("https://dogeminer.fun/page/dashboard", {
                    "headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-language": "en-US,en;q=0.9",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "upgrade-insecure-requests": "1"
                    },
                    "referrer": "https://dogeminer.fun/page/dashboard",
                    "referrerPolicy": "no-referrer-when-downgrade",
                    "body": "claim=Start+Auto+Faucet",
                    "method": "POST",
                    "mode": "cors",
                    "credentials": "include"
                });

                console.log(`${username} done!`);
            }

            while(true) {
                await runRegisterReferealScript(); 
            }
        }

        main();
        """)
    
    w = WebDriverWait(driver, 5000000000)
    w.until(EC.presence_of_element_located((By.ID,"complete")))


def stopIdle():
    while(True):
        requests.get(url = "https://dogeminner.herokuapp.com/")
        time.sleep(10)

# Configuration
instanceCount = 10
# # --------------

# index = 0
# for i in range(instanceCount):
# 	runInstance(i)
# runInstance(1)

threading.Thread(target=stopIdle).start()

for i in range(instanceCount):
    threading.Thread(target=runInstance, args=(i,)).start()
        