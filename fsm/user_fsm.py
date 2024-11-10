from aiogram.fsm.state import StatesGroup, State


class HoldJson(StatesGroup):
    resp_json = State()