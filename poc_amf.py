import requests
import pyamf
from pyamf import remoting
from pyamf.flex import messaging
import uuid

from prettytable import PrettyTable

host = 'command98.stage.jobs2web.com'
email = 'initial.user@sap.com'
password = 'TempPass123'

# to check with burp
proxies = {
    'http': 'localhost:8080',
    'https': 'localhost:8080'
}

# make a login
login_request = requests.post(
    ''.join(['http://', host, '/?method=loginUser']),
    data = {
        'email' : email, 
        'password' : password
    },
    #proxies = proxies
)

# save cookies
jar = login_request.cookies

# build message for CF backend
msg = messaging.RemotingMessage(
    operation='loadRoles',
    source='model.remote.remoteRoleManager',
    destination='ColdFusion',
    messageId=str(uuid.uuid4()).upper(),
    body=[0,'cc']
)
# make an envelope
req = remoting.Request(target='null',body=[msg])
ev = remoting.Envelope(pyamf.AMF3)
ev['/0'] = req
# encode id
bin_msg = remoting.encode(ev)
# send -> the xml formatted request you can find in AMF folder
resp = requests.post(
    ''.join(['http://', host, '/flex2gateway/']),
    data = bin_msg.getvalue(),
    headers = {'Content-Type': 'application/x-amf'},
    cookies = jar,
    #proxies = proxies
)
# get the response -> the xml formatted response you can find in AMF folder
resp_msg = remoting.decode(resp.content)
#print(resp_msg.bodies)
# iterate in a dirty way...
# resp_mgs.bodies -> list
resp_msg_list = resp_msg.bodies
# resp_msg_list -> tuple
resp_msg_list_element = resp_msg_list[0]
# <class 'pyamf.remoting.Response'>
#print(resp_msg_list_element[1])
resp_body = resp_msg_list_element[1].body
# get the role array
resp_array = resp_body.body

# have a nice output of roles
table = PrettyTable(['Role name', 'Role Description', 'Last modified'])
for element in resp_array:
    table.add_row([element.name, element.description, element.lastmodified])
print (table)

# logout
logout_req = requests.get(
    ''.join(['http://', host, '/?method=logoutUser']),
    #proxies = proxies,
    cookies = jar
)