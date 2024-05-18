import requests
from .models import TeleSettings
import datetime
 


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        chat_id = str(settings.tg_chat)
        token = str(settings.tg_token)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]
            current_time = datetime.datetime.now()
            text_slised = part_1 + tg_name + part_2 + tg_phone + part_3 + '\nВремя отправки: ' + current_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            text_slised = text
        try:    
            req = requests.post(method, data={
                'chat_id':chat_id,
                'text':text_slised,
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Сообщение в телеграм отправлено')
    else:
        pass