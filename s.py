# import logging
# import asyncio
# from aiogram import Dispatcher, Bot
# from user import router
# from config import bot_token, admins
# from karzinka import k_router
# from admin import a_router


# dp = Dispatcher()
# bot = Bot(token=bot_token)
# logging.basicConfig(level=logging.INFO)

# dp.include_router(router=k_router)
# dp.include_router(router=a_router)
# dp.include_router(router=router)



# async def main():
#     for id in admins:
#         await bot.send_message(chat_id=id, text="bot ishga tushdi")
#     await dp.start_polling(bot)



# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except:
#         print("tugadi")