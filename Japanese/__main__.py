import asyncio
import importlib

from pyrogram import idle

from Japanese-X-Spambot import app, LOGGER
from Japanese-X-Spambot.modules import ALL_MODULES


async def eval_bot():
    for all_module in ALL_MODULES:
        importlib.import_module(f"src.modules.{all_module}")
    LOGGER.info(f"Successfully loaded {len(ALL_MODULES)}.")

    LOGGER.info("Bot Started Succesfully, Say thanks to Mirza!! ")
    await idle()

    try:
        await app.stop()
    except:
        pass
    LOGGER.info("» Stopping! GoodBye, Say thanks to Mirza!! ")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(eval_bot())
