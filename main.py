import sys
import requests
message=""
for x in sys.argv[1:]:
    message+=x+" "

chat_id="<chat_id>"
TOKEN="<TOKEN>"
url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url).json() # this sends the message
