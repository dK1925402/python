import requests

token = '#Enter token'  
id = '#Enter Chat_id'   
text = input('Enter the Message for bot : ') #Enter text for send the bot

#format of telegram bot api = https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}

#requests.get() used for send the request to website
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
