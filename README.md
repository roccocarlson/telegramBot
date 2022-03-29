# telegramBot
This is a simple telegram bot that sends the local IP address of a raspberry pi to a client whenever the pi reboots

## Why?
The on campus network doesn't allow for .local hostnames or static IP addresses, so running a headless raspberry pi can get annoying.

## How?
The python-telegram-bot library allows for a super simple interaction with the Telegram bot API. Creating a bot using Telegram is also super simple, using The Bot Father.

Creating a service in systemd on the raspberry pi so that the script runs at boot allows for a pretty pretty seemless integration.
![chat image](chat_image.jpg)