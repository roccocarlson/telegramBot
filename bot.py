"""
    Rocco Carlson
    March 29 2020
    Telegram bot for receiving local IP address from a raspberry pi
"""

from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update
from urllib import request
import subprocess, logging

global HOSTNAME
HOSTNAME = '0.0.0.0'

# CHAT ID FOR SPECIFIC CHAT - BOT WILL NOT WORK IN ANY OTHER CHAT
with open('/home/pi/Documents/telegramBot/chatid.txt', 'r') as f:
    CHAT_ID = f.readline()
    print("Chat ID: "+CHAT_ID)

# API ID FOR BOT - OBTAINED FROM BOT FATHER
with open('/home/pi/Documents/telegramBot/apiid.txt', 'r') as f:
    API_ID = f.readline()
    print("API ID: "+API_ID)

def wait_for_internet_connection():
    while True:
        try:
            response = request.urlopen('http://google.com',timeout=1)
            print("Connected to internet!")
            return
        except:
            pass

# Function for simple testing
def test(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=CHAT_ID, text='Hello there')

# Function for sending the ip address of the Pi upon request
# Also invoked upon startup of the Pi
def ip(update: Update, context: CallbackContext):
    HOSTNAME = subprocess.getoutput('hostname -I').split(" ", 2)[0]
    print('Sending IP...', end='')
    context.bot.send_message(chat_id=CHAT_ID, text=('IP: ' + HOSTNAME))
    print(' Sent!')

# Function for shutting down the Pi after recieving telegram message
# Same shutdown process as commonly used for GPIO button shutdown
def shutdown(update: Update, context: CallbackContext):
    print('Shutting down...')
    context.bot.send_message(chat_id=CHAT_ID, text=('Shutting down now...'))
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

def main():

    # WAIT UNTIL CONNECTED TO INTERNET - IMPORTANT FOR SYSTEMD
    wait_for_internet_connection()

    # HOSTNAME FOR THE DEVICE - TO BE SENT ON /ip REQUEST
    HOSTNAME = subprocess.getoutput('hostname -I').split(" ", 2)[0]

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token=API_ID, use_context=True)
    dispatcher = updater.dispatcher

    # SEND IP WHEN RASPI REBOOTS
    print('Sending IP...', end='')
    updater.bot.send_message(chat_id=CHAT_ID, text=('Raspberry Pi booted!\nIP: ' + HOSTNAME))
    print(' Sent!')

    dispatcher.add_handler(CommandHandler('test', test))
    dispatcher.add_handler(CommandHandler('ip', ip))
    dispatcher.add_handler(CommandHandler('shutdown',shutdown))

    updater.start_polling()

if __name__ == '__main__':
    main()
