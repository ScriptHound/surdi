import os

from vkbottle.bot import Bot, Message
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.environ.get("ACCESS_TOKEN")
PERMITTED_USERS = os.environ.get("LUCHSHIE_MALCHIKI")
bot = Bot(TOKEN)


@bot.on.message()
async def handler(message: Message) -> str:
    audio_message = None
    if str(message.from_id) in PERMITTED_USERS:
        return

    for item in message.attachments:
        if item.audio_message is not None:
            audio_message = item.audio_message

    if audio_message is None:
        return
    try:
        print(audio_message.transcript)
        await bot.api.messages.delete(
            conversation_message_ids=[message.conversation_message_id],
            peer_id=message.peer_id,
            delete_for_all=True,
        )
    except Exception as e:
        print(e)


bot.run_forever()
