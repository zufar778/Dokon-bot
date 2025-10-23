from aiogram.fsm.state import State, StatesGroup

class Product(StatesGroup):
    all = State()
    go = State()
    yes = State()
    no = State()


class Karzinka(StatesGroup):
    contact = State()
    location = State()
    confirmation = State()