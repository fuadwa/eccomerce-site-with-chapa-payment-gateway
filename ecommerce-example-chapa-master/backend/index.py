from chapa import Chapa
import time

key_api = 'CHASECK_TEST-SLtpoGgR6Z0oiVoVnnNUK2wRJAa9ob5d'

# Generate a unique transaction reference using the current timestamp
unique_tx_ref = f"tx_abebebikilaa-{int(time.time())}"

data = {
    'email': 'testwe1@utube.com',
    'amount': 1000,
    'first_name': 'testt',
    'last_name': 'we1',
    'tx_ref': unique_tx_ref,
    'return_url':'https://www.google.com',
    'callback_url':'https://www.google.com/callback',
    
    'customization':{
        'title':'utube',
        'description':'payment for your services',
    }
}

chapa_instance = Chapa(key_api)
response = chapa_instance.initialize(**data)
print(response)
