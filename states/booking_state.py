from aiogram.fsm.state import State, StatesGroup

class BookingState(StatesGroup):
    name = State()
    phone = State()
    date = State()
    time = State()
    master = State()