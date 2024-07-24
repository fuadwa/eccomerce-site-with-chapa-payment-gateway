from chapa import Chapa
import time
import requests
from datetime import datetime

key_api = 'CHASECK_TEST-SLtpoGgR6Z0oiVoVnnNUK2wRJAa9ob5d'

# Generate a unique transaction reference using the current timestamp
unique_tx_ref = f"tx_fuad-{int(time.time())}"
chapa_instance = Chapa(key_api)

class Payment:
    @staticmethod
    def pay(email, fname, lname, amount, rdurl):
        now = datetime.now()
        tx_un_num = now.strftime("%m%d%Y%H%M%S")
        tx_id = f'tx_{fname}{tx_un_num}'
        data = {
            'email': email,
            'amount': amount,
            'first_name': fname,
            'last_name': lname,
            'tx_ref': tx_id,
            'return_url': 'https://www.google.com',
            'rdurl': rdurl,
            'customization': {
                'title': 'utube',
                'description': 'payment for your services',
            }
        }

        response = chapa_instance.initialize(**data)
        return {'detail': response, 'tx_id': tx_id}

    @staticmethod
    def custom_verify(transaction_ref):
        url = f"https://api.chapa.co/v1/transaction/verify/{transaction_ref}"
        headers = {
            'Authorization': f'Bearer {key_api}',
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        return response.json()
