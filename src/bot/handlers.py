from aiogram import Router
from aiogram.types import  Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile

from keyboard_button import get_yes_no_kb
from answers import first_message
from utils.yandex_map import get_adres
from utils.youmoney import YouMoneyPayment
from utils.google_sheets.google_table import Google_sheets


router = Router()

class ChooseCity(StatesGroup):
    choosing_City = State()


class ChooseDate(StatesGroup):
    choosing_date = State()


# async def get_yandex_map(city:str):
#     answer = get_adres(city)

# обработчик yandex карт, заправшивает город и сохраняет состояние
@router.message(Command('yandex'))
async def yandex_map(message: Message, state: FSMContext):
    await message.answer('Отлично, в каком городе нужен адреса?')
    await state.set_state(ChooseCity.choosing_City)


# следующий шаг по обработке города, получает город и возвращает url
@router.message(ChooseCity.choosing_City)
async def yandex_map_return_url(message: Message, state: FSMContext):
    if message.text[0] != '/':
        await state.update_data(chosen_city=message.text.lower())
        city = await state.get_data()
        url = await get_adres(city['chosen_city'])
        await message.answer(f'Вот где находится улица Ленина 1 в городе - {city["chosen_city"]}\n {url}')
        await state.clear()
    else:
        await state.clear()


# обработчик оплаты
@router.message(Command('pay'))
async def payment_handler(message: Message):
    user_id = str(message.from_user.id)
    client_pay = YouMoneyPayment(user_id, 2)
    await message.answer(f'Ссылка на оплату: {client_pay.invoice()}')


# обработчик отправки картинки
@router.message(Command('pict'))
async def image_handler(message: Message):
    image = FSInputFile("img/bart.jpg")
    await message.answer_photo(image,caption='а вот картиночка')

#обработчик команды гугл, который возвращает данные с ячейки А2
@router.message(Command('google'))
async def google_handler(message: Message):
    google_shet = await Google_sheets().extract_data_from_sheet('гугл_табличка')
    print(google_shet)
    await message.answer(f'такое значение лежит в А2 = {google_shet}')

#обрабочтик, который спрашивает дату, для последующий ее записи
@router.message(Command('date'))
async def add_date_handler(message: Message, state: FSMContext):
    await message.answer('Отлично, какую дату добавляем?')
    await state.set_state(ChooseDate.choosing_date)

#обработчик, которыё проверяет дату и записывает
@router.message(ChooseDate.choosing_date)
async def yandex_map_return_url(message: Message, state: FSMContext):
    # проверяем, что это была не команда
    if message.text[0] != '/':
        await state.update_data(choosing_date=message.text)
        #получаем и созраняем дату
        date = await state.get_data()
        #Google_sheets - класс для работы с таблицами гугла
        result = await Google_sheets().check_data('гугл_табличка', date['choosing_date'])
        print(date)
        await message.answer(result)
        await state.clear()
    else:
        await state.clear()

#команда старт, которая пишет приветственное сообщение
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(first_message, reply_markup=get_yes_no_kb())


