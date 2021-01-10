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

def runInstance(instance):
    chrome_driver = os.environ.get("GOOGLE_CHROME_BIN")
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(
        executable_path=chrome_driver, options=options)
    driver.get("https://dogeminer.fun/")

    driver.execute_script("""

        $("body").html("");
        var usernameList = ["vokeSqueemoWJ","RaumkriegUH","BresnerG1","festarmeytj","TeclaiQC","SitsgeotsGG","diazsanmiguelzU","TeoriD4","Hogerwv","nowjonfusi2","mwysairo1","EmpomoGetzC","borbolhY0","pitadasuU","espinlonEI","estensorexg","stellababy841x","kayemgee9V","javkaFw","annsameWD","glietiqW","singopationPe","supurarz8","laksesgrao9","tabiriwaT0","naturalteas1u","yearlingM9","cocleaD0","opipseKansapeqn","aubamRK","MymnMynccoectc9","ngilishoHp","nicoguateXq","reb1eg2y4k","Lockomaaw","bagukSp","hmyzemRA","akaitauY","chuspeuC","usclantasNN","skolaMS","Castij0","npjbass5vO","rubrica7N","flipiGZ","mineralogpx","plejadurQ","wa3tr4yc","serwerowyPT","kio35","platimotM","transalveiY","autisthh","mrboingy1X","tlisew9","nikawlrx","manevriraIU","MeghnagiVA","slambytivf","JacacciaTp","aufu0216WN","buiqrkpcajVC","CirlunurltO","ringedoniontO","asumo8r","smouserGJ","thedmannYe","inesiapilsHam6K","okulima8o","wihajsterKz","criscologyTz","zatrpaoMB","nunnibixepea2","Nescisw4","leschefsonqG","doyoung123GO","capricornianQG","auserejaneA","meisok7y","thxbobuJ","beenoudzv","DidenheimLE","kurugoFY","somovkLJ","ryla1Y6","gogreengirlc7","Mavrinovlm","fsbi7","screatallro","ACASXl","metretaKi","pyskIE","Miodowiczd7","sinopsisvital9e","ZipeteLz","MinottodV","apreciisPA","spitanrY","STYPESNE8H","nawuphih5","AlbanMA","garsonjerVl","ringginHg","papanoviaNG","abastarsdA","adfaeddodtk","leviicorpusM8","cistronht","rabotomLr","BiotidoroHk","Vaksljemaxo","limburgerUT","trotylowyWg","behindzX","KaimierasdU","briulesQ7","coeneurepsyncAL","abupheli0U","sinangihT","fokusimaub","Matinatof2","clameneerrobeIf","margarita69N7","BronkpD","makrolpK","bajel4A","pobmanUR","MagamponPT","obveznik10","HeimvideoAF","a2l1xR1","ostajemgn","purest5J","buckeln8j","InsulauttencebE","tripolinosg","morteffineeJB","pirenoWT","RadprofijG","kolovumh","teoromera0l","MeVvr","pensinis9O","cribynJV","flisol5n","aimetzqU","harawanL5","otpratiosS","orrelisteFT","Valdrappaec","ZahnachsenF","Rohrpostb3","eissartcM","kazne47","organiskZd","zuhausenD1","DidenheimaP","Infuss1","ngamahorarM","MiltestibleYw","zastavinY","neigtenYK","lilgiangerm4","kalansayt5","mixfabricsVp","masasabiSI","talaccorotL","odvojaksL","hayshePz","cesarAk","mauharsVp","naumastAf","ZabrekveBt","blikkenjK","katatymiaEM","creolebarbieIV","sceadgU","strariusZy","centrafrique1ct","RestantegV","imarpiddizaryuV","stvarniciK","KarkenDx","putrejuneWr","DejmlBG","tektoblogxT","Indiane7y","tidoToicaitp4","jdelpino4g","nimamnD","conhatgess3","ony1old8M","granadinoKs","darkparnZh","gluiperdBm","mensonTQ","1ta1fe4Ov","stalnijiZK","marnaneloj","PuissaLN","gedosoOtsnE","alimradhivr","luffablechikg1","MindelliKz","giovacapposG","openofficeDL","gugginnu","corrosivazk","1bioYO","Eidelpes0J","2asze1me7Z","creamsicle16cb","ToullyblookyR","orhanovaPA","contradityh","shadikrazile","migrasjon2p","wesleyanaKV","Jetahywhefer4","dosledneZ3","gotskeNA","hie4lsU6","picratoFV","colissatzKa","trupova1l","CalabiOi","PlanicaXg","utfattigzw","vybrnkatv0","librealma34","infoliniapD","melkeveiRX","salonsemploizr","BadulliI4","drogada2k","dadlosseteemyhr","vrygaanFr","thetimepieceFQ","uteknemXu","dalsisyvattOn","robotuxq","unamihoogmachbw","Kasuarineny","reliablebluezM","freudovuG6","jagole8410g","mechanikakH","izdimilaV5","Dembio1A","xxx17074z","maucueitsb8","tidoToicaitww","utadhaniuZ","autadajv","wokubophaUL","deledydd2u","SpoovaMaype2H","admonitorCj","bakpoedergW","meanachPW","tebraouiMF","Ralealf9","smiley070vB","innortEmereqa","arapomGg","upornikov7t","localizaryW","aojiroiemura2h","ScoffoQ8","srpnjiRC","butadersg","finstueO0","ponygal83Bc","Benliroiy","patisonol","hymbiliWI","grychlydOe","kalendamsw","weggeloktJq","videoshaloDi","zo1naFy","zatrpaoGS","MartietteawarqF","exsudava0r","Karpiuk7k","clavillerE8","preohydratordpP","TedVurermge","KispatakhP","vestriseak","amoflatvb","SchmedeyP","pupsi6z","wa3tr4Ab","darkvonhacktv","durbanietdp","poklopitiUX","ManjalymH","seawovlerineYg","sapphirelleyn","KartumomYo","targedauMA","scairdeyH","lelhetaC","wagxilao9","yhendymendezfn","uklonjenuVB","poemlP","hercynidyDX","gywain9O","skvetneC4","zgoiwszy3U","camoceyi","flunkert8A","ZephyrusLk","nheneuo0d","BerroneKA","seshoekOU","PoitonHC","kshUX","TakgoavaFoelarQ","MinnilloYx","deilithe1v","ruspandonL","justplanoldmeyf","gloeiovenk4","iznalaskeIf","ModernTG","kimme012I3","jenekestikd","mrwii911Ba","maltami7o","WHGtS","tyson19486l","BenseddikI1","aggieguy555pZ","saumastreOM","boowapandok4V","emilyascherrS","alguesezZ","tanpopo1234y","zivuleka8T","BrnomP1","RuwenzoriHE","zutretenRn","tsennyipagp","drelaryZ","viossatdenis4Y","Salandinir7","sortentsZZ","FloraCrymbomaoD","grangurAA","kweyesine0q","glommowbamigoZ3","sunitskomoN","mahatma7x","smuglararZQ","brijunskeqT","Diarrhoeahs","gogovutM","WilmsM7","rationate1j","dontherugv6","zi2n1a2nMS","skugge4P","ftblldrk307I","isaziwawn","kragtigbs","remocantaFT","ubroje25","krietrn","dansbro5d","agafetatMZ","lomilkamaKv","umslagti","berwang09","cribynhQ","VrholamirM","tenituraXA","kron17HS","boekerigi7","ooo333booboo1pe","latigazoNl","baentq4","ilizwe7x","tigerangel225l5","blackdeath66744","inegalatZh","Smutka19","noodles310KT","barbolhaFI","WayslesirlsefGt","gilaclaPh","kamesinupC","o4sj2NM","glaisleunQe","betonimDk","animistDl","maddeych0B","draait3Q","celebravaPg","dovleciFL","geliefertPs","angelblancoc1","proclive3g","syfrdeniDW","arcaneagendabk","flacoloco77sh","hotdawg179sh","n5ob2iGo","darkhiusakisc","Garatoniuu","yumikouriuf","muythaicadetAE","itatakdaf5","flocio4v","Tanburac","DinarYr","kri1tixx","ZahneisenBr","en1osztvZ","vestriseoX","li2ajYe","ChifentiWO","boobiesmurf93","kron179u","Gattnerp4","algerisch2V","JilleenBj","wolawopq","FichessaOb","skogRk","lauragirlox3MC","nobelovaS2","Lickispbaisee4o","hwphilsaOG","evorrymoofsdz","kusaZ3","akacijomYl","stukgaan1N","helbredI0","BesiegteQb","terenskomPn","swttest75iK","putagPo","evemarinelaZH","sioF5","ekken0026mv","dolbemBi","lilgujubabiezq","crawciau71","BarraniwK","eksitusbi","tonikiDt","banskog7U","marzantehH","fighterflyjb","Katarczykz5","aprendaMa","NemunasVB","taurnagueptexHs","HadramautRe","horizonusaaE","yatholwarC","odzivatiWT","Matozov4Q","fonvisaFloallnx","xokasiaoxg3","jenki2I","BolziccoeX","ArnoudYr","kazivaoQO","ModernqH","lilshyonexoxFn","macloigjp","tisakhaleqA","interdictumZM","crazygirl26SP","aphoniaZv","KirchfrauKQ","kimgodV1","Abfragez2","Leubetha2t","rendezvous060q","Samsunqu","mynyddaE3","drillerKA","sionis7X","BoniAccobeCen25","CeforomN","pracanty5","razbesneluf","reneThync9K","placentiEY","VeivephochexT","f3reicIP","xidolxlytsxEj","OrtnekaVW","ErrogRowskago3s","firnistPa","sectorizajt","lwendlur9","volapuksfr","sienta7J","ciemniaOi","in2csorQl","aibalwa1s","forleneGn","brostilhaTI","Attaptisarifewc","xikowetokb","simcebelezH","affichesiz","lamourzikaK","iridij35","chircinduta","skyriklisP6","ngholuroqa","fotoblogariosL","MemhoallogmepNV","OfsjochtMH","Kosowymkc","cynthiahcohen5x","leftcleftdoXe","lauraders44","hosterwareha","ThebaultQC","OrdermemodurBTm","regretlay32uu","manghulaKu","rubricae7","InjeleMeessWX","infintymatssy","culinaLU","Fiorilli1N","altspeler9m","retulitST","a1n2a1logYY","szejkl5","MonghadiNw","iglomjL","trencaderXh","eissartaD","sitwaqF","provisoirjj","Savoipk","umvefjarJ","skestyFate3","Draitacit89","photognome7o","EggmannK4","maddeychKv","atauondoa1O","strategyfirstw6","ZvodenkinIO","mellyj2f","fusquenllayf","poetssterCZ","sfinteiLx","QuonSodamum4W","llamadoradaxG","mokapeloeL","modernizi5Z","SkavlanQK","calvaAt","peruvianiteP","s3xyd3viltg","textileindienka","Buchleser2v","DragarjevPo","ravnicuEE","teenklagtI","babydawl99994N","laochraHS","ChuchNeetvv","regrederqV","apollonixr","potassis5B","Fromm5o","Ovettestooneert","Pedrai9Q","ceekhum","rezistencRs","RibepintedexA","nabeira7g","Rucianegofg","hjustonarc","RimaEmaibleon","lecameleonF8","dansbrolP","muilceann9E","tinacs1288iF","egon010mf","pazinski5e","romsanNg","gyfresueU","a2gy1a2coA","anemicaszX","ahpoorG","moubyambica9s","tamiepilaeq","pcoyoteiconsR6","esfolhetzlC","nm200191","hipoteek2g","hop3l355dr3m5xa","sambondumav","minnesangek","activitatZt","anomali3tf","qracelygK","zaprljano1P","ingedroogKh","ZanacoliYe","RirlneincEp","ImpostLj","HarzungenQX","xdragon8o8xAc","nokuzondabi","barimlM","pozavideT6","Hatinhany0w","cuenkaiL","KilzieqG","AbbotvG","kadiriwaPs","icontasticx3tg","bigbro818Te","dobyitoKq","chiman0529Um","nacepitnellsB","Hansatida4O","brezovina3N","de5iscsU","oriesstenuehJ","Yanick18","apogamiasVG","meloiseauwy","annikan19GI","fynoryz","aganissisGY","excavavasY0","buttercupbritxW","TartraimutsKR","sereysethyRV","nuogino16","elegiskbk","hartuinduWs","revienora2M","JohanesRR","alviragexH","promalja5N","gladis6S","BergeggigM","SemnjW","toftirnarWA","attutatoZt","tsennyipam7","tresborimxL","magbuo4A","broeinestpc","Barlettosa","ffablonWm","nachobronchoRq","obplezaliu","assenyatu3","danilobcmSi","metenjem4L","rhuglaMw","dejunantaRe","obalu9D","jamAdmimitv","b4e1neAK","AnnormoppothecM","wlpetersVF","kuneleug","bustsqE","kbgatoSA","xperimentsy8","neddirfq","Rosheim1Y","jenki1o","concediatfH","AninaFapsen","S4SPWQY","arboreTi","orrontatXx","carumIW","crazyhitloverJB","leppefiskIx","ewestpX","skabbut9l","BerroneFI","4lopQI","fegurstOo","armleggurNr","notoriousbkcbI","Artusatowe","Folgebyteou","asianpugboyoE","jrchy18gN","IdedeBizdiokypL","pletenimavO","vivialdereteWx","pquenoaR","xxxxjessxli","mauharsEO","TorpeyBM","bootybrownA6","Parkgrund0j","Kargadeur1u","SaseRemiadekd","alallarg1k","FicarellimH","lovelovelovehTu","cowspot924sh","enkundlaW7","KierulfvV","hystredauXd","temptatiuCU","batikowyiZ","laders08","Giarlotto1h","stormhoekjC","Viticchiens","ninidu59300nU","kt3aanII","kinundu9a","re5asc2Jx","palartzskiDn","choofsthago8O","rtxmz","hakikisho3Z","Arabiska6b","PicofaradFk","idzieV6","ysgefnwchFl","mafonjarn","gemelluna7w","isishoET","thehsumakertu","ThizTrerreomacG","taunuswE","rotweissMj","welovedemboizIZ","loufaS2","laydeeflib8","Jamajkagc","loftbelgrN","udubinomws","EdiggidlyKi","radacaigh0U","caitighy3","kolkux0","sexyspiputsrw","B4PSO","panauhinZz","pojmovnomnu","attinico6E","bevalligqi","japodski99","HinsMoism7e","JunktimEK","AddedeCahfJ","pelleauUT","ubacio3J","se2r1elvkS","ph5or1iz1k","waliitwawU","bliss330Up","esclatesPo","ZeffiriniKm","ChielpoR2","smilgotaser","szmogjaEe","laviejausinaTn","camorrze1J","avlangYR","mypinkhearsewg","rd3uPK","FougnierR3","prsta5n","HoidoEquadaMS","horfast41","gorasanferminqZ","ellirycoP","gasaunIp","fasilicasMt","exaurintxt","stormcatchereA","graczkaWw","papanoviay3","imannajlayy","ZeniNeannerUB","bicokokNI","uu2mimhg","jhenny5490TL","eusqueraov","marial23i","mataukQX","blissful25","chwyrn65","sciestechadayKQ","kelibang43","prievesarDy","jasonb122cm","gymnastbabe02HX","francalataPD","frekuensiJX","uslikanicr","Uruguaykao9","h1x7F","sokukatFn","caigeskd","veltolo9T","gobeludoXL","rebelde1971GY","Chiozzini5h","HepadHK","vkubikfB","alcanceNX","secessionX0","Grzinaym","aintnothang94","garfaglauNX","natacionsalta3o","millilagaBd","wdennaiFe","Tedlagw","ethischerP8","OrganartGt","odaslatayC","serthcZ","revendirD3","kubekelwaqr","kerusakan1y","JabpraibeUe","drauginnjM","ichihachitw","Mezzenarm","nyzgaVn","Bunaciupr","embohavasSR","contara4T","Quemermsent5X","PipestoneCG","mexicasian90At","Calvetti7Z","AbalawulilD","GladiottiUD","LogkR","mrenamaLH","dictadurapp","rendeltetCw","ImpallariVj","Tolstojo9F","SenkaDA","danzaconlobosru","ropavejeroCE","SpeepdwectnatHW","camtarnTB","Zuurbier8W","zavrtegavh","dokuekish","vespatiqueOr","irvinianofd","KEEQDK","caitighSZ","n3rfeHp","lupanarsVX","maisonimage4e","cheaphotelsuk2u","1imdTn","sjamanEh","VerAstersekawRQ","ovijeRG","do1p2l6t","gipperella8m","darkshifter27y1","coluziuneKi","PogelTP","brecsCn","xolindz08xop2","bielakXT","nicoblogPI","ritaredshoesq5","esmerivi73","Scunniptthyncu2","orelfungoIc","dobrosavajW","prislovSS","minusieusbj","licunglW","chillseoulja3I","BopeinhireeiG","sudanerFz","marseille2008Gp","miltonvHH","camoce6k","klabatsPC","mapapalaMt","garfaglVa","clgUc","Elbisbachq7","dudewtfurafgtW9","moraludasZg","gredinahV4","gestresF8","overthrewpS","fjandmennxW","bobsleightT","bodiguisPT","ltreyes36","snarpirLD","Safonova2S","vechiiKo","NebenfachkB","mytholiyh","Ammoucheya","pearsally1Ox","Khzibamd","parallax80iB","komoojduNZ","caskefausydayQz","lejosdeberlinbO","elwqcs2w","blizanac0a","abrarrild2m","Laufzeugmg","sperrtaqz","knegenzk","mavermardu","rachellehcarhw","c2sailboardssf","CymnphephotheVr","oragopourcicail","embelmexcaddyyJ","avaizImitTo","mrwii911YK","durfdeRS","engemantYI","Longykamzh","hustalhavQ","kilimaninf","siudingggb2","chromomersk","n2k1obhG","srannaightg","joyceyongnX","athena54rV","brwnsuggah4","markuskaisc","emilyfsX4","eclipce7eg","manimortezx","uitdamp2p","filo2cemZR","arginnideRs","r066HF","ranfluare4u","ispaljujtE","Digiustoic","atkampuski","Toullyblookfw","Opporneemebra1J","hd6eogon","missclicaC","HorgandontigoJF","glauxaniaL8","SifulayE","Xiamenyj","nitaqR","teikns7","margarita69oh","EmixTinnick80","marcy2008YV","orphanofgodTP","lutrijebK","drzewiej0D","fregabanf0","apelacijeyw","cambrianoeH","TeerwestY5k","valentickq8O","rev6675p","hizzdottrQ7","flaggsinsQT","SypepaydayrarUM","bathiadaukN","isaziwadg","es1c2i2fG","courtrife088L","enrinxava9h","overlapB5","cagsPg","gynhyrfau3C","gogenacy","boutarh","trimovatje","mixatgesPU"];
        
        async function main() {
            $("body").prepend(` 
                <div style="padding: 20px 20px;position: fixed;bottom:0;left: 0;right: 0;background: black;z-index: 99999999;">
                    <button class='btn btn-success' id='generateBtn'>Generate Referreal</button>
                </div> 
            `);


            async function runRegisterReferealScript() {
                var username = usernameList[Math.floor(Math.random() * usernameList.length-1)] + (Math.floor(Math.random() * 900));

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

                await fetch("https://dogeminer.fun/account/register", {
                    "headers": {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-language": "en-US,en;q=0.9",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "upgrade-insecure-requests": "1"
                    },
                    "referrer": "https://dogeminer.fun/account/register",
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "body": `user_name=${username}&email=${username}%40gmail.com&email_repeat=${username}%40gmail.com&password=123456&password_repeat=123456&address=D87S8xBmWjgy6UWUhBjeRs8cMjpMyXdQe5&tos_agree=1&register=Register+Securely`,
                    "method": "POST",
                    "mode": "cors",
                    "credentials": "include"
                });

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


# Configuration
instanceCount = 1
# --------------

index = 0
for i in range(instanceCount):
	runInstance(i)