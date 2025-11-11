from abc import ABC, abstractmethod

from maxo.bot.method_results.messages.callback_answer import CallbackAnswerResult
from maxo.omit import Omittable, Omitted
from maxo.types.callback import Callback
from maxo.types.new_message_body import NewMessageBody
from maxo.utils.facades.methods.base import BaseMethodsFacade


class CallbackMethodsFacade(BaseMethodsFacade, ABC):
    @property
    @abstractmethod
    def callback(self) -> Callback:
        raise NotImplementedError

    async def callback_answer(
        self,
        notification: Omittable[str | None] = Omitted(),
        message: NewMessageBody | None = None,
    ) -> CallbackAnswerResult:
        return await self.bot.callback_answer(
            callback_id=self.callback.callback_id,
            notification=notification,
            message=message,
        )
