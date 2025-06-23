import asyncio
from utils.core import load_from_json, save_to_json, logger
from pyrogram import Client
from data import config


async def snipe_new_gifts(bot_client: Client, tg_client: Client):
    gifts = await bot_client.get_available_gifts()
    gifts_in_json = load_from_json('gifts.json') or []

    for gift in gifts:
        gift_data = {'id': gift.id, 'price': gift.price}

        if gift_data not in gifts_in_json:
            save_to_json('gifts.json', gift_data)
            gifts_in_json.append(gift_data)

            if config.SEND_NOTIFICATIONS:
                limited_status = f'Limited ({gift.available_amount})' if gift.is_limited else 'No limits'

                try:
                    sticker = await bot_client.download_media(gift.sticker.file_id, in_memory=True)
                    sticker.name = 'sticker.tgs'
                    await bot_client.send_sticker(chat_id=config.NOTIFICATIONS_ID, sticker=sticker)
                except Exception as e:
                    logger.error(f"[Sticker] Failed to send to chat {config.NOTIFICATIONS_ID}: {e}")

                try:
                    message = (
                        f'<b>⬆️ NEW GIFT AVAILABLE ⬆️\n❗️ {limited_status}\n\n'
                        f'⭐ Price: {gift.price} STAR\n🎁 Supply: {gift.total_amount}</b>'
                    )
                    await bot_client.send_message(chat_id=config.NOTIFICATIONS_ID, text=message)
                except Exception as e:
                    logger.error(f"[Message] Failed to notify about new gift: {e}")

            if not gift.is_limited:
                continue

            if not (config.SUPPLY_LIMIT["FROM"] <= gift.total_amount <= config.SUPPLY_LIMIT["TO"]):
                continue

            if not (config.PRICE_LIMIT["FROM"] <= gift.price <= config.PRICE_LIMIT["TO"]):
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
    successful_purchases = 0
    errors = ''
    balance_before = await tg_client.get_stars_balance()

    for i in range(1, count + 1):
        try:
            await tg_client.send_gift(
                chat_id=chat_id,
                gift_id=gift_id,
                text='Gift was bought via @ApeCryptor soft'
            )
            successful_purchases += 1
        except Exception as e:
            err_msg = f"{i}/{count} | Error while buying gift {gift_id}: {e}"
            logger.error(err_msg)
            errors += f'{err_msg}\n'

        if i % 3 == 0:
            await asyncio.sleep(1)

    balance_after = await tg_client.get_stars_balance()

    errors_block = (
        f'<b>Errors while buying:</b>\n<blockquote expandable>{errors}</blockquote>'
        if errors else ''
    )

    summary_msg = (
        f'<b>✅ Successfully bought {successful_purchases} of {count} NEW GIFTS!\n\n'
        f'⭐ Stars spent: {balance_before - balance_after}\n'
        f'⭐ BALANCE before: {balance_before}\n'
        f'⭐ BALANCE after: {balance_after}</b>\n\n{errors_block}'
    )

    await bot_client.send_message(chat_id=config.ADMIN_ID, text=summary_msg)
    return successful_purchases
