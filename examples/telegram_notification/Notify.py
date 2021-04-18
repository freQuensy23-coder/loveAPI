import json
from collections import namedtuple
from examples.telegram_notification.Telegram_api import api_id, api_hash
from pyrogram import Client
from API import API
import logging
import datetime
import config

# Модуль которы отправляет указаному контакту
# Утром - очень милое пожелание доброго утра
# Вечером - очень милое пожелание доброй ночи

gender = 'her'  # Гендер человека которому будут отправляться сообщения
love_api = API()
ENDPOINTS = love_api.get_endpoints()
Chat = namedtuple("chat", "chat_id name num")
log = logging.getLogger("Telegram")
data_filename = "data.json"
logging.basicConfig(level=logging.DEBUG)


def to_bool(s: str):
    """Convert y/n answer to True or False"""
    if s.strip().lower() == "y":
        return True
    else:
        return False

def get_all_chats(dialogs) -> list[Chat]:
    """Get list of Chats (namedtuples). Takes list of dialogs got by app.get_dialogs()"""
    res = []
    for i, dialog in enumerate(dialogs):
        if dialog['chat']['type'] == "private":
            chat = Chat(dialog['chat']["id"], dialog['chat']['first_name'], i)
        elif dialog['chat']['type'] == "bot":
            chat = Chat(dialog['chat']["id"], dialog['chat']['username'], i)
        else:
            chat = Chat(dialog['chat']["id"], dialog['chat']['title'], i)
        res.append(chat)
    return res


if __name__ == '__main__':
    try:
        with open(data_filename, "r") as f:
            data = json.load(f)
            log.debug(data)
    except FileNotFoundError:
        data = None

    if not data:
        with Client("my_account", api_id, api_hash) as app:
            dialogs_list = app.get_dialogs()
            chats = get_all_chats(dialogs_list)
            for i, chat in enumerate(chats):
                print(f"({chat.num}) {chat.name}")
            chat_num = int(input("Select chat"))
            chat_id = chats[chat_num]["chat_id"]
            send_morning = to_bool(input("Send in morning (y/N)"))
            send_evening = to_bool(input("Send in evening (y/N)"))
            with open(data_filename, "w") as f:
                save_dict = {"chat_id":chat_id, "send_morning":send_morning, "send_evening":send_evening}
                json.dump(save_dict, f)
                log.debug(f"Saving {save_dict}")
                data = save_dict

    with Client("my_account", api_id, api_hash) as app:

        chat_id = data["chat_id"]
        send_morning = data["send_morning"]
        send_evening = data["send_evening"]

        hours = datetime.datetime.now().hour
        is_morning = False
        is_evening = False
        if hours == 8:
            is_morning = True
            is_evening = False
        elif hours == 22:
            is_morning = False
            is_evening = True

        if is_morning and send_morning:
            msg = love_api.get_random_msg(endpoints=[ENDPOINTS[gender]["morning"]])
            log.debug(f'Sending morning msg, {int(chat_id)}, {msg} ')
            app.send_message(chat_id=int(chat_id), text=str(msg))
            log.info(msg)
        if is_evening and send_evening:
            msg = love_api.get_random_msg(endpoints=[ENDPOINTS[gender]["night"]])
            app.send_message(chat_id, str(msg))
            log.info(msg)

        log.info("App stopped")