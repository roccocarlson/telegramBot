"""
    Rocco Carlson
    March 29 2020
    Telegram bot for receiving local IP address from a raspberry pi
"""

from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update
from urllib import request
import subprocess, logging

# CHAT ID FOR SPECIFIC CHAT - BOT WILL NOT WORK IN ANY OTHER CHAT
with open('chatid.txt', 'r') as f:
    CHAT_ID = f.readline()
    print("Chat ID: "+CHAT_ID)

# API ID FOR BOT - OBTAINED FROM BOT FATHER
with open('apiid.txt', 'r') as f:
    API_ID = f.readline()
    print("API ID: "+API_ID)

# HOSTNAME FOR THE DEVICE - TO BE SENT ON /ip REQUEST
HOSTNAME = subprocess.getoutput('hostname -I').split(" ", 2)[0]

def wait_for_internet_connection():
    while True:
        try:
            response = request.urlopen('http://google.com',timeout=1)
            print("Connected to internet!")
            return
        except:
            pass

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=CHAT_ID, text='Hello there')

def ip(update: Update, context: CallbackContext):
    print('Sending IP...', end='')
    context.bot.send_message(chat_id=CHAT_ID, text=('IP: ' + HOSTNAME))
    print(' Sent!')

def main():

    # WAIT UNTIL CONNECTED TO INTERNET - IMPORTANT FOR SYSTEMD
    wait_for_internet_connection()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    updater = Updater(token=API_ID, use_context=True)
    dispatcher = updater.dispatcher

    # SEND IP WHEN RASPI REBOOTS
    print('Sending IP...', end='')
    updater.bot.send_message(chat_id=CHAT_ID, text=('Raspberry Pi booted!\nIP: ' + HOSTNAME))
    print(' Sent!')

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ip', ip))

    updater.start_polling()

if __name__ == '__main__':
    main()