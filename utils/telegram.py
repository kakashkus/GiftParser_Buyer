import asyncio
from utils.core import load_from_json, save_to_json, logger
from pyrogram import Client
from data import config


async def snipe_new_gifts(bot_client: Client, tg_client: Client):
    gifts = await bot_client.get_available_gifts()
    gifts_in_json = load_from_json('gifts.json')

    for gift in gifts:
        gift_dict = {'id': gift.id, 'price': gift.price}

        if gift_dict not in gifts_in_json:
            save_to_json('gifts.json', gift_dict)
            gifts_in_json.append(gift_dict)

            if config.SEND_NOTIFICATIONS:
                limited = f'Limited ({gift.available_amount})' if gift.is_limited else 'No limits'
                try:
                    sticker_data = await bot_client.download_media(gift.sticker.file_id, in_memory=True)
                    sticker_data.name = 'sticker.tgs'
                    await bot_client.send_sticker(chat_id=config.NOTIFICATIONS_ID, sticker=sticker_data)
                except Exception as e:
                    logger.error(f"Error while sending a sticker to {config.NOTIFICATIONS_ID} chat id: {e}")

                try:
                    txt = f'<b>⬆️ NEW GIFT AVAILABLE ⬆️\n❗️ {limited}\n\n⭐ Price: {gift.price} STAR\n🎁 Supply: {gift.total_amount}</b>'
                    await bot_client.send_message(chat_id=config.NOTIFICATIONS_ID, text=txt)
                except Exception as e:
                    logger.error(f"Error while sending a message about new gift to {config.NOTIFICATIONS_ID} chat id: {e}")

            if not gift.is_limited or gift.total_amount < config.SUPPLY_LIMIT["FROM"] or gift.total_amount > config.SUPPLY_LIMIT["TO"]:
                continue

            if gift.price < config.PRICE_LIMIT['FROM'] or gift.price > config.PRICE_LIMIT['TO']:
                continue

            if config.BUY_GIFT:
                await buy_gift(
                    bot_client=bot_client,
                    tg_client=tg_client,
                    count=config.GIFT_COUNT_TO_BUY,
                    gift_id=gift.id,
                    chat_id=config.ID_TO_BUY
                )


async def buy_gift(bot_client: Client, tg_client: Client, count: int, gift_id: int, chat_id: [int, str]):
    bough_gifts = 0
    star_balance_before = await tg_client.get_stars_balance()

    errors = ''
    for number in range(1, count+1):
        try:
            await tg_client.send_gift(chat_id=chat_id, gift_id=gift_id, text='Gift was bought via @ApeCryptor soft')
            bough_gifts += 1
        except Exception as e:
            error_txt = f"{number}/{count} | Error while buying a gift {gift_id}: {e}"

            logger.error(error_txt)
            errors += f'{error_txt}\n'

        if number % 3 == 0:
            await asyncio.sleep(1)

    star_balance_after = await tg_client.get_stars_balance()
    errors_txt = f'<b>Errors while buying:</b>\n<blockquote expandable>{errors}</blockquote>' if errors else ''

    await bot_client.send_message(
        chat_id=config.ADMIN_ID,
        text=f'<b>✅ Successfully bought {bough_gifts} of {config.GIFT_COUNT_TO_BUY} NEW GIFTS!\n\n⭐ Stars spent: {star_balance_before-star_balance_after}\n⭐ BALANCE before: {star_balance_before}\n⭐ BALANCE after: {star_balance_after}</b>\n\n{errors_txt}'
    )

    return bough_gifts


