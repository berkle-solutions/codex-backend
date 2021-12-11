from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# infobip
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException
from infobip_api_client.api_client import ApiClient, Configuration
#service
from codex.services.infobip import send_message_whatsapp

class NotificacaoView(APIView):
    
    
    @api_view(['POST'])
    def enviar_notificacao_wpp(request):
        try:
            send_message_whatsapp(request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise APIException(e)
    
    @api_view(['POST'])
    def enviar_notificacao(request):
        client_config = Configuration(
            host='yr8e3d.api.infobip.com',
            api_key={"APIKeyHeader": '3ab9363359b48d88f1b7b2b11cd92f76-137f1861-a3bd-483b-b7de-902f788c8f49'},
            api_key_prefix={"APIKeyHeader": 'App'},
        )
        
        api_client = ApiClient(client_config)

        DESTINATION = request.data['destination']
        MESSAGE = request.data['message']
        SENDER = 'InfoSMS'
        
        sms_request = SmsAdvancedTextualRequest(
            messages=[
                SmsTextualMessage(
                    destinations=[
                        SmsDestination(
                            to=DESTINATION
                        ),
                    ],
                    _from=SENDER,
                    text=MESSAGE,
                )
            ]
        )
        
        api_instance = SendSmsApi(api_client)

        try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            print(api_response)
            return Response(status=status.HTTP_200_OK)
        except ApiException as ex:
            print("Error occurred while trying to send SMS message.")
            print(ex)
        