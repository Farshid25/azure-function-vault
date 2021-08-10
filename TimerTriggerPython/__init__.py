import datetime
import logging
import azure.functions as func

import datetime
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
        KVUri = "https://<myvault>.azure.net/"

        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)

        secretName = "testsecret"

        retrieved_secret = client.get_secret(secretName)
        
        print("secrate name:", retrieved_secret.name)
        print("secrate value :",retrieved_secret.value)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print( "hi farshid")
