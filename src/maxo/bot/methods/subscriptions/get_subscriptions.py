from maxo.bot.methods.base import MaxoMethod
from maxo.types.get_subscriptions_result import GetSubscriptionsResult


class GetSubscriptions(MaxoMethod[GetSubscriptionsResult]):
    """
    Получение подписок

    Если ваш бот получает данные через Webhook, этот метод возвращает список всех подписок. При настройке уведомлений для production-окружения рекомендуем использовать Webhook

    >Обратите внимание: для отправки вебхуков поддерживается только протокол HTTPS, включая самоподписанные сертификаты. HTTP не поддерживается

    Пример запроса:
    ```bash
    curl -X GET "https://platform-api.max.ru/subscriptions" \
      -H "Authorization: {access_token}"
    ```

    Источник: https://dev.max.ru/docs-api/methods/GET/subscriptions
    """

    __url__ = "subscriptions"
    __method__ = "get"
