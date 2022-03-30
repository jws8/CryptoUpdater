#Top 10 Crypto Updater/Emailer
#Author: Joshua Wilson Smith (https://www.github.com/jws8)
#Date: 3/22/22
from MailSight import *
from CryptoUpdater import *
import time
print("Requires MailSight, CryptoUpdater in file")
now = time.time()
email_batch = ["youremail@gmail.com", "anotheremail@outlook.com"]

updater = CryptoUpdater()
my_gmail = MailSight()

crypto_dict = updater.get_data()
message = f"" 
#Loop through the keys and values in crypto_dict and format the key and value
i = 0
for key, val in crypto_dict.items():
    i+=1
    message = message + " " + str(i) + ") " + key + ": " + val + " USD" + "\n"
print(message)

my_gmail.set_username_password("Youremail@emailer.com", "YourPassword")
my_gmail.send_mail("Top 10 Crypto Assets Today by Market Cap: @" + str(time.ctime(now)), message, email_batch)