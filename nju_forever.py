#!/usr/bin/env python
import os
import pprint
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

number = os.environ["PHONE"]

# For limited access, I have valid credentials no need for limited access
with Connection("http://192.168.8.1/") as connection:
    client = Client(connection)
    message_list = client.sms.get_sms_list()
    print(message_list)

messages = message_list["Messages"]["Message"]

if isinstance(messages, list):
    for idx, msg in enumerate(messages):
        if msg["Index"] == "40000":
            continue
        pprint.pprint(msg)

        if msg["Phone"] == number:
            # client.sms.send_sms([number], 'TAK')
            result = client.sms.delete_sms(int(msg["Index"]))
            print(result)

        if msg["Phone"] == "nju mobile":
            client.sms.send_sms(["80608"], "TAK")
            result = client.sms.delete_sms(int(msg["Index"]))
            print(result)
            client.sms.send_sms([number], msg["Content"])
