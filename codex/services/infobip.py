import http.client
import json

BASE_URL = "yr8e3d.api.infobip.com"
API_KEY = "App 3ab9363359b48d88f1b7b2b11cd92f76-137f1861-a3bd-483b-b7de-902f788c8f49"

DEFAULT_HEADERS = {
    'Authorization': 'App 3ab9363359b48d88f1b7b2b11cd92f76-137f1861-a3bd-483b-b7de-902f788c8f49',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

APPLICATION_ID_2FA = 'AECBD257FCD6BDD5BFA8BE879B03E534'
APPLICATION_2FA_NAME = 'codex2fa'

APPLICATION_2FA_MESSAGE_ID = '3C5BE1429D804E3EBE23BD17144340E5'

def create_new_person(user_data):
    try:
        conn = http.client.HTTPSConnection(BASE_URL)
        
        payload = {
            "firstName": user_data['nome'],
            "lastName": 'codex',
            "contactInformation": {
                "email": [{
                    "address": user_data['email'],
                }],
                "phone": [{
                    "number": str(user_data['celular']),
                }]
            }
        }
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        conn.request("POST", "/people/2/persons", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        return data
    
    except Exception as e:
        raise e
    
def send_user_pin(user_phone):
    try:
        print(user_phone)
        conn = http.client.HTTPSConnection(BASE_URL)
        
        payload = {
            "applicationId": APPLICATION_ID_2FA,
            "messageId": APPLICATION_2FA_MESSAGE_ID,
            "from": "Infobip 2FA",
            "to": str(user_phone),
        }
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        conn.request("POST", "/2fa/2/pin", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        
        return json.loads(data)
    except Exception as e:
        raise e
    
def verify_user_pin(user_pin_data):
    try:
        conn = http.client.HTTPSConnection(BASE_URL)
        
        payload = {
            "pin": user_pin_data['pinCode'],
        }
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        conn.request("POST", "/2fa/2/pin/" + user_pin_data['pinId'] + "/verify", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        return data
    except Exception as e:
        raise e
    
def resend_verify_user_pin(pin_id):
    try:
        conn = http.client.HTTPSConnection(BASE_URL)
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        conn.request("POST", "/2fa/2/pin/" + pin_id['pin_id'] + "/resend", {}, headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        return data
    except Exception as e:
        raise e
    
def send_message_whatsapp(user_phone):
    try:
        print(user_phone['phone'])
        conn = http.client.HTTPSConnection(BASE_URL)
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        payload = {
            "applicationId": APPLICATION_ID_2FA,
            "content": {
                "text": "Sua encomenda já esta em nosso estoque, por favor, faça a retirada.",
                "callbackData": "Callback data",
            },
            "messageId": APPLICATION_2FA_MESSAGE_ID,
            "from": "Infobip 2FA",
            "to": '55' + str(user_phone['phone']),
        }
        
        conn.request("POST", "/whatsapp/1/message/text", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        return data
    except Exception as e:
        raise e