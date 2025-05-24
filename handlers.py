from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!',
                         reply_markup=kb.menu)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите тип товара',
                         reply_markup=kb.catalog)


@router.callback_query(F.data == 'sneakers')
async def cmd_sneakers(callback: CallbackQuery):
    await callback.answer("Вы выбрали кроссовки!",
                          show_alert=True)
    await callback.message.answer('Вы выбрали sneakers!',
                                  reply_markup=ReplyKeyboardRemove())


@router.message(Command('get_id'))
async def cmd_get_id(message: Message):
    await message.answer(f'{message.from_user.first_name}, вы прописали команду get_id!\n\nВаш ID: {message.from_user.id}')


@router.message(F.text == 'Привет')
async def msg_hello(message: Message):
    await message.reply('Привет, как дела?!')


@router.message(F.text == 'Хорошо!')
async def msg_nice(message: Message):
    await message.reply('Я за тебя рад!')
