from telebot import types, TeleBot
from keyboard import fractions, curning_hares, housekeeping_victoria, belobog
from database.database import find_agent
#Обработчик всех команд
def message_hendler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start(mess: types.Message):
        bot.send_message(mess.chat.id,'<b>Привет я умею отправлять информацию персонажей из игры zenless zone zero</b>', parse_mode='HTML')
        bot.send_message(mess.chat.id, '<b>Выбери фракцию:</b>', reply_markup=fractions, parse_mode='HTML')

def callback_query(bot: TeleBot):
    #Callbcack обработчик
    @bot.callback_query_handler(func=lambda call:True)
    def callback_fraction(call: types.CallbackQuery):
        if call.data == 'curning_hares':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Выбери агента:',
                                  reply_markup=curning_hares)
        elif call.data == 'victoria':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Выбери агента:',
                                  reply_markup=housekeeping_victoria)
        elif call.data == 'belobog':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Выбери агента:',
                                  reply_markup=belobog)
        elif call.data == 'back_curning' or call.data == 'back_victoria' or call.data == 'back_belobog':
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='<b>Выбери фракцию:</b>',
                                  reply_markup=fractions,
                                  parse_mode='HTML')
        else:
            agent = find_agent(call.data)
            if agent:
                text = f"<b>{agent[1]}</b>\n" \
                       f"<i>{agent[2]}</i>\n\n" \
                       f"{agent[3]}"
                photo = agent[4]
                bot.send_photo(call.message.chat.id, photo=open(photo, 'rb'), caption=text, parse_mode='HTML')