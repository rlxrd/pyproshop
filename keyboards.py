# Reply - снизу
# Inline - крепится к сообщению
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'),
     KeyboardButton(text='Контакты')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Цепочки', callback_data='chain'),
     InlineKeyboardButton(text='Браслеты', callback_data='bracelets')]
])


async def buy_item(item):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Купить', callback_data=f'buy_{item}')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]
    ])
