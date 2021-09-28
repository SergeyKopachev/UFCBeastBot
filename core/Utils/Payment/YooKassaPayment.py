from yookassa import Configuration, Payment

from settings import yookassa_settings


# Модуль взаимодействия с сервисом ЮКасса
class YookassaPayment():

    @classmethod
    async def create_payment(cls, name, amount, return_url):
        await cls.__configuration_api()
        payment: Payment = Payment.create({
            "amount": {
                "value": amount,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": return_url
            },
            "capture": True,
            "description": name
        })

        return payment

    @classmethod
    async def check_payment_status(cls, id):
        await cls.__configuration_api()

        payment = Payment.find_one(id)
        return payment.status

    @classmethod
    async def __configuration_api(cls):
        Configuration.account_id = yookassa_settings.shop_id
        Configuration.secret_key = yookassa_settings.api_key
