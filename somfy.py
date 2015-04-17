#! /usr/bin/python
# -*- coding: utf8 -*-
# Benjamin Béguin
# blog.bratik.fr
# 17-04-2015

import requests
import re
import sys
import getopt

login="i"
password="2222"
keyDict = {"A1":"5032","A2":"7829","A3":"1026","A4":"0531","A5":"0817","B1":"0831","B2":"8374","B3":"1739","B4":"9407","B5":"7003","C1":"3064","C2":"3421","C3":"2579","C4":"9542","C5":"0265","D1":"0594","D2":"3675","D3":"8449","D4":"1998","D5":"0213","E1":"5446","E2":"5665","E3":"8707","E4":"7371","E5":"4844","F1":"1555","F2":"5212","F3":"7626","F4":"6537","F5":"0585"}

ip=""

usage=("Usage : "+sys.argv[0]+" -i <ip> [-p <port>]")

# Get request to retrieve the key ID
getRequest=requests.get("http://"+ip+"/fr/login.htm")

# Retrieve the key ID from the get request
match=re.search(r"(\<b\>)(\w\w)",getRequest.text)
if match:
    keyId=match.group(2)
else:
    print("Code d'autentification non détecté")
    print(getRequest.text)
    exit(1)
print("Key ID : "+keyId)

# Testing the connection
payload={'login':login,'password':password,'key':keyDict[keyId],'btn_login':'Connexion'}
postRequest=requests.post("http://"+ip+"/fr/login.htm",payload)
success=re.search(r"\/logout\.htm",postRequest.text)
if success:
    print("Connexion réussie, déconnexion.")
    logout=requests.get("http://"+ip+"/logout.htm",cookies=postRequest.cookies)
else:
    print("La connexion a échoué")
    print(postRequest.text)
    exit(1)
