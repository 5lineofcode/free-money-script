import http.client

userList = ["zaaww98888","RaumkriegUH66939","BresnerG146703","festarmeytj97268","TeclaiQC52602","SitsgeotsGG56804","diazsanmiguelzU88829","TeoriD437405","Hogerwv34031","nowjonfusi231296","mwysairo140881","EmpomoGetzC71043","borbolhY022839","pitadasuU67835","espinlonEI66169","estensorexg80285","stellababy841x68555","kayemgee9V86212","javkaFw24871","annsameWD74174","glietiqW76581","singopationPe80789","supurarz813003","laksesgrao968717","tabiriwaT067061","naturalteas1u60955","yearlingM980801","cocleaD019224","opipseKansapeqn30566","aubamRK53285","MymnMynccoectc934594","ngilishoHp77977","nicoguateXq90532","reb1eg2y4k80734","Lockomaaw21404","bagukSp14211","hmyzemRA97612","akaitauY33804","chuspeuC78999","usclantasNN93445","skolaMS73032","Castij035349","npjbass5vO41955","rubrica7N84611","flipiGZ10255","mineralogpx69389","plejadurQ97803","wa3tr4yc73971","serwerowyPT98948","kio3558937","platimotM61031","transalveiY86179","autisthh58425","mrboingy1X17352","tlisew919076","nikawlrx65658","manevriraIU71319","MeghnagiVA61614","slambytivf54289","JacacciaTp12997","aufu0216WN91778","buiqrkpcajVC59419","CirlunurltO15251","ringedoniontO84669","asumo8r22716","smouserGJ19758","thedmannYe81386","inesiapilsHam6K22218","okulima8o93236","wihajsterKz33354","criscologyTz35381","zatrpaoMB45849","nunnibixepea280812","Nescisw433076","leschefsonqG51155","doyoung123GO94555","capricornianQG96348","auserejaneA14387","meisok7y29164","thxbobuJ76248","beenoudzv82419","DidenheimLE50356","kurugoFY49013","somovkLJ38859","ryla1Y662610","gogreengirlc763366","Mavrinovlm49537","fsbi768395","screatallro20072","ACASXl49339","metretaKi32449","pyskIE36205","Miodowiczd754182","sinopsisvital9e91207","ZipeteLz27876","MinottodV78632","apreciisPA85987","spitanrY88776","STYPESNE8H36230","nawuphih550990"]
currentIndex = 1
for username in userList:
  password="123456"
  wallet = "D87S8xBmWjgy6UWUhBjeRs8cMjpMyXdQe5"

  conn = http.client.HTTPSConnection("dogeminer.fun")
  payload = "user_name="+username+"&email="+username+"%40gmail.com&email_repeat="+username+"%40gmail.com&password=123456&password_repeat=123456&address="+wallet+"&tos_agree=1&register=Register%2BSecurely"

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
    'cookie': 'wolven_core_session=2adfa5c1e7317caf49b498d198faab35'
  }
  conn.request("POST", "/account/register", payload, headers)
  res = conn.getresponse()
  data = res.read()

  print(username + " has been registered ("+str(currentIndex)+"/"+str(len(userList))+")")
  
  print(str(res.status))
  currentIndex+=1