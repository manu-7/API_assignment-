import os
import sys
import django
import logging
from django.conf import settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


django.setup()


from telegram.ext import Updater, CommandHandler
from api.models import TelegramUser

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    user = update.message.from_user
    username = user.username
    chat_id = user.id

    if not username:
        update.message.reply_text("Username not found in your Telegram profile.")
        return

    if not TelegramUser.objects.filter(chat_id=chat_id).exists():
        TelegramUser.objects.create(username=username, chat_id=chat_id)
        update.message.reply_text(f"Hello {username}, you've been registered!")
    else:
        update.message.reply_text(f"You're already registered, {username}!")

def main():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
