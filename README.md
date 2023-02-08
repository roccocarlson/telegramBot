# telegramBot
This is a simple telegram bot that sends the local IP address of a raspberry pi to a client whenever the pi reboots

## Why?
The on campus network doesn't allow for .local hostnames or static IP addresses, so running a headless raspberry pi can get annoying.

## How?
The python-telegram-bot library allows for a super simple interaction with the Telegram bot API. Creating a bot using Telegram is also super simple, using The Bot Father.

Creating a service in systemd on the raspberry pi so that the script runs at boot allows for a pretty pretty seemless integration.

## Update Feb 2023
I added a command for shutting down the pi. This is super useful for shutting down a pi without having to open up a remote connection.

<p align="center">
<img src="chat_image.jpg" alt="chat image" width="200px"/>
</p>

## Note
After ~1 year of using this, it't so useful. Being able to see that a headless pi has booted properly and connected to the internet saves so many troubleshooting steps.
