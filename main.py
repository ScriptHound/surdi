import os

from vkbottle.api.api import API
from vkbottle.bot import Bot, Message
from dotenv import load_dotenv
from vkbottle.exception_factory import VKAPIError

load_dotenv('.env')
TOKEN = os.environ.get("ACCESS_TOKEN")
bot = Bot(TOKEN)
api = API(token=TOKEN)


@bot.on.message()
async def handler(message: Message) -> str:
    attachment = message.attachments
    if attachment != []:
        attachment = attachment[0]
        if attachment.audio_message is not None:
            message_id = message.conversation_message_id
            delete_for_all = True
            peer_id = message.peer_id
            try:
                await api.messages.delete(
                    conversation_message_ids=[message_id],
                    peer_id=peer_id,
                    delete_for_all=delete_for_all)
            except Exception as e:
                print(e)
                return "Не хватает прав, чтобы удалить"
            return "Голосовое удалено"

bot.run_forever()
