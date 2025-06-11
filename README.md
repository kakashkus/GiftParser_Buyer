[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_coding)

[![Static Badge](https://img.shields.io/badge/Telegram-Chat-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_codding_chat)

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/catsgang_bot/join?startapp=eVMDZF6Fxdb8eNnjocoOP)

## Recommendation before use

# 🔥🔥 PYTHON version must be 3.10 🔥🔥

> 🇷 🇺 README in russian available [here](README_ru.md)

# GiftParser + Buyer

This software is designed for automated parsing and purchasing of Telegram gifts. It allows users to configure parameters for tracking and acquiring available gifts based on specified criteria, such as price range and quantity of available gifts.

## How the software works

1.  **Awaiting new gift releases**: The software constantly monitors for new gifts.
2.  **Notification**: Once a new gift is detected, a notification is sent to a private chat, channel, or group.
3.  **Automated purchase**: The software proceeds to purchase the required quantity of the new gift.

### Detailed workflow:

1.  **Monitoring**: The software compares the list of all available gifts with those in a `.json` file every 8-15 seconds. If a new gift is found (i.e., not present in the `.json` file), it proceeds to the next step.
2.  **Notification details**: An animation of the gift and a message with collection information are sent. The recipient of these messages can be configured by setting the `NOTIFICATIONS_ID` in the `data/config.py` file.
3.  **Purchase logic**: The software checks if the gift's supply is within the allowed `SUPPLY_LIMIT` range and if its price is within the `PRICE_LIMIT` range. If both conditions are met, the bot purchases `GIFT_COUNT_TO_BUY` gifts for the chat ID specified in `ID_TO_BUY`.

## Installation and Setup

### 📋 Requirements
- Python 3.9+

### 🚀 Quick Start

1.  **Clone the repository**
    ```bash
    git clone https://github.com/kakashkus/GiftParser_Buyer.git
    cd GiftParser_Buyer
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # or
    venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure `data/config.py`**
    -   Open `data/config.py` and fill in your `API_ID`, `API_HASH`, `BOT_TOKEN_WRITER`, `NOTIFICATIONS_ID`, `ADMIN_ID`, and other auto-purchase settings (`BUY_GIFT`, `PRICE_LIMIT`, `SUPPLY_LIMIT`, `GIFT_COUNT_TO_BUY`, `ID_TO_BUY`).
    -   `API_ID`, `API_HASH`: Get them from [my.telegram.org/auth](https://my.telegram.org/auth).
    -   `BOT_TOKEN_WRITER`: Get this from [@BotFather](http://t.me/BotFather).
    -   For `ADMIN_ID` and `NOTIFICATIONS_ID`, you can use [@userinfobot](https://t.me/userinfobot) to get your chat ID.

5.  **Important Note for User Bot Session**
    -   The Telegram bot handles notifications, while a user bot (your Telegram account) performs the actual gift purchases.
    -   Upon the first run of `main.py`, a user session will be created. You will be prompted to enter your phone number and verification code.

## Running the software

### 🏃‍♂️ Main application
```bash
python main.py
```

## Configuration

Key configuration parameters are located in the `data/config.py` file:

1.  `API_ID`, `API_HASH`: These are essential for Telegram API access. You can obtain them from [my.telegram.org/auth](https://my.telegram.org/auth).
2.  `BOT_TOKEN_WRITER`: The Telegram bot token used for sending notifications about new gifts and purchase logs. Obtain this from [@BotFather](http://t.me/BotFather).
3.  `NOTIFICATIONS_ID`: The chat ID (group/channel/your account ID for direct messages) where the bot will send notifications about new gifts.
4.  `SEND_NOTIFICATIONS`: Set to `True` or `False` to enable or disable notifications mentioned in point 3.
5.  `ADMIN_ID`: The ID of your main account to which the bot will send gift purchase logs.
6.  `BUY_GIFT`: Set to `True` or `False` to enable or disable automated gift purchases.
7.  `PRICE_LIMIT`: The allowed price range for a gift.
8.  `SUPPLY_LIMIT`: The allowed supply range for a gift.
9.  `GIFT_COUNT_TO_BUY`: The number of gifts the bot should buy from a new collection.
10. `ID_TO_BUY`: The chat ID to which the gift should be purchased.

## Interesting Features

*   You can disable gift purchases (`BUY_GIFT = False`) and set `NOTIFICATIONS_ID` to a channel ID. This will turn your channel into a simple gift parser, similar to [@auto_gifts](https://t.me/auto_gifts).
*   The software can purchase gifts directly for a channel, your own account, or another account.
*   If automated purchase is disabled, there's no need to log in to a Telegram account (user bot session).

## Important Notes

The Telegram bot searches for and sends notifications about new gifts, while a user bot (Telegram account) handles the actual gift purchase. Therefore, a user session needs to be created. During the first test run, information about a gift will be displayed (if the gift is not new, no purchase will occur).

## Features

*   **Automated Gift Parsing**: Tracking new gifts available for purchase in Telegram.
*   **Flexible Purchase Settings**: Setting limits by price, quantity, and other parameters for automated gift acquisition.
*   **Notifications**: Receiving notifications about new gifts or purchase status.
