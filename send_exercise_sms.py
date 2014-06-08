#!/home2/davidkl1/venv/happiness/bin/python
import random
from twilio.rest import TwilioRestClient
import random
import time
import os

from_phone = ""
to_phone = ""

# "Twilio Key" needed, check evernote
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

def get_quote_index():
    if not os.path.exists('quote_index'):
        return 0
    try:
        with open('quote_index') as f:
            return int(f.read().strip())
    except ValueError:
        return 0

def save_quote_index(n):
    f = open('quote_index', 'w')
    f.write(str(n))
    f.close()

def send_inspirational_quote():
    quotes = open('quotes.out', 'r').readlines()
    quote_index = get_quote_index()
    quote = quotes[quote_index]
    quote_index += 1
    quote_index %= len(quotes)
    save_quote_index(quote_index)
    send_sms(quote)

def send_sms(body):
    result = client.sms.messages.create(
        body=body,
        to=to_phone,
        from_=from_phone)
    print 'send_sms % result: %s' % (body, result)
    return result

send_sms("Exercise time! Here's a quote to motivate you:")
time.sleep(5)
send_inspirational_quote()
time.sleep(5)
message1 = "Please go and exercise today to stay healthy! Reply to log what you did. \nLove, Julia."
send_sms(message1)

