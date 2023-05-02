from vk_api.longpoll import VkEventType, VkLongPoll
from bot import *
from db import *
from config import *

for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = event.user_id
        if request in ('поиск', 'f'):
            bot.get_age_of_user(user_id)
            bot.get_city(user_id)
            bot.looking_for_persons(user_id) # "отображает перечень обнаруженных людей в чате"
            bot.show_found_person(user_id)  # "включает их в базу данных"
        elif request in ('удалить', 'd'):
            delete_table_seen_person()  # "стирает имеющуюся базу данных"
            create_table_seen_person()  #  "создает новую базу данных"
            bot.send_msg(user_id, f' База данных отчищена! Сейчас наберите "Поиск" или F ')
        elif request in ('смотреть', 's'):
            if bot.get_found_person_id() != 0:
                bot.show_found_person(user_id)
            else:
                bot.send_msg(user_id, f' В начале наберите Поиск или f.  ')
        else:
            bot.send_msg(user_id, f'{bot.name(user_id)} Бот готов к поиску, наберите: \n '
                                      f' "Поиск или F" - Поиск людей. \n'
                                      f' "Удалить или D" - удаляет старую БД и создает новую. \n'
                                      f' "Смотреть или S" - просмотр следующей записи в БД.')
