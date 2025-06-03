# Reply - снизу
# Inline - крепится к сообщению
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.requests import get_categories, get_product_by_category

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'),
     KeyboardButton(text='Контакты')]
],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню...',
one_time_keyboard=True)


async def catalog():
    keyboard = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        keyboard.row(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    return keyboard.as_markup()


async def products(category_id):
    keyboard = InlineKeyboardBuilder()
    all_products = await get_product_by_category(category_id)
    for product in all_products:
        keyboard.row(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
    return keyboard.as_markup()


async def buy_item(item):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Купить', callback_data=f'buy_{item}')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]
    ])


get_contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить контакт', request_contact=True)]
])