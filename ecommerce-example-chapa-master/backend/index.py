import requests
import time
from chapa import Chapa

key_api = 'CHASECK_TEST-SLtpoGgR6Z0oiVoVnnNUK2wRJAa9ob5d'

# Generate a unique transaction reference using the current timestamp
unique_tx_ref = f"tx_fuad-{int(time.time())}"

data = {
    'email': 'testwe1@utube.com',
    'amount': 1000,
    'first_name': 'testt',
    'last_name': 'we1',
    'tx_ref': unique_tx_ref,
    'return_url': 'https://www.google.com',
    'callback_url': 'https://www.google.com/callback',
    'customization': {
        'title': 'utube',
        'description': 'payment for your services',
    }
}

chapa_instance = Chapa(key_api)
response = chapa_instance.initialize(**data)
print("Initialization response:", response)

# Manually verify the transaction
def custom_verify(transaction_ref):
    url = f"https://api.chapa.co/v1/transaction/verify/{transaction_ref}"
    headers = {
        'Authorization': f'Bearer {key_api}',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

verify_response = custom_verify(unique_tx_ref)
print("Custom verification response:", verify_response)
