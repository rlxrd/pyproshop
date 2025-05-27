from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards as kb

router = Router()


class Order(StatesGroup):
    name = State()
    phone = State()
    address = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в бот!',
                         reply_markup=kb.menu)
    await state.clear()


@router.callback_query(F.data == 'back_to_menu')
@router.message(F.text == 'Каталог')
async def catalog(event: Message | CallbackQuery):
    if isinstance(event, Message):
        await event.answer('Выберите тип товара',
                            reply_markup=kb.catalog)
    else:
        await event.message.delete()
        await event.message.answer('Выберите тип товара',
                            reply_markup=kb.catalog)
        await event.answer()


@router.callback_query(F.data == 'sneakers')
async def sneakers(callback: CallbackQuery):
    await callback.answer('Вы выбрали кроссовки')
    await callback.message.answer('Кроссовки Cortez\n\nЦена: 150$',
                                  reply_markup=await kb.buy_item(callback.data))


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали футболку')
    await callback.message.answer('Футболка Cortez\n\nЦена 100$',
                                  reply_markup=await kb.buy_item(callback.data))



@router.callback_query(F.data.startswith('buy_'))
async def buy_item(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Order.name)
    await state.update_data(item=callback.data.split('_')[1])
    await callback.message.answer('Введите ваше имя!')
    await callback.answer()


@router.message(Order.name)
async def order_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Order.phone)
    await message.answer('Введите ваш номер телефона')


@router.message(Order.phone)
async def order_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Order.address)
    await message.answer('Введите ваш адрес')


@router.message(Order.address)
async def order_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.bot.send_message(-1002641692539,
                                   text=f'{data["name"]}, {data["phone"]}, {data["address"]}, хочет купить {data["item"]}')
    await message.answer('Заказ оформлен!')
    await state.clear()


@router.message(Command('get_id'))
async def cmd_get_id(message: Message):
    await message.answer(f'{message.from_user.first_name}, вы прописали команду get_id!\n\nВаш ID: {message.from_user.id}\nID чата: {message.chat.id}')


@router.message(F.text == 'Привет')
async def msg_hello(message: Message):
    await message.reply('Привет, как дела?!')


@router.message(F.text == 'Хорошо!')
async def msg_nice(message: Message):
    await message.reply('Я за тебя рад!')

