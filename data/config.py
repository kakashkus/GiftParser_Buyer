API_ID = 0011
API_HASH = '312321321312f'

# Bot token from @BotFather
BOT_TOKEN_WRITER = '332132132132'

# chat/channel id to which notifications about new gifts will be sent. For a bot to send notifications to a channel, it needs to be added there
SEND_NOTIFICATIONS = True
NOTIFICATIONS_ID = 312321321

# id account to which the bot will write about gift buy. !!!Before you run the soft, you should write first to the bot
ADMIN_ID = 321321321


# # # Auto-purchase settings

# True/False.
BUY_GIFT = True

# Price limit. A purchase will be made if the price of the gift is in the FROM-TO range
PRICE_LIMIT = {
    "FROM": 0,
    "TO": 500
}

# Supply limit. A purchase will be made if the gift supply is between FROM-TO
SUPPLY_LIMIT = {
    "FROM": 1,
    "TO": 10000
}

# Number of gifts per purchase from the collection
GIFT_COUNT_TO_BUY = 20

# chat/channel id on which the gifts will be purchased. ADMIN_ID - if you buy yourself
ID_TO_BUY = -3213213123
