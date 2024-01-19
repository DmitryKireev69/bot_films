from aiogram import Bot, Dispatcher, executor, types
import random

textWithFilms = open('films.txt', 'r', encoding='utf-8').read()
filmsList = textWithFilms.split(',')

def randomFilm():
    return filmsList[random.randint(0, len(filmsList) - 1)]


TOKEN_API = '6217754153:AAHJUgat2Q65s34xF-r_auVVZAcCvyWxD4k'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def handlerText(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="👋Получить рандомный фильм!!!")]],
        resize_keyboard=True)
    await message.reply(f"{randomFilm()}", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp)