import requests

TOKEN = '228606601:AAGltjoUHRr-wsk4vtFefI58dqs8WXImHfk'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN

def sendMsg(msg = "fuck"):
    data = {'chat_id': '-128786812', 'text': msg}
    url = BASE_URL + '/sendMessage'
    r = requests.post(url, data)
    print(r.text)

def getMe():
    url = BASE_URL + '/getMe'
    print(url)
    r = requests.get(url)
    print(r.text)

# {"ok":true,"result":[{"update_id":449110854,
# "message":{"message_id":2,"from":{"id":183518555,"first_name":"Loi","last_name":"Tran Duc","username":"loitd"},"chat":{"id":-128786812,"title":"Massive group","type":"group"},"date":1463638841,"new_chat_participant":{"id":228606601,"first_name":"dollx","username":"dollx_bot"},"new_chat_member":{"id":228606601,"first_name":"dollx","username":"dollx_bot"}}},{"update_id":449110855,
# "message":{"message_id":3,"from":{"id":183518555,"first_name":"Loi","last_name":"Tran Duc","username":"loitd"},"chat":{"id":183518555,"first_name":"Loi","last_name":"Tran Duc","username":"loitd","type":"private"},"date":1463638892,"text":"Fucj"}}]}
def getUpdate():
    url = BASE_URL + '/getUpdates'
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':

    getMe()
    getUpdate()
    sendMsg("Yes, fuck")