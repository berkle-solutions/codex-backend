import http.client
import json

import environ
env = environ.Env()
environ.Env.read_env()


BASE_URL = env('INFOBIP_BASE_URL')
API_KEY = env('INFOBIP_API_KEY')

DEFAULT_HEADERS = {
    'Authorization': env('INFOBIP_API_KEY'),
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

APPLICATION_ID_2FA = env('APPLICATION_ID_2FA')
APPLICATION_2FA_NAME = env('APPLICATION_2FA_NAME')

APPLICATION_2FA_MESSAGE_ID = env('APPLICATION_2FA_MESSAGE_ID')

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
                    "number": '55' + user_data['celular'],
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
        conn = http.client.HTTPSConnection(BASE_URL)
        
        payload = {
            "applicationId": APPLICATION_ID_2FA,
            "messageId": APPLICATION_2FA_MESSAGE_ID,
            "from": "Infobip 2FA",
            "to": '55' + user_phone,
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
            "pin": str(user_pin_data['pinCode']),
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
    
def send_message_whatsapp(user_phone, message = "Sua encomenda já esta em nosso estoque, por favor, faça a retirada."):
    try:
        conn = http.client.HTTPSConnection(BASE_URL)
        
        headers = {
            'Authorization': DEFAULT_HEADERS['Authorization'],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        payload = {
            "content": {
                "text": message,
            },
            "messageId": APPLICATION_2FA_MESSAGE_ID,
            "from": "447860099299",
            "to": '55' + user_phone['phone'],
        }
        
        conn.request("POST", "/whatsapp/1/message/text", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read().decode('utf-8')
        return data
    except Exception as e:
        raise e