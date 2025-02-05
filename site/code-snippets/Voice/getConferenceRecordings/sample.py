from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.exceptions.api_exception import APIException

import os

BW_USERNAME = os.environ["BW_USERNAME"]
BW_PASSWORD = os.environ["BW_PASSWORD"]
BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]

bandwidth_client = BandwidthClient(
    voice_basic_auth_user_name=BW_USERNAME,
    voice_basic_auth_password=BW_PASSWORD
)
voice_client = bandwidth_client.voice_client.client

conference_id = "conf-1234"

try:
    response = voice_client.get_conference_recordings(BW_ACCOUNT_ID, conference_id)
    if len(response.body) > 0:
        print(response.body[0].name)
except APIException as e:
    print(e.response_code)
