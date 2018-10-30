import getpass
from exchangelib import EWSDateTime, EWSTimeZone, DELEGATE, Account, Credentials, Configuration, Message, Mailbox

from prettytable import PrettyTable

# ask for password
password = getpass.getpass()

#set credentials
credentials = Credentials(
    username='GLOBAL\\i331834',
    password=password
)

#set exchange server endpoint
config = Configuration(
    server='mail.sap.com',
    credentials=credentials
)

# set account
account = Account(
    primary_smtp_address='b.nagy@sap.com',
    config=config,
    autodiscover=False,
    access_type=DELEGATE
)

my_folder = account.inbox / 'RMK' / 'DC19'
items = my_folder.filter(
    sender='noreply@noreply19.stage.jobs2web.com'
)[:10]

table = PrettyTable([ 'Subject', 'Body', 'Recived'])

for msg in items:
    table.add_row([msg.subject, msg.body[0:10], msg.datetime_received])

print (table)