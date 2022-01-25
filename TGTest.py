import unittest
import mock
import TgBot
from unittest.mock import AsyncMock

class telegrambot_test(unittest.IsolatedAsyncioTestCase):
    def test(self):
        message = AsyncMock()
        await TgBot.all_tovar(message)
        ret = f"<b>..</b>\n" \
              f"..\n" \
              f"<strike>..</strike>\n" \
              f".."
        message.answer.assert_called_with(ret)
