# 🚨 SSH Login Alarm Bot for Linux Server 🚨

This bot sends an alarm message to your Telegram channel or chat whenever someone logs into your Linux server via SSH. It’s a quick and easy way to monitor unauthorized access attempts and get instant notifications!

## 📜 Features
- Alerts you in real time when someone logs into your server via SSH
- Configurable to send alerts to your Telegram chat or group
- Simple setup with Telegram bot integration

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/erkankyn1/ssh-alert.git
    cd ssh-alert
    ```

2. **Install required dependencies**:
   - Python 3 and pip are recommended for this bot.
    ```bash
    pip install requests
    ```

3. **Configure the Bot**:
   - Update the `main.py` file with your **Telegram Bot Token** and **Chat ID**.
   
4. **Setup the SSH Hook**:
   - Add the script to execute on SSH login by modifying the `.bashrc` or `/etc/profile` file for the user you want to monitor.
   - Example:
     ```bash
     python3 /path/to/ssh-login-alarm-bot/alarm.py '🔔 **Alert:** SSH login detected! 👤 **User:** '`who` ' 🖥️ **IP:** '`hostname` '⏰ **Time:** ' `date`
     ```

## 📲 Setting Up Your Telegram Bot and Getting the API Key

To connect this bot to your Telegram account, you’ll need to create a new Telegram bot and get the API key. Follow these steps:

1. **Create a New Bot**:
    - Open Telegram and search for [BotFather](https://t.me/botfather), the official bot to create and manage Telegram bots.
    - Start a chat with BotFather and send the command:
      ```
      /start
      ```
    - Next, send:
      ```
      /newbot
      ```
    - BotFather will ask you for a name for your bot. Choose a descriptive name, like `SSH Login Alarm`.
    - Then, you’ll need to set a unique username that ends with `_bot` (e.g., `ssh_login_alarm_bot`).

2. **Get Your API Token**:
    - After you’ve set the name and username, BotFather will generate and send you an **API Token**. It will look like this:
      ```
      123456789:ABCdefGHI_jklMNOpqrSTUvWXyz
      ```
    - **Save this token** – you’ll need it to connect your SSH alarm bot to Telegram.

3. **Find Your Chat ID**:
    - To receive messages, you’ll need your chat ID. Here’s how to find it:
      - Start a chat with [IDBot](https://t.me/myidbot) on Telegram.
      - Send `/getid` to IDBot, and it will reply with your chat ID.
      - Alternatively, you can use the `getUpdates` method with your API token to retrieve the chat ID.

## 🚀 Usage

Once configured, the bot will automatically send a message to your Telegram chat each time there is an SSH login on your server.

You can test it by logging into your server through SSH, and you should receive a notification like this:

🔔 **Alert:** SSH login detected! 👤 **User:** username 🖥️ **IP:** IP_address ⏰ **Time:** login_time

