from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from states import Karzinka
from db import karz
from inline_buttons import order, purchase
from reply import contact_phone, location_button
from config import admins


z_router = Router()


@z_router.callback_query(F.data=="Karzinka")
async def see(call: CallbackQuery):
    user_id = call.from_user.id
    await call.message.answer("Purchased products")
    jami_summa = 0
    text = ""
    for i in karz(user_id):
        jami_summa += i[3]
        text += f"Name: {i[2]}\nPrice: {i[3]/i[4]} so'm\nCount: {i[4]}\nSumm: {i[3]} so'm\n\n"
    await call.message.answer(text=f"{text}\n\nOverall summ: {jami_summa}", reply_markup=order)


@z_router.callback_query(F.data=="Order")
async def KarzinkaBot(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Send your contact", reply_markup=contact_phone)
    await state.set_state(Karzinka.contact)


@z_router.message(F.contact, Karzinka.contact)
async def ContactBot(message: Message, state: FSMContext):
    tel = message.contact.phone_number
    await state.update_data({"telefon":tel})
    await message.answer(text="Send your location", reply_markup=location_button)
    await state.set_state(Karzinka.location)


@z_router.message(F.location, Karzinka.location)
async def LocationBot(message: Message, state: FSMContext):
    la = message.location.latitude
    lo = message.location.longitude
    await state.update_data({"la":la, "lo":lo})
    await state.set_state(Karzinka.confirmation)
    await message.answer("Confirmation", reply_markup=purchase)


@z_router.callback_query(F.data == "Yes", Karzinka.confirmation)
async def AdminBot(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = await state.get_data()
    contact = data.get("telefon")
    la = data.get("la")
    lo = data.get("lo")
    jami_summa = 0
    text = ""
    for i in karz(user_id):
        jami_summa += i[3]
        text += f"Name: {i[2]}\nPrice: {i[3]/i[4]} so'm\nCount: {i[4]}\nSumm: {i[3]} so'm\n\n"
    await call.bot.send_location(chat_id=admins[0], latitude=la, longitude=lo)
    await call.bot.send_message(chat_id=admins[0], text=f"Telefon: {contact}\n{text}\n\nOverall summ: {jami_summa}", reply_markup=purchase)