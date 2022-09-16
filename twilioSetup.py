"""
Author:  Utkarsh Gupta
Date:    11 August 2022
"""


from twilio.rest import Client  # install twilio for sending sms


account_sid = 'ACbdec4ccbe7604045ba9dae6638c76c13'  # twilio account id
auth_token = 'd5f315f94e64ccf91122ec64a9cf7742'  # twilio auth token
client = Client(account_sid, auth_token)  # twilio client object