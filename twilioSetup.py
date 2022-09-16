"""
Author:  Utkarsh Gupta
Date:    11 August 2022
"""


from twilio.rest import Client  # install twilio for sending sms


account_sid = ''  # twilio account id
auth_token = ''  # twilio auth token
client = Client(account_sid, auth_token)  # twilio client object