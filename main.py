from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from webScapping import searching
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    buttons = ['1 ოთახიანი', '2 ოთახიანი', '3 ოთახიანი']

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer('გამარჯობა, რამდენ ოთახიანი ბინა გნებავთ?', reply_markup=keyboard)


@dp.message_handler(Text(equals='1 ოთახიანი'))
async def one_room(message: types.Message):
    text = searching('1 ოთახიანი')
    for t in text:
        await message.answer(t)


@dp.message_handler(Text(equals='2 ოთახიანი'))
async def two_room(message: types.Message):
    text = searching('2 ოთახიანი')
    for t in text:
        await message.answer(t)


@dp.message_handler(Text(equals='3 ოთახიანი'))
async def three_room(message: types.Message):
    text = searching('3 ოთახიანი')
    for t in text:
        await message.answer(t)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
