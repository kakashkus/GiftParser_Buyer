import asyncio
import random
from utils.core import logger
from pyrogram import Client
from data import config
from utils.telegram import snipe_new_gifts


async def init_clients():
    bot_client = Client('TgBot', bot_token=config.BOT_TOKEN_WRITER, api_hash=config.API_HASH, api_id=config.API_ID)
    await bot_client.start()

    bot = await bot_client.get_me()
    logger.info(f"Initialized bot client. Bot: {bot.full_name} (@{bot.username}); id:{bot.id} ")

    tg_client = Client("TgAccount", api_hash=config.API_HASH, api_id=config.API_ID)
    if config.BUY_GIFT:
        await tg_client.start()

        user = await tg_client.get_me()
        star_balance = await tg_client.get_stars_balance()
        logger.info(f"Initialized account client. User: {user.full_name} (@{user.username}); ID:{user.id}; star balance: {star_balance}; ID to buy gifts: {config.ID_TO_BUY}")

    else:
        logger.info('account client does not require initialization')

    return bot_client, tg_client


async def main():
    bot_client, tg_client = await init_clients()

    while True:
        try:
            await snipe_new_gifts(bot_client=bot_client, tg_client=tg_client)
            await asyncio.sleep(random.uniform(8, 15))

        except Exception as e:
            await asyncio.sleep(1)
            logger.error(f"Error in main function: {e}")


asyncio.run(main())
