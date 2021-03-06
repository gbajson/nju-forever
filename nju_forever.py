#!/usr/bin/env python
import os
import pprint
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from sh import mailx

email = os.environ["EMAIL"]
hostname = os.environ.get("HOSTNAME")

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

        if msg["Phone"] == "nju mobile":
            client.sms.send_sms(["80608"], "TAK")
            message = client.sms.delete_sms(int(msg["Index"]))
            mailx(["-s", f"SMS from {hostname}'", email], _in=message)
