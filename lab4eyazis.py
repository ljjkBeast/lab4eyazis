import telebot
import dbworker
bot = telebot.TeleBot('')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет, мой дорогой друг! Отправь мне название автомобильного бренда и я пришлю тебе список моделей, которые доступны к покупке в Беларуси.')

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'Бот отправляет список моделей, которые доступны к покупке в РБ.'
                                '\nИнструкция: \n1. Пришли мне название бренда на русском или английском языке;'
                                '\n2. В общем-то всё, наслаждайся результатом))0)'
                                '\n-----------------------------------------------------------------------------------'
                                '\nПриятного использования!')


def get_brand_from_message(message):
    br = ""
    a_list = ["ауди", "audi"]
    p_list = ["порше", "порш", "porsche"]
    v_list = ["фольксваген", "вольксваген", "фольцваген", "volkswagen"]
    s_list = ["стоп", "всё", "все", "хватит", "отдыхай"]

    for word in a_list:
        if word in message.text.lower():
            br = "audi"

    for word in p_list:
        if word in message.text.lower():
            br = "porsche"

    for word in v_list:
        if word in message.text.lower():
            br = "vw"

    for word in s_list:
        if word in message.text.lower():
            br = "stop"

    return br





@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text.lower() == "привет":
        start(message)

    elif message.text.lower() == "помощь":
        help(message)

    elif get_brand_from_message(message) == "":
        bot.send_message(message.chat.id, "Я еще не знаю о таком бренде :(")

    elif get_brand_from_message(message) == "audi":
        bot.send_message(message.chat.id, dbworker.find_models("audi"))
        bot.send_message(message.chat.id, "Какой-нибудь еще бренд или я могу отдыхать?")

    elif get_brand_from_message(message) == "porsche":
        bot.send_message(message.chat.id, dbworker.find_models("porsche"))
        bot.send_message(message.chat.id, "Какой-нибудь еще бренд или я могу отдыхать?")

    elif get_brand_from_message(message) == "vw":
        bot.send_message(message.chat.id, dbworker.find_models("vw"))
        bot.send_message(message.chat.id, "Какой-нибудь еще бренд или я могу отдыхать?")

    elif get_brand_from_message(message) == "stop":
        bot.send_message(message.chat.id, "Спасибо за использование, возвращайся снова!")



bot.polling(none_stop=True, interval=0)
