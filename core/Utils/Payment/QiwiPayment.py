import datetime
import uuid
import pyqiwi

from settings import qiwi_settings

wallet = pyqiwi.Wallet(token=qiwi_settings.QIWI_TOKEN, number=qiwi_settings.QIWI_WALLET)

class NotEnoughMoney(Exception):
    pass

class NotPaymentFound(Exception):
    pass


class QiwiPayment():
    id: str = None
    amount: int

    @classmethod
    async def create_payment(cls, amount):
        payment = cls()
        payment.id = str(uuid.uuid4())
        payment.amount = amount
        return payment

    @classmethod
    async def get_payment(cls, id, amount):
        payment = cls()
        payment.id = id
        payment.amount = amount
        return payment

    async def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date).get('transactions')
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in transaction.comment:
                    if int(transaction.total.amount) >= int(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            return False

    async def get_invoice_link(self):
        link = 'https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}'
        return link.format(pubkey=qiwi_settings.QIWI_P_PUBLIC, amount=self.amount, comment=self.id)
