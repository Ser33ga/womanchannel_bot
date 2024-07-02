from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_id: str) -> None:
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id

class IsParser(BaseFilter):
    def __init__(self, parser_id: str) -> None:
        self.parser_id = parser_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.parser_id