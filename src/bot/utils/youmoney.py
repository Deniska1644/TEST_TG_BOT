import sys
import os
from yoomoney import Client
from yoomoney import Quickpay


sys.path.append(os.path.join(sys.path[0], 'bot'))

from config import YOU_MONEY_TOCKEN




class YouMoneyPayment():
    CLIENT = Client(YOU_MONEY_TOCKEN)

    def __init__(self, user_id:str, cost:float):
        self.user_id = user_id
        self.cost = cost

    def invoice(self):
        quickpay = Quickpay(
            receiver="4100118741483456",
            quickpay_form="shop",
            targets="test",
            paymentType="SB",
            sum=self.cost,
            label=self.user_id,
        )
        return quickpay.base_url
    
#     def chek_payment(self):
#         history = self.CLIENT.operation_history(label=self.user_id)
        # print("Next page starts with: ", history.next_record)
        # for operation in history.operations:
        #     print()
        #     print("Operation:",operation.operation_id)
        #     print("\tStatus     -->", operation.status)
        #     print("\tDatetime   -->", operation.datetime)
        #     print("\tTitle      -->", operation.title)
        #     print("\tPattern id -->", operation.pattern_id)
        #     print("\tDirection  -->", operation.direction)
        #     print("\tAmount     -->", operation.amount)
        #     print("\tLabel      -->", operation.label)
        #     print("\tType       -->", operation.type)


# a = YouMoneyPayment('122', 12.22)

# print(a.invoice())
# print(a.chek_payment())

