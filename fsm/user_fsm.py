from aiogram.fsm.state import StatesGroup, State

class Hold(StatesGroup):
    resp_json = State()
    img_base64 = State()
