import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
from config import bot_token, admin_id
import json
from main import new_tovar
from aiogram.dispatcher.filters import Text


bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    ''' Запускаем бота и выбираем нужную категорию. '''

    buttons = ['Все товары', 'Последние товары','Новые товары']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Привет! С помощью этого бота Вы можете отслеживать скидки на товары на сайте для кондитеров <b><a href = 'https://dvemorkovki.ru/catalog/'>Две морковки.</a></b>\nЧто хотите посмотреть?" ,reply_markup=keyboard)


@dp.message_handler(Text(equals='Все товары')) # код заимствован из youtube (https://www.youtube.com/watch?v=cfcn1-EzSbc&list=LL&index=5)
async def all_tovar(message: types.Message):
    ''' Выводим все товары из списка'''

    with open('tovar_dict.json') as file:
        tovar_dict = json.load(file)

    for k,v in reversed(tovar_dict.items()):
       tovar = f"<b>{v['article_title']}</b>\n" \
               f"{v['article_price']}\n" \
               f"<strike>{v['article_price_old']}</strike>\n" \
               f"{v['article_url']}"

       await message.answer(tovar)



@dp.message_handler(Text(equals='Последние товары'))
async def all_tovar(message: types.Message):
    ''' Выводим несколько последних товаров'''

    with open('tovar_dict.json') as file:
        tovar_dict = json.load(file)

    s=0
    for k,v in tovar_dict.items():
       tovar = f"<b>{v['article_title']}</b>\n" \
               f"{v['article_price']}\n" \
               f"<strike>{v['article_price_old']}</strike>\n" \
               f"{v['article_url']}"
       s+=1
       if s==6:
           break

       await message.answer(tovar)


@dp.message_handler(Text(equals='Новые товары'))
async def new_tovar(message: types.Message):
    ''' Выводим последние обновления - новые товары '''
    fresh_tovar = new_tovar(message)

    if len(fresh_tovar) >= 1:
       for k, v in (fresh_tovar.items()) :
            tovar = f"<b>{v['article_title']}</b>\n" \
                   f"{v['article_price']}\n" \
                    f"<strike>{v['article_price_old']}</strike>\n" \
                    f"{v['article_url']}"

            await message.answer(tovar)

    else:
        await message.answer('Новых товаров нет')

async def notice():
    '''Автоматически присылаем уведомления о новых товарах. '''
    while True:
        fresh_tovar = new_tovar(message)

        if len(fresh_tovar) >= 1:
            for k, v in (fresh_tovar.items()):
                tovar = f"<b>{v['article_title']}</b>\n" \
                        f"{v['article_price']}\n" \
                        f"<strike>{v['article_price_old']}</strike>\n" \
                        f"{v['article_url']}"

                await bot.send_message(admin_id,tovar)
        else:
            await bot.send_message(admin_id, "Новых товаров нет")

        await asyncio.sleep(10)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(notice())

    executor.start_polling(dp)