require 'bandwidth'

include Bandwidth
include Bandwidth::WebRtc

BW_USERNAME = ENV['BW_USERNAME']
BW_PASSWORD = ENV['BW_PASSWORD']
BW_ACCOUNT_ID = ENV['BW_ACCOUNT_ID']

bandwidth_client = Bandwidth::Client.new(
    web_rtc_basic_auth_user_name: BW_USERNAME,
    web_rtc_basic_auth_password: BW_PASSWORD
)

web_rtc_client = bandwidth_client.web_rtc_client.client

session_id = "1234-abcd"
participant_id = "4312-dbca"

begin
    #web_rtc_client.remove_participant_from_session(BW_ACCOUNT_ID, session_id, participant_id)
    web_rtc_client.remove_participant_from_session(BW_ACCOUNT_ID, participant_id, session_id)
    #NOTE: This is currently improperly defined
rescue APIException => e
    puts e.response_code
end