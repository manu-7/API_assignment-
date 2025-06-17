import logging
import os
import sys
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()


from telegram.ext import Updater, CommandHandler
from api.models import TelegramUser

# Logging config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Start command logic
def start(update, context):
    username = update.message.from_user.username
    chat_id = update.message.chat_id

    if not TelegramUser.objects.filter(username=username).exists():
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

if __name__ == "__main__":
    main()
