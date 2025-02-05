from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.exceptions.api_exception import APIException
  
import os

BW_USERNAME = os.environ["BW_USERNAME"]
BW_PASSWORD = os.environ["BW_PASSWORD"]
BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]

bandwidth_client = BandwidthClient(
    messaging_basic_auth_user_name=BW_USERNAME,
    messaging_basic_auth_password=BW_PASSWORD
)
messaging_client = bandwidth_client.messaging_client.client

media_file_name = 'sample_file_name'

try:
    response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
    downloaded_media_file = response.body
except APIException as e:
    print(e.response_code)
