# from aiogram import Router, F
# from aiogram.types import Message, ChatPermissions
# from aiogram.filters import CommandStart, and_f
# import time


# router = Router()


# @router.message(CommandStart(), F.chat.type=="supergroup")
# async def StartBot(message: Message):
#     await message.answer(f"Assalomu aleykum {message.from_user.first_name}")


# @router.message(F.chat.type=="supergroup", F.new_chat_members)
# async def AddUsers(message: Message):
#     users = message.new_chat_members
#     for user in users:
#         await message.answer(f"Assalomu aleykum Guruhga xush kelibsiz\n\n{user.first_name}")


# @router.message(F.chat.type=="supergroup", F.left_chat_member)
# async def LeftUsers(message: Message):
#     user = message.left_chat_member
#     await message.answer(f"Xayr do'stim kelib turing: {user.first_name}")