import os

from vkbottle.bot import Bot, Message
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.environ.get("ACCESS_TOKEN")
bot = Bot(TOKEN)


@bot.on.message()
async def handler(message: Message) -> str:
    if not any(item.audio_message for item in message.attachments):
        return
    try:
        await bot.api.messages.delete(
            conversation_message_ids=[message.conversation_message_id],
            peer_id=message.peer_id,
            delete_for_all=True,
        )
    except Exception as e:
        print(e)


bot.run_forever()
